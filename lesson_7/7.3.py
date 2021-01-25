class Cell:

    def __init__(self, c_cell):
        self.c = c_cell

    def __add__(self, other):
        return Cell(self.c + other.c)

    def __mul__(self, other):
        return Cell(self.c * other.c)

    def __sub__(self, other):
        if self.c - other.c > 0:
            return Cell(self.c - other.c)
        else:
            return "Вычитание невозможно"

    def __floordiv__(self, other):
        try:
            return Cell(self.c // other.c)
        except ZeroDivisionError:
            return "На ноль делить нельзя"

    def __str__(self):
        return f"{self.c} ячеек"

    def make_order(self, n):
        return (("*" * n) + "\n") * (self.c // n) + ("*" * (self.c % n))

cell_1 = Cell(14)
cell_2 = Cell(0)
cell_3 = Cell(20)

print(cell_1.c)
print(cell_1 + cell_2 + cell_3)
print(cell_1 - cell_2)
print(cell_1 - cell_3)
print(cell_1 * cell_2 * cell_3)
print(cell_1 // cell_2)
print(cell_3 // cell_1)
print(cell_1.make_order(3))