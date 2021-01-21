import re

FORMAT = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

def check_line(line):
    min_val, max_val, char, password = re.match(FORMAT, line).groups()

    occ = password.count(char)
    return int(min_val) <= occ <= int(max_val)


def main():
    with open('./input') as input_file:
        data = input_file.readlines()
        print(len(list(filter(check_line, data))))

if __name__ == '__main__':
    main()