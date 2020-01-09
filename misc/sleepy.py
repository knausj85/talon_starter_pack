from talon.voice import Context, ContextGroup
from talon.engine import engine
from talon_plugins import speech, eye_mouse, eye_zoom_mouse

sleep_group = ContextGroup("sleepy")
sleepy = Context("sleepy", group=sleep_group)

def wake_or_sleep(wake_up):
    if wake_up:
        eye_zoom_mouse.zoom_mouse.enable()
        eye_mouse.control_mouse.enable() 
    else:
        eye_zoom_mouse.zoom_mouse.disable()
        eye_mouse.control_mouse.disable()
        engine.mimic("go to sleep".split())

sleepy.keymap( 
    {
        "talon sleep": lambda m: speech.set_enabled(False),
        "talon wake": lambda m: speech.set_enabled(True),
        "dragon mode": [
            lambda m: speech.set_enabled(False),
            lambda m: engine.mimic("wake up".split()),
        ],
        "talon mode": [
            lambda m: speech.set_enabled(True),
            lambda m: engine.mimic("go to sleep".split()),
        ],
        "sleep all" : lambda m: wake_or_sleep(False),
        "welcome back": lambda m: wake_or_sleep(True),
    }
)

sleep_group.load()
