"""
Simple Pokémon Pokédex Lookup Tool

This script allows users to search for Pokémon information stored in a JSON file.
It displays Dex number, type, and evolution chain, and includes a menu interface.

Author: [Nullgrimoire and Racer1428]
"""

import json
from typing import Dict, Any, Optional
from utils.tools import clear_console
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

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
        console.print(f"[bold yellow]Warning:[/] {filename} not found. Returning empty Pokédex.")
        return {}
    except json.JSONDecodeError:
        console.print(f"[bold red]Error:[/] {filename} is not a valid JSON file. Returning empty Pokédex.")
        return {}

def print_pokemon_info(name: str, pokemon: Dict[str, Any]) -> None:
    """
    Print formatted information about a Pokémon.

    Args:
        name (str): The name of the Pokémon.
        pokemon (dict): The Pokémon's data.
    """
    panel_title = f"[bold green]{name}, I choose you![/]"
    table = Table(show_header=False, box=None)
    table.add_row("[bold cyan]No.[/]", f"{pokemon.get('dex', 'N/A')}")
    table.add_row("[bold magenta]Type:[/]", f"{pokemon.get('Type', 'Unknown')}")
    table.add_row("[bold yellow]Evolution:[/]", f"{pokemon.get('Evolution', 'Unknown')}")
    console.print(Panel(table, title=panel_title, expand=False, border_style="green"))

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
    table = Table(title="Pokémon in Pokédex", show_header=False, box=None, title_style="bold blue")
    for name in sorted(pokedex):
        table.add_row(f"[white]-[/] [bold]{name}[/]")
    console.print(table)

def menu() -> None:
    """
    Display the main menu and handle user input.
    """
    pokedex = load_pokedex()
    
    # Uncomment the next line to clear the console each loop
    clear_console()
    
    console.print("[bold blue]Welcome to Pokedex Lookup :)[/bold blue]\n")

    while True:
        console.print("[bold]Options:[/bold]")
        console.print("\n[cyan]1.[/] Search Pokémon\n[cyan]2.[/] List All\n[cyan]3.[/] Exit")

        choice = console.input("[bold yellow]> [/]").strip()

        if choice == "1":
            name = console.input("[bold]Enter Desired Pokemon:[/] ").strip()
            if not name:
                console.print("[red]Please enter a Pokémon name.[/]")
                continue
            pokemon = lookup_pokemon(pokedex, name)
            if pokemon:
                print_pokemon_info(name.title(), pokemon)
            else:
                console.print(f"[red]{name.title()} not found...[/]")
        elif choice == "2":
            list_all_pokemon(pokedex)
        elif choice == "3":
            console.print("[bold magenta]Goodbye... :([/]")
            break
        else:
            console.print("[red]Please choose 1, 2, or 3.[/]")

def main() -> None:
    """
    Entry point for the Pokédex application.
    """
    menu()

if __name__ == "__main__":
    main()
