import re


def check_fields(pairs):
    if int(pairs['byr']) < 1920 or int(pairs['byr']) > 2002:
        return False
    if int(pairs['iyr']) < 2010 or int(pairs['iyr']) > 2020:
        return False
    if int(pairs['eyr']) < 2020 or int(pairs['eyr']) > 2030:
        return False

    height_match = re.match("(\d+)(cm|in)", pairs['hgt'])
    if height_match:
        if height_match.group(2) == 'cm':
            if int(height_match.group(1)) < 150 or int(height_match.group(1)) > 193:
                return False
        else:
            if int(height_match.group(1)) < 59 or int(height_match.group(1)) > 76:
                return False
    else:
        return False

    if not re.match(r"^#[0-9a-f]{6}$", pairs['hcl']):
        return False

    if not (pairs['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False

    if not re.match(r"^[0-9]{9}$", pairs['pid']):
        return False

    return True


def main():
    with open('/home/rbs/projects/advent-of-code-2020/day4/input') as input_file:
        data = input_file.read().split('\n\n')
        count = 0
        for passport in data:
            pairs = re.split(r"\s", passport)

            if (len(pairs) == 8) or (len(pairs) == 7 and len(list(filter(lambda item: 'cid' in item, pairs))) == 0):
                count += check_fields(dict(map(lambda pair: tuple(pair.split(":")), pairs)))

        print("count:", count)


if __name__ == '__main__':
    main()
