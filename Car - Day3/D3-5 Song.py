import machine
import time

notes = {
    'C': 262,
    'D': 294,
    'E': 330,
    'F': 349,
    'G': 392,
    'A': 440,
    'B': 494,
    'C5': 523
}
# 蜂鸣器引脚
BUZZER_PIN = 25 
# 设置PWM输出引脚
buzzer = machine.PWM(machine.Pin(BUZZER_PIN))


# clean up
def cleanup():
    print("clean up...")
    # Buz off
    buzzer.duty(1023)
    print("clean up done.")


def play_tune():
    # 定义频率和持续时间
    tune = ['C', 'C', 'G', 'G', 'A', 'A', 'G', 'F', 'F', 'E', 'E', 'D', 'D', 'C']
    duration = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2]
    for i in range(len(tune)):
        frequency = notes[tune[i]]
        print(f"freq: {frequency}")
        if frequency == 0:
            buzzer.duty(1023)
        else:
            buzzer.freq(frequency)
            buzzer.duty(512)
        time.sleep(duration[i] * 0.25)
        buzzer.duty(1023)
        time.sleep(0.05)


try:
    # 播放音乐
    while True:
        play_tune()
finally:
    cleanup()
