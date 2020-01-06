from talon.voice import Key, press, Str, Context
from ..utils import parse_word, numerals, optional_numerals, text_to_number, jump_to_target, parse_words_as_integer

ctx = Context("generic_editor")

# actions and helper functions
def jump_to_bol(m):
    line = parse_words_as_integer(m)
    press("ctrl-g")
    Str(str(line))(None)
    press("enter")

def jump_to_end_of_line():
    press("end")

def jump_to_beginning_of_text():
    press("ctrl-home")

def jump_to_nearly_end_of_line():
    press("end")

def jump_to_bol_and(then):
    def fn(m):
        if len(m) > 1:
            jump_to_bol(m)
        else:
            press("ctrl-home")
            press("ctrl-left")
        then()

    return fn

def jump_to_eol_and(then):
    def fn(m):
        if len(m) > 1:
            jump_to_bol(m)
        press("end")
        then()

    return fn

def toggle_comments(*unneeded):
    press("ctrl-q")

def snipline():
    press("home")
    press("shift-end")
    press("ctrl-x")

def get_first_word(m):
    return m[0]

def jump_to(m):
    target = get_first_word(m)
    jump_to_target(target)

keymap = {
    "(trundle | comment)": toggle_comments,
    "(trundle | comment) <dgndictation>": jump_to_bol_and(toggle_comments),  # noop for plain/text
    "snipline <dgndictation>": jump_to_bol_and(snipline),
    "sprinkle <dgndictation>++ over": jump_to_bol,
    "spring <dgndictation>": jump_to_eol_and(jump_to_beginning_of_text),
    #"sprinkoon <dgndictation>": jump_to_eol_and(lambda: press("enter")),
    "dear <dgndictation>++ over": jump_to_eol_and(lambda: None),
    "smear <dgndictation>++ over": jump_to_eol_and(jump_to_nearly_end_of_line),
    # general
    # file
    "new": Key("ctrl-n"),
    "(save | safe)": Key("ctrl-s"),
    "close (file | tab)": Key("ctrl-w"),
    # selection
    # "(select | cell) up": Key("shift-up"),
    # "(select | cell) down": Key("shift-down"),
    # "(select | cell) all": Key("cmd-a"),
    # "(select | cell) bottom ": Key("cmd-shift-down"),
    # "(select | cell) right": Key("shift-right"),
    # "(select | cell) left": Key("shift-left"),
    # "(select | cell) word": Key("shift-alt-left"),
    # "(select | cell) (end | push)": Key("cmd-shift-right"),
    # "(select | cell) (start | begin | pop)": Key("cmd-shift-left"),
    # edit
    #"paste match": Key("cmd-shift-v"),
    #"shove": Key("cmd-]"),
    #"tug": Key("cmd-["),
    "(scrap | scratch | delete) word": Key("ctrl-backspace"),
    "(scrap | scratch | delete) (begin | start)": Key("ctrl-shift-l"),
    # navigation
    #"push": Key("cmd-right"),
    #"pop": Key("cmd-left"),
    #"step": Key("alt-right"),
    #"stone": Key("alt-left"),
    "jump to <dgndictation>": jump_to,
}

ctx.keymap(keymap)
