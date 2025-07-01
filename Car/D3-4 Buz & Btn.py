import machine

BUZZER_PIN = 25
button_pin = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
buzzer = machine.PWM(machine.Pin(BUZZER_PIN))
buzzer.freq(2000)
buzzer.duty(1023)

stat = 0


def button_callback(pin):
    global stat
    if pin.value() == 0:
        stat = not stat
        if stat == 1:
            # Buz off
            buzzer.duty(0)
        else:
            # Buz off
            buzzer.duty(1023)
        print("Btn Down")
        print(f"Buz stat: {stat}")
    else:
        print("Btn Up")


button_pin.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING,
               handler=button_callback)


# clean up
def cleanup():
    print("clean up...")
    # Buz off
    buzzer.duty(1023)
    print("clean up done.")


try:
    while True:
        pass
finally:
    cleanup()
