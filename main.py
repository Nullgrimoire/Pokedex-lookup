def lookupPokemon(name):
    pokemon = pokedex.get(name.title())
    if pokemon:
        print(f"\n{name.title()}, I choose you!")
        print(f"No. {pokemon['dex']}")
    else:
        print(f"\n{name.title()} not found...")

def main():
    print("Welcome to Pokedex Lookup :) \n")

    while true:
        print("\n Options")
        print("1. Search for Pokemon")
        print("2. All Pokemon")
        print("3. Exit")
        
        choice = input("> ")

        if choice == "1":
            name = input("Enter Desired Pokemon: ")
            lookupPokemon(name)
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