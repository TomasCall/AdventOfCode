

def main():
    file = open("input.txt")
    lines  = file.read().splitlines()
    counter = 0
    for i in range(1,len(lines)):
        if int(lines[i]) > int(lines[i-1]):
            counter += 1
    print(f"  The answer is :{counter}")


if __name__ == "__main__":
    main()