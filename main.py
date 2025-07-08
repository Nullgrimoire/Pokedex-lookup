"""
Simple Pokémon Pokédex Lookup Tool

This script allows users to search for Pokémon information stored in a JSON file.
It displays Dex number, type, and evolution chain, and includes a menu interface.

Author: [Nullgrimoire and Racer1428]
"""

import json
from typing import Dict, Any, Optional
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
    except json.JSONDecodeError:
        print(f"Error: {filename} is not a valid JSON file. Returning empty Pokédex.")
        return {}

def print_pokemon_info(name: str, pokemon: Dict[str, Any]) -> None:
    """
    Print formatted information about a Pokémon.

    Args:
        name (str): The name of the Pokémon.
        pokemon (dict): The Pokémon's data.
    """
    print(f"\n{name}, I choose you!")
    print(f"No. {pokemon.get('dex', 'N/A')}")
    print(f"Type: {pokemon.get('Type', 'Unknown')}")
    print(f"Evolution: {pokemon.get('Evolution', 'Unknown')}")

def lookup_pokemon(pokedex: Dict[str, Any], name: str) -> Optional[Dict[str, Any]]:
    """
    Look up a Pokémon by name.

    Args:
        pokedex (dict): The Pokédex dictionary.
        name (str): The name of the Pokémon to look up.

    Returns:
        dict or None: The Pokémon's data if found, else None.
    """
    return pokedex.get(name.title())

def list_all_pokemon(pokedex: Dict[str, Any]) -> None:
    """
    Print all Pokémon names in the Pokédex, sorted alphabetically.

    Args:
        pokedex (dict): The Pokédex dictionary.
    """
    print("\nPokémon in Pokédex:")
    for name in sorted(pokedex):
        print(f"- {name}")

def menu() -> None:
    """
    Display the main menu and handle user input.
    """
    pokedex = load_pokedex()
    print("Welcome to Pokedex Lookup :) \n")
    # Uncomment the next line to clear the console each loop
    clear_console()
    while True:

        print("Options:")
        print("\n1. Search Pokémon\n2. List All\n3. Exit")

        choice = input("> ").strip()

        if choice == "1":
            name = input("Enter Desired Pokemon: ").strip()
            if not name:
                print("Please enter a Pokémon name.")
                continue
            pokemon = lookup_pokemon(pokedex, name)
            if pokemon:
                print_pokemon_info(name.title(), pokemon)
            else:
                print(f"\n{name.title()} not found...")
        elif choice == "2":
            list_all_pokemon(pokedex)
        elif choice == "3":
            print("Goodbye... :(")
            break
        else:
            print("Please choose 1, 2, or 3.")

def main() -> None:
    """
    Entry point for the Pokédex application.
    """
    menu()

if __name__ == "__main__":
    main()
