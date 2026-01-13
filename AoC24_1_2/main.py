from pathlib import Path

def get_input_path(filepath: str) -> list[str]:
    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines

def devide_lists(input: list[str]):
    list1 = []
    list2 = []
    for line in input:
        parts = line.split()
        list1.append(parts[0].strip())
        list2.append(parts[1].strip())
    return list1, list2

def type_casting(values: list[str]) -> list[int]:
    casted = []
    for value in values:
        casted.append(int(value))
    return casted

def similary_count(value:int, check_list: list[int]) -> int:
    count = 0
    for item in check_list:
        if item == value:
            count += 1
    return count

def solve(list1: list[int], list2: list[int]) -> int:
    total = 0
    for value in list1:
        total += value * similary_count(value, list2)
    return total

def main():
    file_path = Path(__file__).parent / "../inputs/day1.txt"
    ans = 0
    list1, list2 = devide_lists(get_input_path(file_path))
    list1 = type_casting(list1)
    list2 = type_casting(list2)

    ans = solve(list1, list2)
    print(f"Answer of task 1.2: {ans}")

if __name__ == "__main__":
    main()