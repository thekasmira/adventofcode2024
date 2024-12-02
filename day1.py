from collections import Counter

def fetch_input(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.read().split()))
    
    
def parse_input(data):
    list1 = data[::2]
    list2 = data[1::2]
    return list1, list2
    
def process_and_compare (list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)

    total_distance = 0

    for a,b in zip(list1,list2):
        diff = abs(a - b)
        total_distance += diff

    return total_distance

def count_similarity_score(right_list,left_list):
    right_count = Counter(right_list)

    similarity_score = 0

    for num in left_list:
        similarity_score += num * right_count[num]

    return similarity_score
    

def main():
    path = "/Users/kasmira/Documents/Code/adventofcode2024/text.txt"
    data = fetch_input(path)
    list1, list2 = parse_input(data)
    result = process_and_compare(list1, list2)
    score = count_similarity_score(list1,list2)
    print("Sum of results: ", result)
    print("Similarity Score: ", score)

if __name__ == "__main__":
    main()