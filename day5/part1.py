
def get_seat_index(line):
    row_info = line[0:7]
    col_info = line[7:]

    low_row_index = 0
    high_row_index = 127
    low_col_index = 0
    high_col_index = 7

    for letter in row_info:
        if letter == 'F':
            high_row_index = high_row_index - ((high_row_index+1)-low_row_index)//2
        elif letter == 'B':
            low_row_index = low_row_index + ((high_row_index+1)-low_row_index)//2

    for letter in col_info:
        if letter == 'L':
            high_col_index = high_col_index - ((high_col_index+1)-low_col_index)//2
        elif letter == 'R':
            low_col_index = low_col_index + ((high_col_index+1)-low_col_index)//2

    return high_row_index * 8 + high_col_index

def main():
    with open('./input') as input_file:
        data = input_file.read().split('\n')[:-1]
        seats_numbers = []
        for line in data:
            seats_numbers.append(get_seat_index(line))
        print(max(seats_numbers))

if __name__ == '__main__':
    main()
