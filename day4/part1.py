import re


def main():
    with open('./input') as input_file:
        data = input_file.read().split('\n\n')
        count = 0
        for passport in data:
            pairs = re.split(r"\s", passport)
            if len(pairs) == 8:
                count += 1
            elif len(pairs) == 7 and len(list(filter(lambda item: 'cid' in item, pairs))) == 0:
                count += 1
        print(count)


if __name__ == '__main__':
    main()
