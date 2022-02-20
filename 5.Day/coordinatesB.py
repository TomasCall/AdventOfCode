class Line:
    def __init__(self, coordinates, map_of_ocean,d):
        self.x1 = coordinates[0]
        self.y1 = coordinates[1]
        self.x2 = coordinates[2]
        self.y2 = coordinates[3]
        tmp = f"{self.x1} {self.y1}"
        if tmp in d:
            d[tmp] += 1
        else:
            d[tmp] = 0
        tmps = f"{self.x2} {self.y2}"
        if tmps in d:
            d[tmps] += 1
        else:
            d[tmps] = 0
        map_of_ocean.append(tmp)
        self.draw(map_of_ocean,d)

    def direction(self):
        if self.x1 == self.x2:
            return 1
        elif self.y1 == self.y2:
            return 2
        elif self.y1 < self.y2:
            if self.x1 < self.x2:
                return 3
            else:
                return 4
        elif self.y1 > self.y2:
            if self.x1 < self.x2:
                return 5
            else:
                return 6

#asd
    def draw(self, map_of_ocean,d):
        if self.direction() ==  1:
            for i in range(self.y1+1,self.y2):
                tmp = f"{self.x1} {i}"
                if tmp in d:
                    d[tmp] += 1
                else:
                    d[tmp] = 0
                map_of_ocean.append(tmp)
        elif self.direction() ==  2: 
            for i in range(self.x1+1,self.x2):
                tmp = f"{i} {self.y1}"
                if tmp in d:
                    d[tmp] += 1
                else:
                    d[tmp] = 0
                map_of_ocean.append(tmp)
        elif self.direction() == 3:
            x1 = self.x1
            y1 = self.y1
            while x1 != self.x2 and y1 != self.y2:
                x1 += 1
                y1 += 1
                tmp = f"{x1} {y1}"
                if tmp in d:
                    d[tmp] += 1
                else:
                    d[tmp] = 0
                map_of_ocean.append(tmp)
        elif self.direction() == 4:
            x1 = self.x1
            y1 = self.y1
            while x1 != self.x2 and y1 != self.y2:
                x1 -= 1
                y1 += 1
                tmp = f"{x1} {y1}"
                if tmp in d:
                    d[tmp] += 1
                else:
                    d[tmp] = 0
                map_of_ocean.append(tmp)
        elif self.direction() == 5:
            x1 = self.x1
            y1 = self.y1
            while x1 != self.x2 and y1 != self.y2:
                x1 += 1
                y1 -= 1
                tmp = f"{x1} {y1}"
                if tmp in d:
                    d[tmp] += 1
                else:
                    d[tmp] = 0
                map_of_ocean.append(tmp)
        elif self.direction() == 6:
            x1 = self.x1
            y1 = self.y1
            while x1 != self.x2 and y1 != self.y2:
                x1 -= 1
                y1 -= 1
                tmp = f"{x1} {y1}"
                if tmp in d:
                    d[tmp] += 1
                else:
                    d[tmp] = 0
                map_of_ocean.append(tmp)
        

def is_count_bigger_than_two(item,map_of_ocean):
    count = 0
    for element in map_of_ocean:
        if element == item:
            count +=1
            if count == 2:
                return True


def main():
    d = {}
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

        if tmp[1] > max_y:
            max_y = tmp[1]
        elif tmp[3] > max_y:
            max_y = tmp[3]
        pair_cordinates.append(tmp)
    map_of_ocean = []
    lines_objects = []
    for item in pair_cordinates:
        tmp_object = Line(item, map_of_ocean,d)
        lines_objects.append(tmp_object)
    count = 0
    print("hey")
    """
        for item in tmp_map_of_ocean:
        if is_count_bigger_than_two(item,map_of_ocean):
            count += 1
            print("Doing stuff")
    """
    for item in d.values():
        if item > 0:
            count += 1
    print(f"The answer is:{d}")
    t = []


if __name__ == "__main__":
    main()