import config
import terminal
import logins
import sequences
import commands
import shutil
import gifos
from gifos.utils.load_config import gifos_settings

# github_stats = gifos.utils.fetch_github_stats(
#     user_name="Ethorbit"
# )

t = terminal.create()
t.toggle_show_cursor(False)
sequences.boot(t)
t.clone_frame(config.TYPING_DELAY)
logins.tty(t)

# Logged in, time to enter commands
commands.whoami(t)
commands.echo(t, config.END_MESSAGE)
commands.reboot(t)

t.gen_gif()
# gif -> Docker volume
shutil.copy(
    (
        gifos_settings.get("files", {}).get("output_gif_name") or "output"
    ) + ".gif",
    "/output"
)
