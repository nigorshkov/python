class Matrix:
    def __init__(self, *args):
        self.matrix = [*args]

    def __str__(self):
        result = ''
        for i in self.matrix:
            for j in i:
                result += str(j) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        new_matrix = []
        try:
            for i in range(len(self.matrix)):
                list = []
                for j in range(len(self.matrix[i])):
                    list.append(self.matrix[i][j] + other.matrix[i][j])
                new_matrix.append(list)
            return new_matrix
        except:
            return 'Ошибка, у матриц разная размерность'


a = Matrix([1, 2, 3], [3, 4, 5], [1, 2, 3])
b = Matrix([5, 6, 5], [7, 8, 6], [2, 4, 6])
c = a + b
print(c)
