import re

FORMAT = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


def check_line(line):
    first_index, sec_index, char, password = re.match(FORMAT, line).groups()
    return (password[int(first_index) - 1] == char) ^ (password[int(sec_index) - 1] == char)


def main():
    with open('./input') as input_file:
        data = input_file.readlines()
        print(len(list(filter(check_line, data))))


if __name__ == '__main__':
    main()
