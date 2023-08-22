import os
import time
import keyboard
import pyautogui as pg


def home_page():
    keyboard.press_and_release('Win+d')
    time.sleep(1)


def open_chrome():
    file_path_chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    os.startfile(file_path_chrome)


def open_discord():
    file_path_discord = "C:\\Users\\dimak\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\Discord.lnk"
    os.startfile(file_path_discord)


def open_steam():
    file_path_steam = "E:\Steam\steam.exe"
    os.startfile(file_path_steam)


def open_edge():
    file_path_edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    os.startfile(file_path_edge)


def open_telegram():
    file_path_telegram = "C:\\Users\dimak\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk"
    os.startfile(file_path_telegram)


def open_binance():
    pg.hotkey("winleft")
    pg.typewrite("Binance")
    time.sleep(1)
    pg.press("Enter")


def open_trello():
    pg.hotkey("winleft")
    pg.typewrite("Trello")
    time.sleep(1)
    pg.press("Enter")


def open_spotify():
    pg.hotkey("winleft")
    pg.typewrite("Spotify")
    time.sleep(1)
    pg.press("Enter")


