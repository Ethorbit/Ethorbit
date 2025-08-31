import utils
import config
import logins
import sequences
import gifos
import random

def clear(t):
    t.gen_typing_text(
        " clear",
        row_num=(t.curr_row - 1),
        speed=2,
        contin=True
    )
    t.clear_frame()
    t.gen_prompt(t.curr_row + 1)


def whoami(t):
    t.gen_typing_text(
        " whoami",
        row_num=(t.curr_row - 1),
        speed=2,
        contin=True
    )
    t.gen_text(config.USER, row_num=(t.curr_row + 1))
    t.gen_prompt(t.curr_row + 1)


def echo(t, message):
    t.gen_typing_text(
        f" echo {message}",
        row_num=(t.curr_row - 1),
        speed=1,
        contin=True
    )
    t.gen_text(message, row_num=(t.curr_row + 1))
    t.gen_prompt(t.curr_row + 1)


def cowsay(t, message):
    t.gen_typing_text(
        f" cowsay {message}",
        row_num=(t.curr_row - 1),
        speed=1,
        contin=True
    )
    num_lines = len(message) + 5
    line = ("_" * num_lines)
    t.gen_text(line, row_num=(t.curr_row + 1))
    t.gen_text("< " + message + " >", row_num=(t.curr_row + 1))
    t.gen_text(line, row_num=(t.curr_row + 1))
    t.gen_text(
        r"""
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\
                ||----w |
                ||     ||
        """,
        row_num=(t.curr_row + 1)
    )

    t.gen_prompt(t.curr_row + 1)


def ghfetch(t, gh_stats):
    gh_avatar_ascii = utils.fetch_github_avatar_ascii(
        user_name=config.USER
    )

    t.gen_typing_text(
        f" ghfetch -u {config.USER} -c green",
        row_num=(t.curr_row - 1),
        speed=1,
        contin=True
    )

    t.gen_text(
        gh_avatar_ascii,
        row_num=(t.curr_row + 1),
        col_num=1
    )

    t.set_txt_color("green")
    col = 28
    t.cursor_to_box(row_num=3, col_num=1, contin=True)
    t.gen_text(
        f"User: {config.USER}",
        row_num=t.curr_row + 2,
        col_num=col,
        contin=True)
    t.gen_text(
        "--------------",
        row_num=(t.curr_row + 1),
        col_num=col,
        contin=True
    )
    t.gen_text(
        f"Rating: {gh_stats.user_rank.level}",
        row_num=(t.curr_row + 1),
        col_num=col,
        contin=True
    )
    t.gen_text(
        f"Followers: {gh_stats.total_followers}",
        row_num=(t.curr_row + 1),
        col_num=col,
        contin=True
    )
    t.gen_text(
        f"Total Stars Earned: {gh_stats.total_stargazers}",
        row_num=(t.curr_row + 1),
        col_num=col,
        contin=True
    )
    t.gen_text(
        f"Total Commit Last Year: {gh_stats.total_commits_last_year}",
        row_num=(t.curr_row + 1),
        col_num=col,
        contin=True
    )
    t.gen_text(
        f"Total PRs: {gh_stats.total_pull_requests_made}",
        row_num=(t.curr_row + 1),
        col_num=col,
        contin=True
    )
    t.gen_text(
        f"Total Issues: {gh_stats.total_issues}",
        row_num=(t.curr_row + 1),
        col_num=col,
        contin=True
    )

    t.set_txt_color()
    t.gen_prompt(t.curr_row + 6)


def listlanguages(t, gh_stats):
    t.gen_typing_text(
        " head -n 6 /proc/languages | color.sh",
        row_num=(t.curr_row - 1),
        speed=1,
        contin=True
    )

    for language, percent in gh_stats.languages_sorted:
        row = t.curr_row + 1
        color = f"\x1b[{utils.random_color_code()}m"
        t.cursor_to_box(row_num=row, col_num=1)

        t.gen_text(
            f"{color}· {language}\x1b[0m",
            row_num=row,
            contin=True
        )

        t.gen_text(
            f"{color}{percent}%\x1b[0m",
            row_num=row,
            col_num=20,
            contin=True
        )

    t.gen_prompt(t.curr_row + 1)


def reboot(t):
    t.gen_typing_text(
        " sudo shutdown -r now", row_num=(t.curr_row - 1), speed=2, contin=True
    )
    logins.sudo(t)
    t.gen_text("", row_num=(t.curr_row + 1))
    sequences.reboot(t)
    t.gen_prompt(t.curr_row + 1)
