import os
import serial
from inputs import get_gamepad


if os.name == "nt":
    USB_PORT = "COM3" #Windows (garbage)
else:
    USB_PORT = "/dev/ttyACM0" #actually good operating systems

    
def establish_serial() -> serial.Serial:
    """Create serial connection between the host and the Arduino."""
    try:
        usb = serial.Serial(USB_PORT, 9600, timeout=2) #9600 baud
        return usb
    except Exception as e:
        print(e)
        print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
        print("Exiting program.")
        exit()


def convbits16_8(x: int) -> int:
    """Convert 16 bit controller state to 8 bits."""
    return (x + 32768) >> 8


def main():
    """Main entry point."""
    usb = establish_serial()

    left_stick_x = 128 #0 to 255, 8 bits
    left_stick_y = 128 #0 to 255, 8 bits
    right_stick_x = 128 #0 to 255, 8 bits
    right_stick_y = 128 #0 to 255, 8 bits
    dpad_x = 0 #-1 to 1, 2 bits
    dpad_y = 0 #-1 to 1, 2 bits

    # Codes:
    # LSTICK:   8 bits _ 8 bits + 8 bits    = 24 bits
    # RSTICK:   8 bits _ 8 bits + 8 bits    = 24 bits
    # BUTTONS:  8 bits _ 8 bits             = 16 bits
    #
    # Codes Alternative:
    # CODE: 8 bits
    # LSTICK:   8 bits + 8 bits    = 16 bits
    # RSTICK:   8 bits + 8 bits    = 16 bits
    # BUTTONS:  8 bits             = 8 bits

    # For the buttons, the lowest 4 bits represent the four buttons,
    # and the dpad has 9 states, so 4 bits to represent those.
    # Can say lowest bit here is x -1 or 1, second lowest is x 0 or otherwise,
    # third lowest is y -1 or 1, highest is y 0 or otherwise.

    while True:
        events = get_gamepad()
        for event in events:
            #if event.code == "BTN_SOUTH" and event.state == 1:
            #    usb.write((1).to_bytes())
            match event.code:
                case "ABS_X":
                    left_stick_x = convbits16_8(event.state)
                case "ABS_Y":
                    left_stick_y = convbits16_8(event.state)
                case "ABS_RX":
                    right_stick_x = convbits16_8(event.state)
                case "ABS_RY":
                    right_stick_y = convbits16_8(event.state)
                case "ABS_HAT0X":
                    dpad_x = event.state
                case "ABS_HAT0Y":
                    dpad_y = event.state

            #if event.code == "ABS_X":
            #    #new_val = int((event.state + 32768) >> 8)
            #    new_val = convbits16_8(event.state)
            #    #print(new_val.to_bytes())
            #    usb.write(new_val.to_bytes())
            #if event.code == "ABS_HAT0X":
            #    print(event.state)


if __name__ == "__main__":
    main()


