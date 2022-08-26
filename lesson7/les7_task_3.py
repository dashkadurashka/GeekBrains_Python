class Cell:
    def __init__(self, quant):
        self.quant = quant

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quant // cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quant % cells_in_row)}'
        return row

    def __str__(self):
        return f'Результат операции {self.quant}'

    def __add__(self, other):
        return Cell(self.quant + other.quant)

    def __sub__(self, other):
        return Cell(self.quant - other.quant) if self.quant - other.quant > 0 else "Err!"

    def __mul__(self, other):
        return Cell(self.quant * other.quant)

    def __truediv__(self, other):
        return Cell(self.quant // other.quant)




cell_1 = Cell(7)
cell_2 = Cell(38)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(5))

