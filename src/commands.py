import config
import logins
import sequences


def whoami(t):
    t.gen_prompt(t.curr_row)
    t.gen_typing_text(" whoami", row_num=(t.curr_row - 1), speed=2, contin=True)
    t.gen_text(config.USER, row_num=(t.curr_row + 1))
    t.clone_frame(1)


def echo(t, message):
    t.gen_prompt(t.curr_row + 1)
    t.gen_typing_text(
        f" echo {config.END_MESSAGE}", row_num=(t.curr_row - 1), speed=1, contin=True
    )
    t.gen_text(config.END_MESSAGE, row_num=(t.curr_row + 1))


def reboot(t):
    t.gen_prompt(t.curr_row + 1)
    t.clone_frame(config.TYPING_DELAY)
    t.gen_typing_text(
        " sudo shutdown -r now", row_num=(t.curr_row - 1), speed=2, contin=True
    )
    logins.sudo(t)
    t.gen_text("", row_num=(t.curr_row + 1))
    sequences.reboot(t)
