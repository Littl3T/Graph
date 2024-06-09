class Vertex:
    def __init__(self, name: str):
        # A vertex is simply a point in the graph
        # Represented by its name
        self.__name = name

    def __lt__(self, other):
        return self.__name < other.name

    def __eq__(self, other):
        return self.__name == other.name

    def __hash__(self):
        return hash(self.__name)

    def __repr__(self):
        return f"Vertex({self.__name})"

    @property
    def name(self):
        return self.__name
