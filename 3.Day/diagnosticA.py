pows = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]


def converter(binary):
    index = 0
    tmp = 0
    for bit in binary[::-1]:
        if bit == "1":
            tmp += pows[index]
        index += 1
    return tmp


def main():
    file = open("input.txt")
    lines  = file.read().splitlines()
    gamma = ""
    epsilon = ""
    index = 0
    while index < len(lines[0]):
        count_of_zero = 0
        count_of_one = 0
        for line in lines:
            if line[index] == "0":
                count_of_zero += 1
            else:
                count_of_one += 1
        index += 1
        if count_of_one > count_of_zero:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(gamma)
    print(epsilon)
    print(f"Result: {converter(gamma) * converter(epsilon)}")
    



if __name__ == "__main__":
    main()