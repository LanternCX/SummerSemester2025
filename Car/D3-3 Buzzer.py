import machine
import time

BUZZER_PIN = 25

buzzer = machine.PWM(machine.Pin(BUZZER_PIN))
buzzer.freq(2000)


# 退出清理
def cleanup():
    print("clean up...")
    # 关闭蜂鸣器
    buzzer.duty(1023)
    print("clean up done.")


try:
    while True:
        # 蜂鸣器低电平触发，占空比越低音调越高
        buzzer.duty(512)
        time.sleep(1)
        print("buzzer-duty: 50%")

        buzzer.duty(0)
        time.sleep(1)
        print("buzzer-duty: 0%")
finally:
    cleanup()
