from time import sleep

import win32con
import win32api
from win32api import keybd_event, mouse_event

from key_map import KEYS

class MyWinApi():
    def __init__(self, screen_x,screen_y, letter_delay):
        self._screen_x = screen_x
        self._screen_y = screen_y
        self._letter_delay = letter_delay

    def key_down(self, key):
        keybd_event(KEYS[key], 0, 1, 0)

    def key_up(self, key):
        keybd_event(KEYS[key], 0, win32con.KEYEVENTF_EXTENDEDKEY  | 
        win32con.KEYEVENTF_KEYUP, 0)

    def press_key(self, key: str):
        keybd_event(KEYS[key],0,1,0)
        sleep(self._letter_delay)
        keybd_event(KEYS[key],0 ,win32con.KEYEVENTF_KEYUP ,0)

    def type_word(self, word: str):
        for char in word:
            if char.isalpha():
                self.press_key(char.lower())
            else:
                self.press_key(char)
        
    def left_click_down(self):
        mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        
    def right_click_down(self):
        mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        
    def left_click_up(self):
        mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        
    def right_click_up(self):
        mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        
    def left_click(self):
        mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        
    def right_click(self):
        mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

    def mouse_top_left(self):
        win32api.SetCursorPos([0,0])

    def mouse_bottom_left(self):
        win32api.SetCursorPos([0,self._screen_y])

