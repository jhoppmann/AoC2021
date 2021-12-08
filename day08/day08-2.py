def main() -> None:
    with open('input.txt') as file:
        lines = file.read().splitlines()

    result = 0
    for line in lines:
        numbers = {}
        notes, output = line.split(" | ")
        output = output.split()
        notes = notes.split()
        for token in notes:
            if len(token) == 2:
                numbers[1] = token
            if len(token) == 3:
                numbers[7] = token
            if len(token) == 4:
                numbers[4] = token
            if len(token) == 7:
                numbers[8] = token
        #   1
        #  2 3
        #   4
        #  5 6
        #   7
        segments = {}
        segments_by_number = {
            0: [1, 2, 3, 5, 6, 7],
            1: [3, 6],
            2: [1, 3, 4, 5, 7],
            3: [1, 3, 4, 6, 7],
            4: [2, 3, 4, 6],
            5: [1, 2, 4, 6, 7],
            6: [1, 2, 4, 5, 6, 7],
            7: [1, 3, 6],
            8: [1, 2, 3, 4, 5, 6, 7],
            9: [1, 2, 3, 4, 6, 7]}
        segments[1] = find_segment(1, numbers)
        segments[2] = find_segment(2, numbers, notes)
        segments[3] = find_segment(3, numbers, notes, segments)
        segments[5] = find_segment(5, numbers, notes)

        segments[6] = find_segment(6, numbers, notes, segments)
        segments[4] = find_segment(4, numbers, notes, segments)
        segments[7] = find_segment(7, numbers, notes, segments)

        ordered_representations = order_all(segments, segments_by_number)

        output_as_number = to_number(output, ordered_representations)
        result += output_as_number
    print(result)


def find_segment(segment: int, numbers: dict, notes: list = None, segments: dict = None) -> str:
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if segment == 1:
        for char in characters:
            if char in numbers[7] and char not in numbers[1]:
                return char
    if segment == 2:
        for character in characters:
            counter = 0
            for note in notes:
                if character in note:
                    counter += 1
            if counter == 6:
                return character
    if segment == 3:
        for character in characters:
            if segments[1] == character:
                continue
            counter = 0
            for note in notes:
                if character in note:
                    counter += 1
            if counter == 8:
                return character
    if segment == 4:
        for character in characters:
            if character in numbers[4] \
                    and character != segments[2] \
                    and character != segments[3] \
                    and character != segments[6]:
                return character
    if segment == 5:
        for character in characters:
            counter = 0
            for note in notes:
                if character in note:
                    counter += 1
            if counter == 4:
                return character
    if segment == 6:
        for character in characters:
            if character in numbers[1] and character != segments[3]:
                return character
    if segment == 7:
        for character in characters:
            if character not in segments.values():
                return character


def order_all(segments: dict, segments_by_number: dict) -> dict:
    ordered = {}
    for number, representation in segments_by_number.items():
        chars = []
        for num in representation:
            chars.append(segments[num])
        chars.sort()
        ordered[number] = chars
    return ordered


def to_number(output: list, ordered_representation: dict) -> int:
    result_string = ""
    for token in output:
        ordered = list(token)
        ordered.sort()
        for k, v in ordered_representation.items():
            if v == ordered:
                result_string += str(k)
    return int(result_string)


if __name__ == '__main__':
    main()
