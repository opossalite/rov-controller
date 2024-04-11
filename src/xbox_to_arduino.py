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
        # figure out which messages we need to send
        left_stick = False
        right_stick = False
        buttons = False #includes dpad
        button_codes = 0 #initially just used for 

        events = get_gamepad()
        for event in events:
            match event.code:
                case "ABS_X":
                    left_stick_x = event.state
                    left_stick = True
                case "ABS_Y":
                    left_stick_y = event.state
                    left_stick = True
                case "ABS_RX":
                    right_stick_x = event.state
                    right_stick = True
                case "ABS_RY":
                    right_stick_y = event.state
                    right_stick = True
                case "ABS_HAT0X":
                    dpad_x = event.state
                    buttons = True
                case "ABS_HAT0Y":
                    dpad_y = event.state
                    buttons = True
                case "BTN_NORTH":
                    button_codes |= 1
                    buttons = True
                case "BTN_SOUTH":
                    button_codes |= 1 << 1
                    buttons = True
                case "BTN_WEST":
                    button_codes |= 1 << 2
                    buttons = True
                case "BTN_EAST":
                    button_codes |= 1 << 3
                    buttons = True

            #if event.code == "ABS_X":
            #    #new_val = int((event.state + 32768) >> 8)
            #    new_val = convbits16_8(event.state)
            #    #print(new_val.to_bytes())
            #    usb.write(new_val.to_bytes())
            #if event.code == "ABS_HAT0X":
            #    print(event.state)

        # prepare variables for building message
        message_codes = 0
        message: list[bytes] = [b""]

        # build the serial messages
        if left_stick:
            message_codes |= 1
            message.append(convbits16_8(left_stick_x).to_bytes())
            message.append(convbits16_8(left_stick_y).to_bytes())
        if right_stick:
            message_codes |= 1 << 1
            message.append(convbits16_8(right_stick_x).to_bytes())
            message.append(convbits16_8(right_stick_y).to_bytes())
        if buttons:
            message_codes |= 1 << 2
            if dpad_x != 0:
                button_codes |= 1 << 5
                button_codes |= int(dpad_x == 1) << 4
            if dpad_y != 0:
                button_codes |= 1 << 7
                button_codes |= int(dpad_y == 1) << 6
            message.append(button_codes.to_bytes())

        # send the message if there is something to send
        if message_codes > 0:
            message[0] = message_codes.to_bytes() #plug in all codes we're sending
            for chunk in message:
                usb.write(chunk)


if __name__ == "__main__":
    main()


