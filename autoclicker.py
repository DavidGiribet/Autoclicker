import pydirectinput
import keyboard
import time

interval = 1
initialWaitTime = 4

def iniciar():
    print("--AUTOCLICKER INITIATED--")
    
    time.sleep(initialWaitTime)  

    try:
        while True:
            pydirectinput.press('space')
            
            for _ in range(int(interval * 10)):
                if keyboard.is_pressed('esc'):
                    print("\nStopping program")
                    return
                time.sleep(0.1)
                
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    iniciar()