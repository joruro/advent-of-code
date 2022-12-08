import os

BASE_LINK = "https://github.com/joruro/advent-of-code/blob/main/src/years/"


def parse(e, base_path=""):
    name = e.replace(".py", "")
    # name = " ".join(name.split("_")[1:])
    return f"[{name}]({BASE_LINK}{base_path}{e})"


years = os.listdir("src/years")
content = []
for year in years:
    content.append(f"* {parse(year)}")
    solutions = filter(lambda x: ".py" in x and "init" not in x,
                       os.listdir(f"src/years/{year}"))
    content += [f"    *{parse(f'{solution}', f'{year}/')}" for _,
                solution in enumerate(sorted(solutions))]

readme_content = "# Advent of Code\n\n"
readme_content += "## Usage\n\n## Problems list:\n"
readme_content += "\n".join(content)

with open("README.md", "w") as f:
    f.write(
        readme_content
        + "\n\nInspired by: [advent-of-code-setup](https://github.com/tomfran/advent-of-code-setup)"
    )
