import gifos
import shutil
from gifos.utils.load_config import gifos_settings

# github_stats = gifos.utils.fetch_github_stats(
#     user_name="Ethorbit"
# )

user = "ethorbit"
host = "github"
prompt = f"┌──(\033[32m{user}\033[37m@\033[31m{host}\033[37m)-[~]\n└─$"

t = gifos.Terminal(width=500, height=300, xpad=5, ypad=5)
t.set_font(
    "/usr/share/fonts/truetype/FiraCodeNerdFontMono-Regular.ttf",
    13
)
t.toggle_show_cursor(False)
t.gen_text(f"GitHub README.md tty1", row_num=1)
t.gen_text("", row_num=2)
t.clone_frame(5)
t.toggle_show_cursor(True)
t.gen_text(f"{host} login: ", row_num=3)
t.clone_frame(5)
t.gen_typing_text(user, row_num=3, speed=1, contin=True)
t.gen_text("Password: ", row_num=4)
t.clone_frame(5)
t.gen_typing_text("**************", row_num=4, speed=1, contin=True)
t.clone_frame(5)
t.gen_text("", row_num=1)
t.gen_text("", row_num=2)
t.gen_text("", row_num=3)
t.gen_text("", row_num=4)
t.gen_text("", row_num=5)
t.set_prompt(prompt)
t.gen_prompt(1)
t.gen_typing_text(" whoami", row_num=2, speed=2, contin=True)
t.gen_text(user, row_num=3)
t.gen_prompt(4)
t.clone_frame(30)
t.gen_gif()

# gif -> Docker volume
shutil.copy(
    (
        gifos_settings.get("files", {}).get("output_gif_name") or "output"
    ) + ".gif",
    "/output"
)
