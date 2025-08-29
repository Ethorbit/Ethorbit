import config


def tty(t):
    t.toggle_show_cursor(False)
    t.clear_frame()
    t.gen_text("GitHub README.md tty1", row_num=(t.curr_row))
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_text(f"{config.HOST} login: ", row_num=(t.curr_row + 2))
    t.clone_frame(config.TYPING_DELAY)
    t.gen_typing_text(config.USER, row_num=t.curr_row, speed=1, contin=True)
    t.gen_text("Password: ", row_num=(t.curr_row + 1))
    t.clone_frame(config.TYPING_DELAY)
    t.gen_typing_text(
        config.PASSWORD, row_num=t.curr_row, speed=1, contin=True
    )
    t.clone_frame(5)
    t.clear_frame()


def sudo(t):
    t.gen_text(
        f"[sudo] password for {config.USER}: ", row_num=(t.curr_row + 1)
    )
    t.clone_frame(config.TYPING_DELAY)
    t.gen_typing_text(
        config.PASSWORD, row_num=t.curr_row, speed=1, contin=True
    )
