import sys
import re


def main():
    if len(sys.argv) != 2:
        print("Usage: [program] [input.txt]")
        return
    with open(sys.argv[1], "r") as file:
        result = []
        input = file.read()
        matches = re.findall(r"mul\(\d+\,\d+\)", input)
        for match in matches:
            mul = [int(re.findall(r"\d+", n)[0]) for n in match.split(",")]
            result.append(mul[0] * mul[1])
        print(sum(result))


if __name__ == "__main__":
    main()
