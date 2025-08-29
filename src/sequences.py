import config
from datetime import datetime


def boot(t):
    t.toggle_show_cursor(False)
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
    t.toggle_show_cursor(True)


def reboot(t):
    t.toggle_show_cursor(False)
    time_now = datetime.now(tz=config.ZONE)
    time_now_formatted = time_now.strftime("%a %Y-%m-%d %H:%M:%S %Z")
    t.gen_text(
        (
            f"Broadcast message from {config.USER}@{config.HOST} on pts/0"
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
    # Blank: rebooting
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(True)
