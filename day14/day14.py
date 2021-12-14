def main() -> None:
    with open('input.txt') as file:
        input_data = file.read().splitlines()

    template = input_data[0]

    insertion_rules = {}
    for line in input_data[2:]:
        split = line.split(" -> ")
        insertion_rules[split[0]] = split[1]

    repetitions = 10

    for _ in range(repetitions):  # Brute force, because, oh well, why not
        new_polymer = ""
        for i in range(len(template)-1):
            lookup = template[i:i+2]
            new_polymer += lookup[0] + insertion_rules[lookup]
        new_polymer += template[-1]
        template = new_polymer

    elements = set(insertion_rules.values())
    min_val = len(template)
    max_val = 0

    for element in elements:
        max_val = max(max_val, template.count(element))
        min_val = min(min_val, template.count(element))

    print(max_val - min_val)


if __name__ == '__main__':
    main()
