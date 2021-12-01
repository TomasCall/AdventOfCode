
def main():
    file = open("input.txt")
    lines  = file.read().splitlines()
    sum_of_three = []
    for i in range(len(lines)):
        try:
            sum_of_three.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))
        except:
            break
    counter = 0
    for i in range(1,len(sum_of_three)):
        if sum_of_three[i] > sum_of_three[i-1]:
            counter += 1
    print(f" The answer is :{counter}")


if __name__ == "__main__":
    main()