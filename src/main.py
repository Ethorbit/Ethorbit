import config
import terminal
import logins
import sequences
import commands
import shutil
import gifos
from gifos.utils.load_config import gifos_settings

try:
    gh_stats = gifos.utils.fetch_github_stats(
        user_name=config.USER
    )

finally:
    t = terminal.create()
    sequences.boot(t)
    t.clone_frame(config.TYPING_DELAY)
    logins.tty(t)
    t.gen_prompt(1)
    t.clone_frame(5)
    commands.whoami(t)
    t.clone_frame(5)
    commands.ghfetch(t, gh_stats)
    t.clone_frame(20)
    # commands.clear(t)
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
