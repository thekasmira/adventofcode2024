def parse_rule_line(line):
    parts = line.strip().split('|')
    if len(parts) != 2:
        return None
    A, B = parts
    return int(A), int(B)

def parse_update_line(line):
    parts = line.strip().split(',')
    return [int(x) for x in parts]

def check_update_order(update, rules):
    page_to_index = {page: i for i, page in enumerate(update)}
    
    for (A, B) in rules:
        if A in page_to_index and B in page_to_index:
            if page_to_index[A] >= page_to_index[B]:
                return False
    return True

def read_data_from_file(filename):
    with open(filename, 'r') as f:
        lines = [line for line in f]

    blank_line_index = None
    for i, line in enumerate(lines):
        if line.strip() == '':
            blank_line_index = i
            break
    
    rule_lines = lines[:blank_line_index]
    update_lines = lines[blank_line_index+1:]
    
    rules = []
    for line in rule_lines:
        line = line.strip()
        if line:
            rule = parse_rule_line(line)
            if rule:
                rules.append(rule)
    
    updates = []
    for line in update_lines:
        line = line.strip()
        if line:
            update = parse_update_line(line)
            updates.append(update)
    
    return rules, updates

if __name__ == "__main__":
    rules, updates = read_data_from_file("/Users/kasmira/Documents/Code/adventofcode2024/text5.txt") 
    
    middle_sum = 0
    for i, update in enumerate(updates, start=1):
        if check_update_order(update, rules):
            mid_index = len(update) // 2
            middle_page = update[mid_index]
            middle_sum += middle_page
    
    print(middle_sum)