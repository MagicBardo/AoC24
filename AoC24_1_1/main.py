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

def pair_lists(list1: list[str], list2: list[str]) -> list[tuple[str, str]]:
    list1.sort()
    list2.sort()
    return list(zip(list1, list2))

def type_casting(values: list[tuple[str, str]]) -> list[tuple[int, int]]:
    casted = []
    for pair in values:
        casted.append((int(pair[0]), int(pair[1])))
    return casted

def calc_difference(pair: tuple[str, str]) -> list[int]:
    return abs(int(pair[0]) - int(pair[1]))

def main():
    file_path = Path(__file__).parent / "../inputs/day1.txt"
    ans = 0
    list1, list2 = devide_lists(get_input_path(file_path))
    paired = pair_lists(list1, list2)
    casted = type_casting(paired)
    differences = [calc_difference(pair) for pair in casted]
    ans = sum(differences)

    print(f"Answer of task 1.1: {ans}")

if __name__ == "__main__":
    main()