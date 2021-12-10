def main() -> None:
    with open('input.txt') as file:
        input_data = file.read().splitlines()
    points = {')': 3,
              ']': 57,
              '}': 1197,
              '>': 25137}
    char_mapping = {')': '(',
                    '}': '{',
                    ']': '[',
                    '>': '<'}

    score = 0
    for line in input_data:
        stack = []
        for char in line:
            if char in char_mapping.values():
                stack.append(char)
            else:
                opening = stack.pop()
                if opening != char_mapping[char]:
                    score += points[char]
                    break
    print(score)


if __name__ == '__main__':
    main()
