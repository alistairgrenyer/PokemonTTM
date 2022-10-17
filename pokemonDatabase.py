import sqlite3
import pandas as pd


def databaseConnect():
    try:
        conn = sqlite3.connect('Pokemon.db')
        return conn
    except KeyError as e:
        print(e)


def createTable(conn: sqlite3.Connection):
    cursor = conn.cursor()
    try:
        createPokemonDatabase = '''
            CREATE TABLE "PokemonDatabase" (
            "Name"	TEXT,
            "Artwork"	TEXT,
            "Attack"	INTEGER,
            "Defence"	INTEGER,
            "Type1"	TEXT,
            "Type2"	TEXT
            );
            '''
        cursor.execute(createPokemonDatabase)
        conn.commit()
    except sqlite3.OperationalError as e:
        print(e)


def findPokemonFromName(conn: sqlite3.Connection, pokemonName: str):
    selectData = f'''
        SELECT * FROM PokemonDatabase
        WHERE PokemonDatabase.Name = "{pokemonName}"
        '''
    pokemonNameDataFrame = pd.read_sql_query(selectData, conn)
    if pokemonNameDataFrame.empty:
        return None
    else:
        return pokemonNameDataFrame
