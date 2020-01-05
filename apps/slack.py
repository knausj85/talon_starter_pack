from talon.voice import Context, Key
from ..utils import text

ctx = Context("slack",exe='C:\\Users\\knausj\\AppData\\Local\\slack\\app-4.2.0\\slack.exe')

keymap = {
    # Channel
    "channel": Key("ctrl-k"),
    "channel <dgndictation>": [Key("ctrl-k"), text],
    "([channel] unread last | gopreev)": Key("alt-shift-up"),
    "([channel] unread next | goneck)": Key("alt-shift-down"),
    "(slack | lack) [channel] info": Key("ctrl-shift-i"),
    "channel up": Key("alt-up"),
    "channel down": Key("alt-down"),
    # Navigation
    "(move | next) focus": Key("ctrl-`"),
    "[next] (section | zone)": Key("f6"),
    "(previous | last) (section | zone)": Key("shift-f6"),
    "(slack | lack) [direct] messages": Key("ctrl-shift-k"),
    "(slack | lack) threads": Key("ctrl-shift-t"),
    "(slack | lack) (history [next] | back | backward)": Key("alt-left"),
    "(slack | lack) forward": Key("alt-right"),
    "[next] (element | bit)": Key("tab"),
    "(previous | last) (element | bit)": Key("shift-tab"),
    "(slack | lack) (my stuff | activity)": Key("ctrl-shift-m"),
    "(slack | lack) directory": Key("ctrl-shift-e"),
    "(slack | lack) (starred [items] | stars)": Key("ctrl-shift-s"),
    "(slack | lack) unread [messages]": Key("ctrl-j"),
    #"(go | undo | toggle) full": Key("ctrl-cmd-f"),
    "(slack | lack) (find | search)": Key("ctrl-f"),
    # Messaging
    "grab left": Key("shift-up"),
    "grab right": Key("shift-down"),
    "add line": Key("shift-enter"),
    #"(slack | lack) (slap | slaw | slapper)": [Key("cmd-right"), Key("shift-enter")],
    "(slack | lack) (react | reaction)": Key("ctrl-shift-\\"),
    "(insert command | commandify)": Key("ctrl-shift-c"),
    "insert code": [
        "``````",
        Key("left left left"),
        Key("shift-enter"),
        Key("shift-enter"),
        Key("up"),
    ],
    "(slack | lack) (bull | bullet | bulleted) [list]": Key("ctrl-shift-8"),
    "(slack | lack) (number | numbered) [list]": Key("ctrl-shift-7"),
    "(slack | lack) (quotes | quotation)": Key("ctrl-shift-9"),
    "bold": Key("ctrl-b"),
    "(italic | italicize)": Key("ctrl-i"),
    "(strike | strikethrough)": Key("ctrl-shift-x"),
    "mark all read": Key("shift-esc"),
    "mark channel read": Key("esc"),
    "(clear | scrap | scratch)": Key("ctrl-a backspace"),
    # Files and Snippets
    "(slack | lack) upload": Key("ctrl-u"),
    "(slack | lack) snippet": Key("ctrl-shift-enter"),
    # Calls
    "([toggle] mute | unmute)": Key("m"),
    "(slack | lack) ([toggle] video)": Key("v"),
    "(slack | lack) invite": Key("a"),
    # Miscellaneous
    "(slack | lack) shortcuts": Key("ctrl-/"),
}

ctx.keymap(keymap)
