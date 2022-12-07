import os
import sys
import datetime

# Create folder years
os.makedirs("src/years", exist_ok=True)

# Find year
if len(sys.argv) == 2:
    year = sys.argv[1]
    print(year)
else:
    years = os.listdir("src/years")
    if len(years) == 0:
        year = datetime.datetime.now().year
    else:
        year = int(sorted(years)[-1])
# Create folder for year
os.makedirs(f"src/years/{year}", exist_ok=True)

# Find day
days = list(filter(lambda x: "__" not in x and ".py" in x,
            os.listdir(f"src/years/{year}")))
day = int(sorted(days)[-1][:2]) + 1 if len(days) > 0 else 1
DEFAULT_FILE = "\n".join([
    "import sys",
    "import os",
    'sys.path.insert(0, os.path.abspath("src"))',
    "from utils.api import get_input  # noqa: E402\n",
    f"input = get_input({year}, {day})\n",
    "# WRITE YOUR SOLUTION HERE\n\n"
])

path = f"src/years/{year}/{day:02d}.py"
with open(path, "w") as f:
    f.write(DEFAULT_FILE)

print(f"Enter your solution in {path}")
