TREE = '#'
EMPTY = '.'


def main():
    with open('./input') as input_file:
        rows = list(map(str.strip, input_file.readlines()))
        length = len(rows[0])
        height = len(rows)
        col_offset = 3
        row_offset = 1
        col_index = (0 + col_offset) % length
        row_index = 0 + row_offset
        tree_count = 0

        while row_index < height:
            if rows[row_index][col_index] == TREE:
                tree_count += 1
            row_index += row_offset
            col_index = (col_index + col_offset) % length
        print(tree_count)


if __name__ == '__main__':
    main()
