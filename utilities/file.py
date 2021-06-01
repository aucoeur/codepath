import os
import re

def generate_readmes(directory):
    '''
    Generate READMEs.md in each directory with basic headers but janky
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

                # i know this is janky ok
                file.write(f"# {formatted_header}\n")
                file.write(f"\n## TODO\n")
                file.write(f"- [ ] [PreWork](#PreWork)\n")
                file.write(f"- [ ] [Session #1](#Session-1)\n")
                file.write(f"- [ ] [Session #2](#Session-2)\n")
                file.write(f"- [ ] HackerRank\n")
                file.write(f"- [ ] [Additional Exercises](#Additional-Exercises)\n")
                file.write(f"\n## PreWork\n")
                file.write(f"\n## Session #1\n")
                file.write(f"## Session #2\n")
                file.write(f"\n## Additional Exercises\n")







if __name__ == "__main__":
    generate_readmes(".")
