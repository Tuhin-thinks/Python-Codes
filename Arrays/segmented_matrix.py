def find_all_left_diag(matrix):
    start_positions = []
    
    # gather all first row positions
    for i in range(len(matrix[0])):
        start_positions.append((0, i))
    
    # gather all left column positions excep first row, first col
    for i in range(1, len(matrix)):
        start_positions.append((i, 0))

    for pos in start_positions:
        current_position = pos
        last_elem = None
        # calculate diagonal sum
        while True:
            row, col = current_position
            
            current_position = (row+1, col+1)
            row, col = current_position

            if row < len(matrix) and col < len(matrix[0]):
                elem = matrix[row][col]
                if last_elem is None:
                    last_elem = elem
                elif last_elem != elem:
                    return False
            else:
                break
    return True


if __name__ == "__main__":
    mat = []
    n, m  = tuple(map(int, input().split()))
    for row_index in range(n):
        elems = list(map(int, input().split()))
        mat.append(elems)

    res = find_all_left_diag(mat)
    if res:
        print("YES")
    else:
        print("NO")