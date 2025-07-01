from machine import Pin
import time
led = Pin(19, Pin.OUT)
while True:
    led.on()
    print("LED on!")
    time.sleep(1)
    led.off()
    print("LED off!")
    time.sleep(1)