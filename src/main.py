import config
import terminal
import logins
import sequences
import commands
import shutil
import gifos
from gifos.utils.load_config import gifos_settings

gh_stats = gifos.utils.fetch_github_stats(
    user_name=config.USER
)

if gh_stats is None:
    raise TypeError(f'''
    gh_stats is None.
    Is {config.USER} a valid Github user?
    ''')

t = terminal.create()
sequences.boot(t)
t.clone_frame(config.TYPING_DELAY)
logins.tty(t)
t.gen_prompt(t.curr_row + 1)
t.clone_frame(config.TYPING_DELAY)
commands.whoami(t)
t.clone_frame(config.TYPING_DELAY)
commands.ghfetch(t, gh_stats)
t.clone_frame(20)
t.clone_frame(config.TYPING_DELAY)
commands.cowsay(t, config.END_MESSAGE)
t.clone_frame(15)
commands.reboot(t)

t.gen_gif()
# gif -> Docker volume
shutil.copy(
    (
        gifos_settings.get("files", {}).get("output_gif_name") or "output"
    ) + ".gif",
    "/output"
)
