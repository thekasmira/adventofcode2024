import re

def extract_and_sum(input_data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    matches = re.findall(pattern, input_data)

    total_sum = sum(int(x) * int(y) for x,y in matches)

    return total_sum

def main():

    filename = "/Users/kasmira/Documents/Code/adventofcode2024/text3.txt"

    try:
        with open(filename, "r") as file:
            input_data = file.read()
    except FileNotFoundError:
        print(f"File name '{filename}' not found.")
        return
    
    total_sum = extract_and_sum(input_data)

    print("Sum of all multiplications: ", total_sum)
    
if __name__ == "__main__":
    main()
