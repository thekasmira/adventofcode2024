def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for row in range(1, rows - 1): 
        for col in range(1, cols - 1):  
            if (
                grid[row][col] == 'A' and
                grid[row - 1][col - 1] == 'M' and
                grid[row + 1][col + 1] == 'S' and
                grid[row - 1][col + 1] == 'M' and
                grid[row + 1][col - 1] == 'S'
            ):
                count += 1
            
            elif (
                grid[row][col] == 'A' and
                grid[row - 1][col - 1] == 'S' and
                grid[row + 1][col + 1] == 'M' and
                grid[row - 1][col + 1] == 'M' and
                grid[row + 1][col - 1] == 'S'
            ):
                count += 1

            elif (
                grid[row][col] == 'A' and
                grid[row - 1][col - 1] == 'S' and
                grid[row + 1][col + 1] == 'M' and
                grid[row - 1][col + 1] == 'S' and
                grid[row + 1][col - 1] == 'M'
            ):
                count += 1

            elif (
                grid[row][col] == 'A' and
                grid[row - 1][col - 1] == 'M' and
                grid[row + 1][col + 1] == 'S' and
                grid[row - 1][col + 1] == 'S' and
                grid[row + 1][col - 1] == 'M'
            ):
                count += 1            
            
    return count

def main():
    filename = "/Users/kasmira/Documents/Code/adventofcode2024/text4.txt"
    with open(filename, "r") as f:
        matrix = [list(line.strip()) for line in f]

    result = count_xmas(matrix)
    print("Number of X-MAS patterns:", result)

if __name__ == "__main__":
    main()