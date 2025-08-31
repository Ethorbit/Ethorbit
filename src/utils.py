import random
from ascii_magic import AsciiArt


def random_color_code():
    return random.randint(31, 36)


def fetch_github_avatar_ascii(user_name: str):
    try:
        avatar_url = f"https://github.com/{user_name}.png?size=40"
        avatar_ascii = AsciiArt.from_url(avatar_url)
        # avatar_img = Image.open(requests.get(avatar_url, stream=True).raw)
    except OSError as e:
        print(f'''
        An unexpected error occurred when fetching the avatar
        for the Github user: ${user_name}

        Server said: {e}
        ''')
    finally:
        return avatar_ascii.to_ascii(columns=25)
