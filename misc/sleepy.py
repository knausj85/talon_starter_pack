from talon.voice import Context, ContextGroup
from talon.engine import engine
from talon_plugins import speech, eye_mouse, eye_zoom_mouse
import subprocess
import win32gui
import win32con
import ctypes
import os
import winreg
import platform

sleep_group = ContextGroup("sleepy")
sleepy = Context("sleepy", group=sleep_group)

default_cursor = {
"AppStarting": "%SystemRoot%\\Cursors\\aero_working.ani",
"Arrow": "%SystemRoot%\\Cursors\\aero_arrow.cur",
"Hand": "%SystemRoot%\\Cursors\\aero_link.cur",
"Help": "%SystemRoot%\\Cursors\\aero_helpsel.cur",
"No": "%SystemRoot%\\Cursors\\aero_unavail.cur",
"NWPen": "%SystemRoot%\\Cursors\\aero_pen.cur",
"Person": "%SystemRoot%\\Cursors\\aero_person.cur",
"Pin": "%SystemRoot%\\Cursors\\aero_pin.cur",
"SizeAll": "%SystemRoot%\\Cursors\\aero_move.cur",
"SizeNESW": "%SystemRoot%\\Cursors\\aero_nesw.cur",
"SizeNS": "%SystemRoot%\\Cursors\\aero_ns.cur",
"SizeNWSE": "%SystemRoot%\\Cursors\\aero_nwse.cur",
"SizeWE": "%SystemRoot%\\Cursors\\aero_ew.cur",
"UpArrow": "%SystemRoot%\Cursors\\aero_up.cur",
"Wait": '%SystemRoot%\\Cursors\\aero_busy.ani',
"Crosshair": "",
"IBeam":"",
}

hidden_cursor = "%AppData%\\talon\\user\\talon_starter_pack-master\\misc\\HiddenCursor.cur"

def show_cursor(show):
    if "Windows-10" in platform.platform(terse=True):
        try:
            Registrykey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\Cursors", 0, winreg.KEY_WRITE)

            for value_name, value in default_cursor.items():   
                if show: 
                    winreg.SetValueEx(Registrykey, value_name, 0, winreg.REG_EXPAND_SZ, value)
                else:
                    winreg.SetValueEx(Registrykey, value_name, 0, winreg.REG_EXPAND_SZ, hidden_cursor)
                    
            winreg.CloseKey(Registrykey)

            ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETCURSORS, 0, None, 0)
        except WindowsError:
            print("Unable to show_cursor({})".format(str(show)))

def wake_or_sleep(wake_up):
    if wake_up:
        eye_zoom_mouse.zoom_mouse.enable()
        eye_mouse.control_mouse.enable() 
        show_cursor(False)
    else:
        eye_zoom_mouse.zoom_mouse.disable()
        eye_mouse.control_mouse.disable()
        engine.mimic("go to sleep".split())
        show_cursor(True)

sleepy.keymap( 
    {
        "talon sleep": lambda m: speech.set_enabled(False),
        "talon wake": lambda m: speech.set_enabled(True),
        "dragon mode": lambda m: speech.set_enabled(False),
        "talon mode": lambda m: speech.set_enabled(True),
        "sleep all" : lambda m: wake_or_sleep(False),
        "welcome back": lambda m: wake_or_sleep(True),
        "curse yes": lambda m: show_cursor(True),
        "curse no": lambda m: show_cursor(False),
    }
)

sleep_group.load()
