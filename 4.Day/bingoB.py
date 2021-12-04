
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


def get_score(card,numbers_drawn):
    i = 0
    while i < len(numbers_drawn):
        card.number_drawn(numbers_drawn[i])
        if card.check_columns() == True or card.check_rows() == True:
            tmp_sum = 0
            print(numbers_drawn[i])
            for k in range(5):
                for j in range(5):
                    if card.table_tf[k][j] == False:
                        tmp_sum += int(card.table[k][j])
            return tmp_sum * int(numbers_drawn[i])
        i += 1
    return -1


def win_num(table,numbers_drawn):
    i = 0
    while i < len(numbers_drawn):
        table.number_drawn(numbers_drawn[i])
        if table.check_columns() == True or table.check_rows() == True:
            return i
        i += 1
    return i


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
    tmp_cards = cards[::]
    for i in range(0,len(rows),5):
        tmp = []
        tmp.append(rows[i].split())
        tmp.append(rows[i + 1].split())
        tmp.append(rows[i + 2].split())
        tmp.append(rows[i + 3].split())
        tmp.append(rows[i + 4].split())
        card = Table(tmp)
        cards.append(card)
        cardb = Table(tmp)
        tmp_cards.append(cardb)
    tmp = []
    for item in cards:
        tmp.append(win_num(item,numbers_drawn))
    card = tmp_cards[tmp.index(max(tmp))]
    print(card.table)
    print(card.table_tf)
    print(max(tmp))
    print(f"The answer is: {get_score(card,numbers_drawn)}")

if __name__=="__main__":
    main()