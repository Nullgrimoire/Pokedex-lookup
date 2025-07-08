"""
Simple Pokémon Pokédex Lookup Tool

This script allows users to search for Pokémon information stored in a JSON file.
It displays Dex number, type, and evolution chain, and includes a menu interface.

Author: [Nullgrimoire and Racer1428]
"""

import json
from typing import Dict, Any
from utils.tools import clear_console

def load_pokedex(filename: str = "pokedex/pokedex.json") -> Dict[str, Any]:
    """
    Load the Pokédex data from a JSON file.

    Args:
        filename (str): The name of the JSON file to load. Defaults to 'pokedex/pokedex.json'.

    Returns:
        dict: A dictionary containing Pokémon data, keyed by Pokémon name.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Returning empty Pokédex.")
        return {}

def lookup_pokemon(pokedex: Dict[str, Any], name: str) -> None:
    """
    Look up a Pokémon by name and print its information.

    Args:
        pokedex (dict): The Pokédex dictionary.
        name (str): The name of the Pokémon to look up.
    """
    pokemon = pokedex.get(name.title())
    if pokemon:
        print(f"\n{name.title()}, I choose you!")
        print(f"No. {pokemon.get('dex', 'N/A')}")
        print(f"Type: {pokemon.get('Type', 'Unknown')}")
        print(f"Evolution: {pokemon.get('Evolution', 'Unknown')}")
    else:
        print(f"\n{name.title()} not found...")

def main() -> None:
    """
    Main function to run the Pokédex menu interface.
    Allows users to search for Pokémon, list all Pokémon, or exit the app.
    """
    pokedex = load_pokedex()
    print("Welcome to Pokedex Lookup :) \n")

    while True:
        # clear_console()
        print("Options: ")
        print("\n1. Search Pokémon\n2. List All\n3. Exit")
        
        choice = input("> ").strip()

        if choice == "1":
            name = input("Enter Desired Pokemon: ").strip()
            if not name:
                print("Please enter a Pokémon name.")
                continue
            lookup_pokemon(pokedex, name)
        elif choice == "2":
            print("\n Pokémon in Pokedex:")
            for name in sorted(pokedex):
                print(f"- {name}")
        elif choice == "3":
            print("Goodbye... :(")
            break
        else:
            print("Please choose 1, 2, or 3")

if __name__ == "__main__":
    main()
