import time
import mouse

while True:
    mouse.move(200,0, absolute=True, duration=3)
    time.sleep(400)
    mouse.move(0,0, absolute=True, duration=3)
    time.sleep(4)