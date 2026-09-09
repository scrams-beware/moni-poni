# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: RecipeCost
import sys

class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    
    COLORS = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
    }
    
    BG_COLORS = {
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m',
    }

_color_enabled = True

def enable_colors():
    global _color_enabled
    _color_enabled = True

def disable_colors():
    global _color_enabled
    _color_enabled = False

def colorize(text, color, bg=None):
    if not _color_enabled:
        return str(text)
    if bg:
        return f'{Color.COLORS.get(color, "")}{Color.BG_COLORS.get(bg, "")}{text}{Color.RESET}'
    return f'{Color.COLORS.get(color, "")}{text}{Color.RESET}'

def bold(text):
    if not _color_enabled:
        return str(text)
    return f'{Color.BOLD}{text}{Color.RESET}'

def dim(text):
    if not _color_enabled:
        return str(text)
    return f'{Color.DIM}{text}{Color.RESET}'

def underline(text):
    if not _color_enabled:
        return str(text)
    return f'{Color.UNDERLINE}{text}{Color.RESET}'
