import config
import gifos
from gifos.utils.load_config import gifos_settings


def create():
    t = gifos.Terminal(
        width=config.TERMINAL_WIDTH,
        height=config.TERMINAL_HEIGHT,
        xpad=5,
        ypad=5
    )
    t.set_font(
        config.TERMINAL_FONT_PATH,
        config.TERMINAL_FONT_SIZE
    )
    t.set_prompt(config.PROMPT)
    return t
