import ctypes
from time import sleep

import pyautogui  # type: ignore
from pynput.keyboard import Key, Listener  # type: ignore
from pynput.keyboard._base import KeyCode  # type: ignore

# set the title of the window, otherwise it'll be generic "python" or similar
ctypes.windll.kernel32.SetConsoleTitleW("Autoclicker")

#  ======== settings ========
delay = 1  # in seconds
resume_key: KeyCode = Key.f1
pause_key: KeyCode = Key.f2
exit_key: KeyCode = Key.f3
#  ==========================

pause = True
running = True
position1: pyautogui.Point | None = None
position2: pyautogui.Point | None = None


def on_press(key: KeyCode) -> None:
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls() -> None:
    print("\nAutoClicker by iSayChris")
    print(" - Settings: ")
    print("\t delay = " + str(delay) + " sec" + "\n")
    print(" - Controls:")
    print(f"\t {resume_key.name} = Resume")
    print(f"\t {pause_key.name} = Pause")
    print(f"\t {exit_key.name} = Exit")
    print("-----------------------------------------------------")
    print(f"Press {resume_key.name} to start ...")


def get_mouse_position() -> pyautogui.Point:
    input("Move your mouse to the desired position and press Enter...")
    return pyautogui.position()


def main() -> None:
    global running, position1, position2

    # Get the two positions from the user
    print("First, let's set up your clicking positions:")
    print("\nPosition 1:")
    position1 = get_mouse_position()
    print(f"Position 1 set at: {position1}")

    print("\nPosition 2:")
    position2 = get_mouse_position()
    print(f"Position 2 set at: {position2}")

    lis = Listener(on_press=on_press)  # type: ignore
    lis.start()

    display_controls()
    while running:
        if not pause:
            # Click position 1
            pyautogui.click(position1)
            pyautogui.PAUSE = delay

            # Click position 2
            pyautogui.click(position2)
            pyautogui.PAUSE = delay
        else:
            sleep(delay)  # otherwise it uses 100% CPU

    print("\n[Exit]")
    lis.stop()


if __name__ == "__main__":
    main()
