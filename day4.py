def fetch_input(filename):
    with open(filename, "r") as f:
        matrix = [list(line.strip()) for line in f]
    return matrix

def is_valid(x,y,rows,cols):
    return 0 <= x < rows and 0 <= y < cols

def count_word_occurrences(matrix, word):
    rows, cols = len(matrix), len(matrix[0])
    word_length = len(word)

    directions = [
        (0 , 1),
        (0 , -1),
        (1 , 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    count = 0

    for row in range(rows):
        for col in range(cols):
            for dy,dx in directions:
                found = True
                for k in range(word_length):
                    nx,ny = row + k * dx, col + k * dy
                    if not is_valid(nx, ny, rows, cols) or matrix[nx][ny] != word[k]:
                        found = False
                        break
                if found:
                    count += 1
    return count

def main():
    filename = "/Users/kasmira/Documents/Code/adventofcode2024/text4.txt"
    word = "XMAS"
    matrix = fetch_input(filename)
    count = count_word_occurrences(matrix,word)
    print("The count of XMAS occurences is ", count)

if __name__ == "__main__":
    main()