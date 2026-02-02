import pydirectinput
import keyboard
import time

initialWaitTime = 4
clickWaitTime = 0.2
cycleInterval = 0.2

buttonOneX, buttonOneY = 880, 1010
buttonTwoX, buttonTwoY = 920, 650

def initiate():
    print("-- MOUSE COMBO INITIATED --")
    time.sleep(initialWaitTime)

    try:
        while True:
            pydirectinput.moveTo(buttonOneX, buttonOneY)
            pydirectinput.mouseDown()
            time.sleep(clickWaitTime)
            pydirectinput.mouseUp()
            
            time.sleep(0.2)
            
            pydirectinput.moveTo(buttonTwoX, buttonTwoY)
            pydirectinput.mouseDown()
            time.sleep(clickWaitTime)
            pydirectinput.mouseUp()

            for _ in range(int(cycleInterval * 10)):
                if keyboard.is_pressed('esc'):
                    print("\nStopping program")
                    return
                time.sleep(0.1)

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    initiate()