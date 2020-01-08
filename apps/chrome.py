from talon.voice import Context, Key

context = Context("GoogleChrome", exe="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

keymap = {
    "(address bar | go address | go url)": Key("ctrl-l"),
    "go back[ward]": Key("alt-left"),
    "forward": Key("alt-right"),
    "close [tab]": Key("ctrl-w"),
    "chrome (find | marco)": Key("ctrl-f"),
    "dev tools": Key("ctrl-alt-i"),
    # navigating current page
    "help": Key("?"),
    "scroll tiny down": Key("j"),
    "scroll tiny up": Key("k"),
    "scroll left": Key("h"),
    "scroll right": Key("l"),
    "scroll (pop | spring)": Key("z H"),
    "scroll push": Key("z L"),
    "scroll top": Key("gg"),
    "scroll (bottom | end)": Key("G"),
    "(scroll half down | mini page)": Key("d"),
    "scroll half up": Key("u"),
    "[open] link": Key("f"),
    "[open] link new": Key("F"),
    "copy link": Key("y f"),
    "copy (address | url)": Key("escape y y"),
    "(refresh | reload)": Key("ctrl-r"),
    "view source": Key("g s"),
    "insert mode": Key("i"),
    "next frame": Key("g f"),
    "main frame": Key("g F"),
    # navigating to new pages
    "(open | go) (url | history)": Key("o"),
    "(open | go) (url | history) new": Key("O"),
    "(open | go) bookmark": Key("b"),
    "(open | go) bookmark new": Key("B"),
    # using find
    "find mode": Key("/"),
    "next match": Key("n"),
    "previous match": Key("N"),
    # navigating history
    "history back": Key("H"),
    "history forward": Key("L"),
    # manipulating tabs
    "last visited": Key("^"),
    "dupe tab": Key("y t"),
    "restore": Key("X"),
    "search tabs": Key("T"),
    "move to window": Key("W"),
}

context.keymap(keymap)
