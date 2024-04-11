from inputs import get_gamepad

'''
ABS_X       left stick x
ABS_Y       left stick y
ABS_RX      right stick x
ABS_RY      right stick y
BTN_THUMBL  left stick down
BTN_THUMBR  right stick down
ABS_Z       left trigger
ABS_RZ      right trigger
BTN_TL      left button
BTN_TR      right button
BTN_NORTH   main cluster (some letter)
BTN_SOUTH   main cluster (some letter)
BTN_WEST    main cluster (some letter)
BTN_EAST    main cluster (some letter)
ABS_HAT0X   dpad x
ABS_HAT0Y   dpad y
BTN_START   start
BTN_SELECT  select
BTN_MODE    home
'''


while True:
    events = get_gamepad()
    for event in events:
        #print(event.code)
        #if event.code == "BTN_SOUTH" and event.state == 1:
        #    usb.write((1).to_bytes())
        if event.code == "ABS_X":
            new_val = int((event.state + 32768) >> 8)
            print(new_val)
        if event.code == "ABS_HAT0X":
            print(event.state)


