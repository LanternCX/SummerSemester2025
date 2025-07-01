import machine

button_pin = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)


def button_callback(pin):
    if pin.value() == 0:
        print("按键按下")
    else:
        print("按键释放")


button_pin.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING,
               handler=button_callback)

while True:
    pass
