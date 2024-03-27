#from __future__ import print_function

#imports
from inputs import get_gamepad
import serial

def main():
    try:
        usb = serial.serial(USB_PORT, 9600, timeout = 2)
    except:
        print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
        print("Exiting program.")
        exit()
    
    A_state = False

    while 1:
        events = get_gamepad()
        for event in events:
            #print(event.ev_type, event.code, event.state)
            if event.code == "BTN_SOUTH" and event.state == 1:
                A_state = not A_state
                print(A_state)


if __name__ == "__main__":
    main()

