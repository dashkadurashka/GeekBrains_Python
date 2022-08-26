import copy


class Matrix:
    def __init__(self, my_mtr):
        self.matrix = my_mtr

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        result = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                result[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(result)


m_1 = [[14, 23, 34], [43, 456, 45], [25, 66, 67]]
m_2 = [[141, 221, 41], [315, 41, 512], [551, 616, 627]]
mtr_1 = Matrix(m_1)
mtr_2 = Matrix(m_2)
new_mtr = mtr_1 + mtr_2
print(new_mtr)
