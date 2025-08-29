import gifos
import shutil
from gifos.utils.load_config import gifos_settings
from datetime import datetime
import zoneinfo

# github_stats = gifos.utils.fetch_github_stats(
#     user_name="Ethorbit"
# )

user = "ethorbit"
host = "github"
password = "**************"
prompt = f"┌──(\033[32m{user}\033[37m@\033[31m{host}\033[37m)-[~]\n└─$"
end_message = "Thanks for checking out my profile!"
zone = zoneinfo.ZoneInfo("America/Los_Angeles")

t = gifos.Terminal(width=500, height=300, xpad=5, ypad=5)
t.set_font(
    "/usr/share/fonts/truetype/FiraCodeNerdFontMono-Regular.ttf",
    13
)
t.toggle_show_cursor(False)

# systemd boot sequence
t.gen_text(
    "[  \033[32mOK\033[0m  ] Reached target github-multi-user.target",
    row_num=t.curr_row
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Started GitHub SSH Agent",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Started Repository Manager Service",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Started Git Credential Helper",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Mounted /dev/github-repos",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Started GitHub Actions Runner Daemon",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Started Pull Request Notification Service",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Started Issue Tracker Backend",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Reached target github-graphical.target",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Started GitHub Desktop Environment",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Started Terminal Session Manager",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    (
        "[  \033[33mWARN\033[0m  ] caffeine.target: "
        "failed: focus.service"
    ),
    row_num=(t.curr_row + 1)
)
t.clone_frame(5)

# tty login
t.clear_frame()
t.gen_text("GitHub README.md tty1", row_num=(t.curr_row))
t.clone_frame(10)
t.toggle_show_cursor(True)
t.gen_text(f"{host} login: ", row_num=(t.curr_row + 2))
t.clone_frame(5)
t.gen_typing_text(user, row_num=t.curr_row, speed=1, contin=True)
t.gen_text("Password: ", row_num=(t.curr_row + 1))
t.clone_frame(5)
t.gen_typing_text(password, row_num=t.curr_row, speed=1, contin=True)
t.clone_frame(5)

# home shell
t.clear_frame()
t.set_prompt(prompt)
t.gen_prompt(t.curr_row)
t.gen_typing_text(" whoami", row_num=(t.curr_row - 1), speed=2, contin=True)
t.gen_text(user, row_num=(t.curr_row + 1))
t.clone_frame(1)
t.gen_prompt(t.curr_row + 1)
t.gen_typing_text(f" echo {end_message}", row_num=(t.curr_row - 1), speed=1, contin=True)
t.gen_text(end_message, row_num=(t.curr_row + 1))
t.clone_frame(5)
t.gen_prompt(t.curr_row + 1)
t.gen_typing_text(" sudo shutdown -r now", row_num=(t.curr_row - 1), speed=2, contin=True)
t.gen_text("[sudo] password for ethorbit: ", row_num=(t.curr_row + 1))
t.clone_frame(5)
t.gen_typing_text(password, row_num=t.curr_row, speed=1, contin=True)
t.gen_text("", row_num=(t.curr_row + 1))

# systemd reboot sequence
time_now = datetime.now(tz=zone)
time_now_formatted = time_now.strftime("%a %Y-%m-%d %H:%M:%S %Z")
t.gen_text(
    (
        f"Broadcast message from {user}@{host} on pts/0"
        f"\n({time_now_formatted}):"
    ),
    row_num=(t.curr_row + 1)
)

t.gen_text("The system is going down for reboot NOW!", row_num=(t.curr_row + 1))
t.clone_frame(5)

t.gen_text(
    "[  \033[32mOK\033[0m  ] Stopping github-desktop.service...",
    row_num=(t.curr_row + 2)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Stopping github-actions-runner.service...",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Stopping pr-notification.service...",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Stopping github-webhook-dispatcher.service...",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Stopping git-lfs-daemon.service...",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Stopping github-ssh-agent.service...",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Unmounting /dev/github-repos...",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Reached target shutdown.target",
    row_num=(t.curr_row + 1)
)
t.gen_text(
    "[  \033[32mOK\033[0m  ] Reboot: System halt",
    row_num=(t.curr_row + 1)
)

t.clone_frame(5)
t.clear_frame()
t.clone_frame(5)

t.gen_gif()
# gif -> Docker volume
shutil.copy(
    (
        gifos_settings.get("files", {}).get("output_gif_name") or "output"
    ) + ".gif",
    "/output"
)
