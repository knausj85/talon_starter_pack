# From https://github.com/talonvoice/examples
from talon_plugins import eye_mouse, eye_zoom_mouse
from talon.voice import Context
ctx = Context("eye_control")

def toggle_zoom_mouse(m):
    if eye_zoom_mouse.zoom_mouse.enabled:
        try:
            eye_zoom_mouse.zoom_mouse.disable()
        except:
            eye_zoom_mouse.zoom_mouse.enabled = False
    else:
        eye_zoom_mouse.zoom_mouse.enable()
        
ctx.keymap(
    {
        "debug overlay": lambda m: eye_mouse.debug_overlay.toggle(),
        "control mouse": lambda m: eye_mouse.control_mouse.toggle(),
        "zoom mouse": toggle_zoom_mouse,
        "camera overlay": lambda m: eye_mouse.camera_overlay.toggle(),
        "run calibration": lambda m: eye_mouse.calib_start(),
    }
)

