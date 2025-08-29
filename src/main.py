import config
import terminal
import logins
import sequences
import commands
import shutil
import gifos
from gifos.utils.load_config import gifos_settings

t = terminal.create()

sequences.boot(t)
t.clone_frame(config.TYPING_DELAY)
logins.tty(t)

# commands.whoami(t)
t.gen_prompt(1)
commands.ghfetch(t)
commands.clear(t)
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
