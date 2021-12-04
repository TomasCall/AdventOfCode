
class Table:
    def __init__(self, table):
        self.table = table
        self.table_tf = []
        for i in range(5):
            tmp = []
            for j in range(5):
                tmp.append(False)
            self.table_tf.append(tmp)

    def cehck_row(self,row_num):
        counter = 0
        for i in range(5):
            if self.table_tf[row_num][i] == True:
                counter += 1
        return counter == 5


    def check_column(self,col_num):
        counter = 0
        for i in range(5):
            if self.table_tf[i][col_num] == True:
                counter += 1
        return counter == 5


    def check_rows(self):
        for i in range(5):
            if self.cehck_row(i):
                return True


    def check_columns(self):
        counter  = 0
        for i in range(5):
            if self.check_column(i):
                return True


    def number_drawn(self,number):
        for i in range(5):
            for j in range(5):
                if self.table[i][j] == number.strip():
                    self.table_tf[i][j] = True


def get_score(numbers_drawn,cards):
    i = 0
    while i < len(numbers_drawn):
        for item in cards:
            item.number_drawn(numbers_drawn[i])
            if item.check_columns() == True or item.check_rows() == True:
                tmp_sum = 0
                print(numbers_drawn[i])
                for k in range(5):
                    for j in range(5):
                        if item.table_tf[k][j] == False:
                            tmp_sum += int(item.table[k][j])
                print(tmp_sum)
                return tmp_sum * int(numbers_drawn[i])
        i += 1
    return -1


def main():
    file = open("input.txt")
    lines = file.read().splitlines()
    numbers_drawn = lines[0].split(",")
    lines.remove(lines[0])
    rows = []
    for line in lines:
        if line != '':
            rows.append(line)
    cards = []
    for i in range(0,len(rows),5):
        tmp = []
        tmp.append(rows[i].split())
        tmp.append(rows[i + 1].split())
        tmp.append(rows[i + 2].split())
        tmp.append(rows[i + 3].split())
        tmp.append(rows[i + 4].split())
        card = Table(tmp)
        cards.append(card)
    print(f"The answer is: {get_score(numbers_drawn,cards)}")

if __name__=="__main__":
    main()