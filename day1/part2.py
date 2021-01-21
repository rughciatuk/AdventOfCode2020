def main():
    with open("./input") as input_file:
        numbers = list(map(int, input_file.readlines()))
        for first in range(len(numbers)):
            for sec in range(first + 1, len(numbers)):
                for third in range(sec + 1, len(numbers)):
                    if numbers[first] + numbers[sec] + numbers[third] == 2020:
                        print(numbers[first] * numbers[sec]* numbers[third])


if __name__ == '__main__':
    main()
