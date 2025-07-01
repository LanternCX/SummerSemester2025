from machine import Pin
from machine import Timer

led = Pin(19, Pin.OUT)


# LED callback
def flash(t):
    global stat, led
    if stat:
        led.value(1)
        print("LED OFF")
        stat = False
    else:
        led.value(0)
        print("LED ON")
        stat = True


stat = False
timer = Timer(1)
timer.init(period=1000, mode=Timer.PERIODIC, callback=flash)


def cleanup():
    print("clean up...")
    # deinit time
    timer.deinit()
    # led off
    led.value(1)
    print("clean up done.")


try:
    while True:
        pass
finally:
    cleanup()