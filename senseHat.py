from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

b = (0, 0, 0)  # black
r = (255, 0, 0)  # red

up_down_pixels = [
    b, b, b, b, b, b, b, b,
    b, b, b, r, b, b, b, b,
    b, b, r, b, b, b, b, b,
    b, r, r, r, r, r, r, b,
    b, b, r, b, b, b, b, b,
    b, b, b, r, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b]

left_right_pixels = [
    b, b, b, b, b, b, b, b,
    b, b, b, r, b, b, b, b,
    b, b, r, r, r, b, b, b,
    b, r, b, r, b, r, b, b,
    b, b, b, r, b, b, b, b,
    b, b, b, r, b, b, b, b,
    b, b, b, r, b, b, b, b,
    b, b, b, b, b, b, b, b]

while True:
    # go throw all joystick’s events
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            # Check which direction
            if event.direction == "up":
                sense.set_pixels(up_down_pixels)  # Up arrow
            elif event.direction == "down":
                sense.set_pixels(up_down_pixels)
                sense.flip_h()  # Down arrow
            elif event.direction == "left":
                sense.set_pixels(left_right_pixels)
                sense.flip_v()  # Left arrow
            elif event.direction == "right":
                sense.set_pixels(left_right_pixels)  # Right arrow
            elif event.direction == "middle":
                sense.show_letter("M")  # Enter key

             # Wait a while and then clear the screen
            sleep(0.5)
            sense.clear()