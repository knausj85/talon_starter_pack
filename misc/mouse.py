# From https://github.com/talonvoice/examples
import time
from talon import ctrl, tap, ui, noise
from talon.voice import Context, Key
from talon_plugins import eye_mouse, eye_zoom_mouse
import win32gui 
import win32con
import os

ctx = Context("mouse")

#history is used exclusively for drag currently.
x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None

def toggle_zoom_mouse(m):
    if eye_zoom_mouse.zoom_mouse.enabled:
        try:
            eye_zoom_mouse.zoom_mouse.disable()
        except:
            eye_zoom_mouse.zoom_mouse.enabled = False
    else:
        eye_zoom_mouse.zoom_mouse.enable()

def on_move(typ, e):
    mouse_history.append((e.x, e.y, time.time()))
    if force_move:
        e.x, e.y = force_move
        return True

def on_pop(m):
    if not eye_zoom_mouse.zoom_mouse.enabled:
        click("")
        
noise.register('pop', on_pop)
# tap.register(tap.MMOVE, on_move)

# def click_pos(m):
    # word = m[0]
    # start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0
    # diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    # return pos[:2]

def click(m, button=0, repeat=1, force_zoom_when_zm_active=False):     
    call_on_pop = force_zoom_when_zm_active and eye_zoom_mouse.zoom_mouse.enabled and eye_zoom_mouse.zoom_mouse.state == eye_zoom_mouse.STATE_IDLE

    if call_on_pop:
        eye_zoom_mouse.zoom_mouse.on_pop(eye_zoom_mouse.zoom_mouse.state)
    
    else:
        for n in range(repeat):
            ctrl.mouse_click(button=button)
            
        #cancel zoom mouse if pending
        if eye_zoom_mouse.zoom_mouse.enabled:
            eye_zoom_mouse.zoom_mouse.cancel()
     
     
def right_click(m):
    click(m, button=1)

def dubclick(m):
    click(m, repeat=2)
  
def tripclick(m):
    click(m, repeat=3)

def press_key_and_click(m, key, button=0, times=1):
    ctrl.key_press(key, down=True)
    ctrl.mouse_click(button=button, times=times, wait=16000)
    ctrl.key_press(key, up=True)

def mouse_scroll(amount):
    def scroll(m):
        ctrl.mouse_scroll(y=amount)

    return scroll


def mouse_smooth_scroll(amount):
    def scroll(m):
        if SCROLL_TOTAL_TIME != 0:
            interval = 0.007
            depth = int(SCROLL_TOTAL_TIME // interval)
            split = amount / depth
            for x in range(depth):
                ctrl.mouse_scroll(y=split)
                time.sleep(interval)
        else:
            ctrl.mouse_scroll(y=amount)
    return scroll

is_dragging = False
def mouse_drag(m):
    global is_dragging 
    is_dragging = not is_dragging
    if is_dragging:
       ctrl.mouse_click(down=True)
    else:
       ctrl.mouse_click(up=True)

def shift_click(m, button=0, times=1):
    press_key_and_click(m, "shift", button, times)


def control_click(m, button=0, times=1):
    press_key_and_click(m, "control", button, times)


def command_click(m, button=0, times=1):
    press_key_and_click(m, "cmd", button, times)


def control_shift_click(m, button=0, times=1):
    ctrl.key_press("shift", ctrl=True, shift=True, down=True)
    ctrl.mouse_click(x, y, button=button, times=times, wait=16000)
    ctrl.key_press("shift", ctrl=True, shift=True, up=True)

ctx.keymap(
    {
        "debug overlay": lambda m: eye_mouse.debug_overlay.toggle(),
        "control mouse": lambda m: eye_mouse.control_mouse.toggle(),
        "zoom mouse": toggle_zoom_mouse,
        "camera overlay": lambda m: eye_mouse.camera_overlay.toggle(),
        "(click | chiff | pop | tap | tea)": lambda m: click(m, force_zoom_when_zm_active=True),
        "(q-tip | cutey | q click)": lambda m: click(m, force_zoom_when_zm_active=False),
        "run calibration": lambda m: eye_mouse.calib_start(),
        "(righty | rickle)": right_click,
        "(dubclick | duke)": dubclick,
        "(tripclick | triplick)": tripclick,
        "drag": mouse_drag,
        # "control click": control_click,
        # "shift click": shift_click,
        #"(command click | chom lick)": command_click,
        # "(control shift click | troll shift click)": control_shift_click,
        # "(control shift double click | troll shift double click)": lambda m: control_shift_click(
            # m, 0, 2
        # ),
        #"do park": [dubclick, Key("ctrl-v")],
        #"do koosh": [dubclick, Key("ctrl-c")],
        #"wheel down": mouse_smooth_scroll(250),
        #"wheel up": mouse_smooth_scroll(-250),
        #"wheel down here": [mouse_center, mouse_smooth_scroll(250)],
        #"wheel up here": [mouse_center, mouse_smooth_scroll(-250)],
        #"mouse center": mouse_center,
    }
)

