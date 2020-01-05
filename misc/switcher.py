from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ui
import re

apps = {}
overrides = {}

def split_camel(word):
    return re.findall(r'[0-9A-Z]*[a-z]+(?=[A-Z]|$)', word)


def get_words(name):
    words = re.findall(r'[0-9A-Za-z]+', name)
    out = []
    for word in words:
        out += split_camel(word)
    return out


def switch_app(m):
    name = str(m[1])

    full = apps.get(name)
    if not full:
        return
    for app in ui.apps():
        if app.name == full and not app.background:
            app.focus()
            break


ctx = Context("switcher")
keymap = {"(focus | folk) {switcher.apps}": switch_app}
ctx.keymap(keymap)


def update_lists():
    global apps
    new = {}
    for app in ui.apps(background=False):
        name = app.name
        if name.endswith('.exe'):
            name = name.rsplit('.', 1)[0]
        words = get_words(name)
        for word in words:
            if word and not word in new:
                new[word] = app.name
        new[name] = app.name
    for override in overrides:
        new[override] = overrides[override]
    if set(new.keys()) == set(apps.keys()):
        return
    ctx.set_list("apps", new.keys())
    apps = new


def ui_event(event, arg):
    if event in ("app_activate", "app_deactivate", "app_launch", "app_close"):
        update_lists()


ui.register("", ui_event)
update_lists()
