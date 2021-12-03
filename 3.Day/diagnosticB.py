pows = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]


def converter(binary):
    index = 0
    tmp = 0
    for bit in binary[::-1]:
        if bit == "1":
            tmp += pows[index]
        index += 1
    return tmp


def get_o2():
    file = open("input.txt")
    lines  = file.read().splitlines()
    o2 = ""
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
        if count_of_one == count_of_zero:
            o2 += "1"
        elif count_of_zero > count_of_one:
            o2 += "0"
        else:
            o2 += "1"
        tmp = []
        for item in lines:
            if o2 not in item[0:index]:
                tmp.append(item)
        for item in tmp:
            lines.remove(item)
        if len(lines) == 1:
            return lines[0]
                    
def get_co2():
    file = open("input.txt")
    lines  = file.read().splitlines()
    co2 = ""
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
        if count_of_one == count_of_zero:
            co2 += "0"
        elif count_of_zero > count_of_one:
            co2 += "1"
        else:
            co2 += "0"
        tmp = []
        for item in lines:
            if co2 not in item[0:index]:
                tmp.append(item)
        for item in tmp:
            lines.remove(item)
        if len(lines) == 1:
            return lines[0]


def main():
    print(f"Result: {converter(get_o2())*converter(get_co2())}")


if __name__ == "__main__":
    main()