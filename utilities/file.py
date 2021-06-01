import os
import re

def generate_readmes(directory):
    '''
    Generate READMEs.md in each directory
    '''
    for _, dirs, _ in os.walk(directory):
        unitDirs = [dir for dir in dirs if re.match(r"\d+", dir[0])]

        for dir in unitDirs:
            with open(f"{dir}/README.md", "w+") as file:
                header = dir.split("-")
                formatted_header = f"Unit {header[0]}:"
                for word in header[1:]:
                    spacedWord = re.sub(r"([A-Z]{1,2})", " \\1", word).strip()
                    formatted_header += f" {spacedWord}"

                file.write(f"# {formatted_header}\n")
                file.write(f"## TODO\n")
                file.write(f"- [ ] PreWork\n")
                file.write(f"- [ ] Session #1\n")
                file.write(f"- [ ] Session #2\n")
                file.write(f"- [ ] HackerRank\n")
                file.write(f"- [ ] Additional Exercises")

if __name__ == "__main__":
    generate_readmes(".")
