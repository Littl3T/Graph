class Edge:
    def __init__(self, A: object, B: object, value: int):
        # Each edge is a link between two vertex, A and B
        # the value is the travel cost between those two points
        self.__A = A
        self.__B = B
        self.__value = value

    def __repr__(self):
        return f"Edge ({self.__A.name}-{self.__B.name})"

    @property
    def A(self):
        return self.__A

    @A.setter
    def A(self,value):
        self.__A = value

    @property
    def B(self):
        return self.__B

    @B.setter
    def B(self,value):
        self.__B = value

    @property
    def value(self):
        return self.__value
