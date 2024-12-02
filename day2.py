def fetch_input(filename):
    with open(filename, "r") as f:
        return [list(map(int, line.split())) for line in f if line.strip()]
    
def is_safe_report(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    if all(1 <= diff <= 3 for diff in differences):
        return True
    
    if all(-3 <= diff <= -1 for diff in differences):
        return True
    
    return False

def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe_report(report))

def main():
    path = "/Users/kasmira/Documents/Code/adventofcode2024/text2.txt"
    try:
        report_list = fetch_input(path)
    except FileNotFoundError:
        print(f"The file '{path}' is not found")
        return
        
    safe_count = count_safe_reports(report_list)
    print("The number of safe reports is: ", safe_count)

if __name__ == "__main__":
    main()
