"""
Simple Pokémon Pokédex Lookup Tool

This script allows users to search for Pokémon information stored in a SQLite database.
It displays Dex number, type, and evolution chain, and includes a menu interface.

Author: [Nullgrimoire and Racer1428]
"""

import sqlite3
from typing import Dict, Any, Optional
from .utils import clear_console
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

DB_PATH = "pokedex.db"

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def load_pokedex():
    """
    Load all Pokémon from the SQLite database.
    Returns:
        dict: {name: {dex, Type, Evolution}}
    """
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT name, dex, Type, Evolution FROM pokemon")
    pokedex = {row[0]: {"dex": row[1], "Type": row[2], "Evolution": row[3]} for row in c.fetchall()}
    conn.close()
    return pokedex

def print_pokemon_info(name: str, pokemon: Dict[str, Any]) -> None:
    panel_title = f"[bold green]{name}, I choose you![/]"
    table = Table(show_header=False, box=None)
    table.add_row("[bold cyan]No.[/]", f"{pokemon.get('dex', 'N/A')}")
    table.add_row("[bold magenta]Type:[/]", f"{pokemon.get('Type', 'Unknown')}")
    table.add_row("[bold yellow]Evolution:[/]", f"{pokemon.get('Evolution', 'Unknown')}")
    console.print(Panel(table, title=panel_title, expand=False, border_style="green"))

def lookup_pokemon(pokedex: Dict[str, Any], name: str) -> Optional[Dict[str, Any]]:
    return pokedex.get(name.title())

def list_all_pokemon(pokedex: Dict[str, Any]) -> None:
    table = Table(title="Pokémon in Pokédex", show_header=False, box=None, title_style="bold blue")
    for name in sorted(pokedex):
        table.add_row(f"[white]-[/] [bold]{name}[/]")
    console.print(table)

def menu() -> None:
    pokedex = load_pokedex()
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
    menu()

if __name__ == "__main__":
    main()
