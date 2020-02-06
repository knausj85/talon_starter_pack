from talon.voice import Context, Key
from ..utils import text

ctx = Context("notepad++",exe="C:\\Program Files (x86)\\Notepad++\\notepad++.exe")

keymap = {
    "close tab": Key("ctrl-w"),
    "previous tab": Key("ctrl-pagedown"),
    "switch tab": Key("ctrl-tab"),
    "next tab": Key("ctrl-pageup"),
    "open": Key("ctrl-o"),
    "refresh": Key("ctrl-r"),
}

ctx.keymap(keymap)
