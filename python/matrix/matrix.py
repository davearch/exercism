class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split('\n')
        self.m = []
        for row in rows:
            self.m.append([int(num) for num in row.split(' ')])

    def row(self, index):
        if len(self.m) >= index-1:
            return self.m[index-1]

    def column(self, index):
        if len(self.m) and len(self.m) >= index -1:
            output = []
            for i in range(len(self.m)):
                output.append(self.m[i][index-1])
            return output
