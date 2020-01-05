from talon.voice import Context, Key
from ..utils import is_filetype

FILETYPES = (".cs")

context = Context("csharp", func=is_filetype(FILETYPES))

context.keymap(
    {
        #"empty dict": "{}",
        #"word (dickt | dictionary)": "dict",
        #"state (def | deaf | deft)": "def ",
        "state else if": ["else if ()", Key("left")],
        "state if": "if ",
        "state while": ["while ()", Key("left")],
        "state for": "for ",
        "state for each": "for each ",
        "state switch": ["switch ()", Key("left")],
        "state case": ["case ()\n{\n}\nbreak;", Key("up"), Key("up")],
        # "state goto": "goto ",
        # "state import": "import ",
        # "state class": "class ",
        # "state include": "#include ",
        # "state include system": ["#include <>", Key("left")],
        # "state include local": ['#include ""', Key("left")],
        # "state type deaf": "typedef ",
        # "state type deaf struct": ["typedef struct {\n\n};", Key("up"), "\t"],
        # "comment py": "# ",
        # "dunder in it": "__init__",
        # "self taught": "self.",
        # "from import": ["from import ", Key("alt-left"), Key("space"), Key("left")],
        # "for in": ["for in ", Key("alt-left"), Key("space"), Key("left")],
    }
)
