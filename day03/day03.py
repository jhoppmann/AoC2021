with open('input.txt') as file:
    readings = file.read().splitlines()


def main():
    entries = len(readings)
    ones = {}
    for line in readings:
        for index, number in enumerate(line):
            if number == '1':
                if index in ones:
                    ones[index] += 1
                else:
                    ones[index] = 1

    gamma = ""
    epsilon = ""
    for i in range(len(readings[0])):
        if ones[i] > (entries / 2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print(int(gamma, 2) * int(epsilon, 2))


if __name__ == '__main__':
    main()
