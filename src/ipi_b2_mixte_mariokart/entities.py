from math import sqrt, pow

class Vehicule:
    def __init__(self, id: str, name: str, type: str, max_speed: int, acceleration: int):
        self.__id: str = id
        self.__name: str = name
        self.__type: str = type
        self.__max_speed: int = max_speed
        self.__acceleration: int = acceleration

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def type(self) -> str:
        return self.__type

    @property
    def max_speed(self) -> int:
        return self.__max_speed

    @property
    def acceleration(self) -> int:
        return self.__acceleration

class Character:
    def __init__(self, id: str, name: str, weight: int):
        self.__id: str = id
        self.__name: str = name
        self.__weight: int = weight
    
    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def weight(self) -> int:
        return self.__weight

class Coordinates:
    def __init__(self, x: int, y: int):
        self.__x: int = x
        self.__y: int = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

class Race:
    def __init__(self, id: str, name: str, laps_number: int, route: list[Coordinates]):
        self.__id: str = id
        self.__name: str = name
        self.__laps_number: int = laps_number
        self.__route: list[Coordinates] = route
    
    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def laps_number(self) -> int:
        return self.__laps_number

    @property
    def route(self) -> list[Coordinates]:
        return self.__route

    def compute_vector_distance(self, start: Coordinates, end: Coordinates) -> float:
        return sqrt( pow(end.x - start.x, 2) + pow(end.y - start.y, 2) )
    
    def compute_distance(self) -> float:
        points = self.__route + [self.__route[0]]
        return sum(self.compute_vector_distance(a, b)
                       for a, b in zip(points, points[1:]))

    def __repr__(self) -> str:
        return f"Race(id={self.__id}, name={self.__name}, laps_number={self.__laps_number}, route={self.__route})"