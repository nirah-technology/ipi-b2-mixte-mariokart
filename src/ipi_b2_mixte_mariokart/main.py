from pathlib import Path

from .entities import Vehicule, Character, Coordinates, Race
from .repositories import VehiclesRepository
from .servers import MarioKartServer


def main():
    characters = [
        Character(1, "Mario", 50),
        Character(2, "Yoshi", 50),
        Character(3, "Luigi", 50),
        Character(4, "Peach", 50),
        Character(5, "Daisy", 50),
        Character(6, "Waluigi", 50),
        Character(7, "Toad", 25),
        Character(8, "Donkey-Kong", 100),
        Character(9, "Wario", 100),
        Character(10, "Bowser", 100),
    ]

    vehicules = [
        Vehicule(1, "Mario Kart", "KART", 75, 75),
        Vehicule(2, "Yoshi Moto", "MOTO", 50, 100),
        Vehicule(3, "Wario Car", "CAR", 100, 50),
    ]

    races = [
        Race(1, "Mario Kart Circuit", 3, [
            Coordinates(0, 0),
            Coordinates(0, 10),
            Coordinates(0, 20),
            Coordinates(0, 30),
            Coordinates(10, 30),
            Coordinates(10, 20),
            Coordinates(10, 20),
            Coordinates(10, 10),
            Coordinates(10, 0)
        ]),
        Race(2, "Circuit Arc-En-Ciel", 3, [
            Coordinates(0, 0),
            Coordinates(0, 10),
            Coordinates(0, 20),
            Coordinates(10, 20),
            Coordinates(10, 10),
            Coordinates(10, 0)]),
        Race(3, "Montagne DK", 3, [
            Coordinates(0, 0),
            Coordinates(0, 10),
            Coordinates(10, 10),
            Coordinates(10, 0)])
    ]

    for character in characters:
        print(character)

    vehicules_repository = VehiclesRepository("mariokart.db")
    vehicules_repository.initialize(Path("vehicules.sql"))

    for vehicule in vehicules:
        # Vérifier si le véhicule existe dans la BDD
        vehicule_found = vehicules_repository.find_by_id(vehicule.id)
        if (vehicule_found is None):
            # S'il n'éxiste pas, il faut le créer dans la BDD.
            vehicules_repository.create(vehicule)

        print(vehicule)

    for race in races:
        print(race)

    server = MarioKartServer("0.0.0.0", 3000)
    server.start()

if (__name__ == "__main__"):
    main()