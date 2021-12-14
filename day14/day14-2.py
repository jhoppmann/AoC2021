import timeit


def main() -> None:
    start = timeit.default_timer()
    with open('input.txt') as file:
        input_data = file.read().splitlines()

    template = input_data[0]

    insertion_rules = {}
    for line in input_data[2:]:
        split = line.split(" -> ")
        insertion_rules[split[0]] = split[1]

    pair_count = {}
    counts_by_element = {}
    for letter_pair in insertion_rules.keys():
        pair_count[letter_pair] = 0

    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        pair_count[pair] += 1

    for char in template:
        if char not in counts_by_element:
            counts_by_element[char] = 0
        counts_by_element[char] += 1

    repetitions = 40

    for _ in range(repetitions):
        new_pair_count = pair_count.copy()
        for k, v in pair_count.items():
            if v != 0:
                new_char = insertion_rules[k]
                chain_one = k[0] + new_char
                chain_two = new_char + k[1]
                new_pair_count[chain_one] += v
                new_pair_count[chain_two] += v
                new_pair_count[k] -= v
                if new_char not in counts_by_element:
                    counts_by_element[new_char] = 0
                counts_by_element[new_char] += v
        pair_count = new_pair_count

    print(max(counts_by_element.values()) - min(counts_by_element.values()))
    stop = timeit.default_timer()
    print('Time: ', stop - start)


if __name__ == '__main__':
    main()
