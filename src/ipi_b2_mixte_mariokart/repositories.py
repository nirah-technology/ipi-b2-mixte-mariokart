import sqlite3

from pathlib import Path
from typing import Optional

from .entities import Vehicule, Character, Coordinates, Race

class VehiclesRepository:
    def __init__(self, database_file: Path):
        self.__database_file: Path = database_file
    
    def create(self, vehicule: Vehicule):
        with sqlite3.connect(self.__database_file) as sql_connection:
            try:
                sql_connection.execute(
                    """
                    INSERT INTO vehicules (id, name, type, max_speed, acceleration)
                    VALUES (?, ?, ?, ?, ?)""",
                    (
                        vehicule.id, 
                        vehicule.name, 
                        vehicule.type, 
                        vehicule.max_speed, 
                        vehicule.acceleration
                    )
                )
            except:
                print("Il y a un probleme avec l'éxécution de la requete SQL pour sauvegarder le véhicule")
                sql_connection.rollback()
            else:
                sql_connection.commit()
        
    def delete(self, vehicule: Vehicule):
        with sqlite3.connect(self.__database_file) as sql_connection:
            try:
                sql_connection.execute(
                    """
                    DELETE FROM vehicules WHERE id = ?""",
                    (
                        vehicule.id,
                    )
                )
            except:
                print("Il y a un probleme avec l'éxécution de la requete SQL pour supprimer le véhicule")
                sql_connection.rollback()
            else:
                sql_connection.commit()
        
    def update(self, vehicule: Vehicule):
        with sqlite3.connect(self.__database_file) as sql_connection:
            try:
                sql_connection.execute(
                    """
                    UPDATE vehicules 
                    SET name = ?, type = ?, max_speed = ?, acceleration = ?
                    WHERE id = ?""",
                    (
                        vehicule.name, 
                        vehicule.type, 
                        vehicule.max_speed, 
                        vehicule.acceleration,
                        vehicule.id
                    )
                )
            except:
                print("Il y a un probleme avec l'éxécution de la requete SQL pour mettre à jour le véhicule")
                sql_connection.rollback()
            else:
                sql_connection.commit()

    def __map_row_to_vehicule(self, row: dict) -> Vehicule:
        return Vehicule(
                    id=row["id"],
                    name=row["name"],
                    type=row["type"],
                    max_speed=row["max_speed"],
                    acceleration=row["acceleration"]
                )

    def find_by_id(self, vehicle_id: str) -> Optional[Vehicule]:
        vehicle_found: Vehicule|None = None
        with sqlite3.connect(self.__database_file) as sql_connection:
            sql_connection.row_factory = sqlite3.Row
            cursor = sql_connection.execute("""
                SELECT id, name, type, max_speed, acceleration
                FROM vehicules 
                WHERE id = ?
            """, (vehicle_id,))
            row = cursor.fetchone()
            if row is not None:
                vehicle_found = self.__map_row_to_vehicule(row)
        return vehicle_found

    def find_all(self) -> list[Vehicule]:
        vehicles_found: list[Vehicule] = []
        with sqlite3.connect(self.__database_file) as sql_connection:
            cursor = sql_connection.execute("""
                SELECT id, name, type, max_speed, acceleration
                FROM vehicules
            """)
            rows = cursor.fetchall()
            for row in rows:
                vehicule = self.__map_row_to_vehicule(row)
                vehicles_found.append(vehicule)

        return vehicles_found

    def initialize(self, sql_script_file: Path):
        with sqlite3.connect(self.__database_file) as sql_connection:
            sql_connection.executescript(sql_script_file.read_text())
            sql_connection.commit()
    
    