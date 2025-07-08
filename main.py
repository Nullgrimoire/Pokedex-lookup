import json

def load_pokedex(filename="pokedex.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def lookup_pokemon(pokedex, name):
    pokemon = pokedex.get(name.title())
    if pokemon:
        print(f"\n{name.title()}, I choose you!")
        print(f"No. {pokemon['dex']}")
    else:
        print(f"\n{name.title()} not found...")

def main():
    pokedex = load_pokedex()
    print("Welcome to Pokedex Lookup :) \n")

    while True:
        print("\n1. Search Pokémon\n2. List All\n3. Exit")
        
        choice = input("> ")

        if choice == "1":
            name = input("Enter Desired Pokemon: ")
            lookup_pokemon(pokedex, name)
        elif choice == "2":
            print("\n Pokemon in Pokedex:")
            for name in pokedex:
                print(f"- {name}")
        elif choice == "3":
            print("Goodbye... :(")
            break
        else:
            print("Please choose 1, 2, or 3")

if __name__ == "__main__":
    main()