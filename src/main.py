import config
import logins
import sequences
import gifos
import shutil
from gifos.utils.load_config import gifos_settings

# github_stats = gifos.utils.fetch_github_stats(
#     user_name="Ethorbit"
# )


t = gifos.Terminal(width=500, height=300, xpad=5, ypad=5)
t.set_font(
    config.TERMINAL_FONT_PATH,
    config.TERMINAL_FONT_SIZE
)
t.toggle_show_cursor(False)
sequences.boot(t)
t.clone_frame(config.TYPING_DELAY)
logins.tty(t)
t.set_prompt(config.PROMPT)
t.gen_prompt(t.curr_row)
t.gen_typing_text(" whoami", row_num=(t.curr_row - 1), speed=2, contin=True)
t.gen_text(config.USER, row_num=(t.curr_row + 1))
t.clone_frame(1)
t.gen_prompt(t.curr_row + 1)
t.gen_typing_text(
    f" echo {config.END_MESSAGE}", row_num=(t.curr_row - 1), speed=1, contin=True
)
t.gen_text(config.END_MESSAGE, row_num=(t.curr_row + 1))
t.gen_prompt(t.curr_row + 1)
t.clone_frame(config.TYPING_DELAY)
t.gen_typing_text(
    " sudo shutdown -r now", row_num=(t.curr_row - 1), speed=2, contin=True
)
logins.sudo(t)
t.gen_text("", row_num=(t.curr_row + 1))
sequences.reboot(t)

t.gen_gif()
# gif -> Docker volume
shutil.copy(
    (
        gifos_settings.get("files", {}).get("output_gif_name") or "output"
    ) + ".gif",
    "/output"
)
