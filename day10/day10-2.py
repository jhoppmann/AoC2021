import statistics
from pprint import pprint


def main() -> None:
    with open('input.txt') as file:
        input_data = file.read().splitlines()
    points = {')': 1,
              ']': 2,
              '}': 3,
              '>': 4}
    char_mapping = {')': '(',
                    '}': '{',
                    ']': '[',
                    '>': '<'}
    char_mapping_reverse = {v: k for k, v in char_mapping.items()}

    incomplete_stacks = []
    for line in input_data:
        stack = []
        corrupted = False
        for char in line:
            if char in char_mapping.values():
                stack.append(char)
            else:
                opening = stack.pop()
                if opening != char_mapping[char]:
                    corrupted = True
                    break
        if not corrupted:
            incomplete_stacks.append(stack)

    scores = []
    for stack in incomplete_stacks:
        score = 0
        stack.reverse()
        for bracket in stack:
            closer = char_mapping_reverse[bracket]
            point_add = points[closer]
            score *= 5
            score += point_add
        scores.append(score)
    print(statistics.median(scores))


if __name__ == '__main__':
    main()
