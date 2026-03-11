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
            pydirectinput.keyDown('left')
            
            for _ in range(int(hold_time * 10)):
                if keyboard.is_pressed('esc'):
                    pydirectinput.keyUp('left')
                    print("\nStopping program")
                    return
                time.sleep(0.1)
            
            pydirectinput.keyUp('left')
            time.sleep(release_time)


            pydirectinput.keyDown('right')
            
            for _ in range(int(hold_time * 10)):
                if keyboard.is_pressed('esc'):
                    pydirectinput.keyUp('right')
                    print("\nStopping program")
                    return
                time.sleep(0.1)
            
            pydirectinput.keyUp('right')
            time.sleep(release_time)
                
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    initiate()