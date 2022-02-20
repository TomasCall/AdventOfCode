class Line:
    def __init__(self, coordinates, map_of_ocean):
        self.x1 = coordinates[0]
        self.y1 = coordinates[1]
        self.x2 = coordinates[2]
        self.y2 = coordinates[3]
        self.draw(map_of_ocean)

    def direction(self):
        if self.x1 == self.x2:
            return 1
        elif self.y1 == self.y2:
            return 2

    def draw(self, map_of_ocean):
        if self.direction() ==  1:
            for i in range(self.y1,self.y2+1):
                map_of_ocean[self.x1][i] += 1
        elif self.direction() ==  2: 
            for i in range(self.x1,self.x2+1):
                map_of_ocean[i][self.y1] += 1
        

def main():
    file  = open("proba.txt")
    lines = file.read().splitlines()
    pair_cordinates = []
    max_x = 0
    max_y = 0
    for line in lines:
        tmp = []
        x1 = int(line.split()[0].split(",")[0])
        y1 = int(line.split()[0].split(",")[1])
        x2 = int(line.split()[2].split(",")[0])
        y2 = int(line.split()[2].split(",")[1])

        if x1 == x2:
            if y1 < y2:
                tmp.append(x1)
                tmp.append(y1)
                tmp.append(x2)
                tmp.append(y2)
            else:
                tmp.append(x2)
                tmp.append(y2)
                tmp.append(x1)
                tmp.append(y1)
        elif y1 == y2:
            if x1 < x2:
                tmp.append(x1)
                tmp.append(y1)
                tmp.append(x2)
                tmp.append(y2)
            else:
                tmp.append(x2)
                tmp.append(y2)
                tmp.append(x1)
                tmp.append(y1)
        else:
                tmp.append(x1)
                tmp.append(y1)
                tmp.append(x2)
                tmp.append(y2)

        if tmp[0] > max_x:
            max_x = tmp[0]
        elif tmp[2] > max_x:
            max_x = tmp[2]

        if tmp[1] > max_x:
            max_x = tmp[1]
        elif tmp[3] > max_y:
            max_y = tmp[3]
        pair_cordinates.append(tmp)
    map_of_ocean = []
    for i in range(max_x+1):
        tmp = []
        for j in range(max_y+1):
            tmp.append(0)
        map_of_ocean.append(tmp)
    lines_objects = []
    for item in pair_cordinates:
        tmp_object = Line(item, map_of_ocean)
        lines_objects.append(tmp_object)
    count = 0
    for item in map_of_ocean:
        for number in item:
            if number >= 2:
                count += 1
    print(f"The answer is:{count}")
    for item in map_of_ocean:
        print(item)

if __name__ == "__main__":
    main()