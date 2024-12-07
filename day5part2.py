from collections import defaultdict, deque

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

def topological_sort(nodes, edges):
    """ Perform a topological sort on the given graph.
        nodes: set of all nodes (pages)
        edges: dict of node -> list of nodes that must come after
    """
    in_degree = {node: 0 for node in nodes}
    for u in edges:
        for v in edges[u]:
            in_degree[v] += 1

    queue = deque([n for n in nodes if in_degree[n] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in edges[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(result) != len(nodes):
        raise ValueError("No valid ordering found (cycle in rules?).")
    return result

def reorder_update(update, rules):
    pages = set(update)
    applicable_edges = defaultdict(list)
    for (A, B) in rules:
        if A in pages and B in pages:
            # A must come before B
            applicable_edges[A].append(B)

    sorted_pages = topological_sort(pages, applicable_edges)
    return sorted_pages

if __name__ == "__main__":
    rules, updates = read_data_from_file("/Users/kasmira/Documents/Code/adventofcode2024/text5.txt")  

    correct_middle_sum = 0
    incorrect_updates = []
    
    for update in updates:
        if check_update_order(update, rules):
            mid_index = len(update) // 2
            correct_middle_sum += update[mid_index]
        else:
            incorrect_updates.append(update)

    print("Sum of middle pages of correctly-ordered updates:", correct_middle_sum)

    fixed_middle_sum = 0
    for update in incorrect_updates:
        reordered = reorder_update(update, rules)
        mid_index = len(reordered) // 2
        fixed_middle_sum += reordered[mid_index]

    print("Sum of middle pages of previously incorrectly-ordered (now fixed) updates:", fixed_middle_sum)