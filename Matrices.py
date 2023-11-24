class Matrix:
    """
    Esta clase emula las operaciones de matrices
    - Suma
    - Resta
    - Multiplicación entre matrices
    - Inversa
    - Transpuesta

    """
    def __init__(self, matrix:list) -> None:
        self.matrix = matrix
        pass

    def __repr__(self):
        return repr(self.matrix)

    def __str__(self):
        return repr(self.matrix)

    def transpose(self):
        """
        Transpuesta de una matriz por definición
        """
        R = [[None] * len(self.matrix) for _ in range(len(self.matrix[0]))]
        i = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                R[j][i] = self.matrix[i][j]
            j = 0
        return Matrix(R)
    
    def concatenate(self,B):
        """
        Concatenar matrices para obtener matrix aumentada
        """
        C = [[0] * len(self.matrix[0]*2) for _ in range(len(self.matrix))]
        for i in range(len(C)):
            C[i] = (self.matrix[i]+B.matrix[i])

        return Matrix(C)
    
    @staticmethod
    def identity(n:int):
        """
        Retorna matriz identidad
        """
        return Matrix([[1 if i==j else 0 for i in range(n)] for j in range(n)])
    
    def invertir(self):
        """
        Invertir matrices
        """
        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("La matriz debe ser cuadrada para tener una inversa.")
        
        n = len(self.matrix)
        I = Matrix.identity(n)
        A_aumented = Matrix(self.matrix).concatenate(I).matrix
        for i in range(n):
            divisor = A_aumented[i][i]
            A_aumented[i] = [x/divisor for x in A_aumented[i]]
            for j in range(n):
                if i != j:
                    factor = A_aumented[j][i]
                    factor = [-1*x*factor for x in A_aumented[i]]
                    A_aumented[j] = [x+y for x,y in zip(factor,A_aumented[j])]
        
        return Matrix([x[n:] for x in A_aumented])

    def __mul__(self,B):
        """
        Producto de matrices por definición
        """

        if len(self.matrix[0]) == len(B.matrix):
            C = [[0] * len(B.matrix[0]) for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(B.matrix[0])):
                    for k in range(len(B.matrix)):
                        C[i][j] += self.matrix[i][k] * B.matrix[k][j]
            result = Matrix(C)  
            if len(result.matrix) == 1:#Caso de producto interno, el retorno es un número real
                return result.matrix[0][0]
            else:
                return result
        else:
            raise ValueError('La matriz izquierda debe tener el mismo número de columnas que las filas de la derecha ')

    def __add__(self,B):
        """
        Suma de matrices por definición
        """
        return Matrix([[self.matrix[i][j] + B.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])
    
    def __sub__(self,B):
        return Matrix([[self.matrix[i][j] - B.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])
    