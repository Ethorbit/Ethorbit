import gifos
import shutil
from gifos.utils.load_config import gifos_settings

# github_stats = gifos.utils.fetch_github_stats(
#     user_name="Ethorbit"
# )

user = "Ethorbit"
host = "github.com"
prompt = f"┌──(\033[32m{user}\033[37m@\033[31m{host}\033[37m)-[~]\n└─$"

t = gifos.Terminal(width=500, height=300, xpad=5, ypad=5)
t.set_font(
    "/usr/share/fonts/truetype/FiraCodeNerdFontMono-Regular.ttf",
    13
)
t.set_prompt(prompt)
t.gen_prompt(1)
t.gen_text("", row_num=1)
t.gen_typing_text(" whoami", row_num=2, speed=2, contin=True)
t.set_txt_color("green")
t.gen_text(user, row_num=3)
t.set_txt_color("white")
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
