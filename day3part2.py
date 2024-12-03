import re

def extract_and_check_enabled_and_sum(input_data):
    multi_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    yes_pattern = r"do\(\)"
    no_pattern = r"don\'t\(\)" 

    enabled = True
    total_sum = 0

    tokens = re.split(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))", input_data)

    for token in tokens:
        token = token.strip()
        if not token:
            continue

        if re.fullmatch(yes_pattern, token):
            enabled = True

        elif re.fullmatch(no_pattern, token):
            enabled = False

        elif re.fullmatch(multi_pattern, token):
            if enabled:
                x, y = map(int, re.findall(r"\d+", token))
                total_sum += x * y

    return total_sum

def main():
    filename = "/Users/kasmira/Documents/Code/adventofcode2024/text3.txt"

    try: 
        with open(filename, "r") as file:
            input_data = file.read()
    except FileNotFoundError:
        print(f"File named '{filename}' not found.")
        return
    
    total_sum = extract_and_check_enabled_and_sum(input_data)
    print("The total sum is:", total_sum)

if __name__ == "__main__":
    main()