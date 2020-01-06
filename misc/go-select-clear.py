from talon.voice import Context, Key
from os import system

ctx = Context('go-select-clear')

direction = 'right'
def set_dir(d):
    def wrapper(m):
        global direction
        direction = d
    return wrapper

ctx.keymap({
    # moving

    # left, right, up and down already defined
    'go word left': Key('ctrl-a'),
    'go word right': Key('ctrl-right'),

    'go left': Key('left'),
    'go right': Key('right'),
    'go up': Key('up'),
    'go down': Key('down'),

    'go line start': Key('home'),
    'go line end': Key('end'),

    'go way left': Key('home'),
    'go way right': Key('end'),
    'go way down': Key('ctrl-end'),
    'go way up': Key('ctrl-home'),

    # selecting
    'select line': Key('home shift-end'),

    'select left': Key('shift-left'),
    'select right': Key('shift-right'),
    'select up': Key('shift-up'),
    'select down': Key('shift-down'),

    #'select word left': [Key('left shift-right left alt-left alt-right shift-alt-left'), set_dir('left')],
    #'select word right': [Key('right shift-left right alt-right alt-left shift-alt-right'), set_dir('right')],

    #'extend': lambda m: Key(f'ctrl-{direction}')(m),

    'select way left': Key('shift-home'),
    'select way right': Key('shift-end'),
    'select way up': Key('shift-ctrl-home'),
    'select way down': Key('shift-ctrl-end'),

    # deleting
    'clear line': Key('home shift-end delete'),
    
    'clear left': Key('backspace'),
    'clear right': Key('delete'),
    'clear up':  Key('shift-up delete'),
    'clear down':  Key('shift-down delete'),

    #'clear word left': Key('alt-backspace'),
    #'clear word right': Key('alt-delete'),

    'clear way left': Key('shift-home delete'),
    'clear way right': Key('shift-end delete'),
    'clear way up': Key('ctrl-shift-home delete'),
    'clear way down': Key('ctrl-shift-end delete'),
})
