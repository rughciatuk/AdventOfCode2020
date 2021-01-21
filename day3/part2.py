TREE = '#'
EMPTY = '.'


def check_slop(col_offset, row_offset, rows):
    length = len(rows[0])
    height = len(rows)
    col_index = (0 + col_offset) % length
    row_index = 0 + row_offset
    tree_count = 0

    while row_index < height:
        if rows[row_index][col_index] == TREE:
            tree_count += 1
        row_index += row_offset
        col_index = (col_index + col_offset) % length
    return tree_count


def main():
    with open('./input') as input_file:
        rows = list(map(str.strip, input_file.readlines()))

        print(check_slop(1, 1, rows) *
              check_slop(3, 1, rows) *
              check_slop(5, 1, rows) *
              check_slop(7, 1, rows) *
              check_slop(1, 2, rows))


if __name__ == '__main__':
    main()
