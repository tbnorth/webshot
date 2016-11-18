"""
webshot.py - screen shot a window

http://stackoverflow.com/q/3586046/1072212

Terry N Brown, terrynbrown@gmail.com, Fri Nov 18 13:31:59 2016
"""

import re
import sys
import win32con
import win32gui
import win32ui


def do_shot(window_pattern, bmpfilenamename, top, left, bottom, right):

    window_re = re.compile(window_pattern)

    def callback(hwnd, main):
        """from win32gui.EnumWindows, per window handle (hwnd)"""
        text = (win32gui.GetWindowText(hwnd))
        if window_re.search(text) and win32gui.IsWindowVisible(hwnd):
            windows.append(hwnd)

    windows = []
    win32gui.EnumWindows(callback, 0)

    if not windows:
        print("Didn't find window matching '%s'" % window_pattern)
        exit(1)
    if len(windows) > 1:
        print("NOTE: %d windows matched '%s'" % (len(windows), window_pattern))

    hwnd = windows[0]

    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x - left - right
    h = rect[3] - y - top - bottom

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h) , dcObj, (left, top), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


def main():

    window_pattern, bmpfilenamename = sys.argv[1:3]
    top, left, bottom, right = map(int, sys.argv[3:7])
    do_shot(window_pattern, bmpfilenamename, top, left, bottom, right)

if __name__ == '__main__':
    main()
