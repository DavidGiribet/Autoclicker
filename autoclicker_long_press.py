import pydirectinput
import keyboard
import time

hold_time = 1.9
release_time = 0.1
initial_wait = 4

def initiate():
    print("-- HOLD BUTTON AUTOCLICKER INITIATED --")
    time.sleep(initial_wait)

    try:
        while True:
            pydirectinput.keyDown('e')
            
            for _ in range(int(hold_time * 10)):
                if keyboard.is_pressed('esc'):
                    pydirectinput.keyUp('e')
                    print("\nStopping program")
                    return
                time.sleep(0.1)
            
            pydirectinput.keyUp('e')
            time.sleep(release_time)
                
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    initiate()