def main():
    file = open("input.txt")
    lines  = file.read().splitlines()
    horizontal = 0
    vertical = 0
    aim = 0
    for item in lines:
        if item.split()[0] == "forward":
            horizontal += int(item.split()[1])
            vertical += aim * int(item.split()[1])
        elif item.split()[0] == "up":
            aim -= int(item.split()[1])
        elif item.split()[0] == "down":
            aim += int(item.split()[1])
    result = horizontal * vertical
    print(f"The answer is: {result}")


if __name__ == "__main__":
    main()