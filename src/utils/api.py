import requests
import os

def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()


def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"


SESSION_ID_FILE = "session.cookie"
SESSION = get_session_id(SESSION_ID_FILE)
HEADERS = {
    "User-Agent": "github.com/joruro/advent-of-code"
}
COOKIES = {"session": SESSION}


def get_input(year, day):
    inputs_dir = f"inputs/{year}"
    # Create folder for year
    os.makedirs(inputs_dir, exist_ok=True)

    path = f"{inputs_dir}/{day:02d}"

    if not os.path.exists(path):
        url = get_url(year, day)
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(path, "w") as f:
            f.write(response.text[:-1])

    with open(path, "r") as f:
        return f.read()
