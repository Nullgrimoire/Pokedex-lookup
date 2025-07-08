# 🧭 Pokédex Lookup CLI

Welcome to the **Pokédex Lookup CLI**, a simple but powerful terminal tool built by two passionate Pokémon fans — perfect for searching Pokémon data like types and evolution chains, directly from your terminal.

---

## 📦 Features

- 🔍 Search Pokémon by name  
- 📜 View Type (with Type1/Type2 combined)  
- 🔗 See full Evolution Chains  
- 📁 Backed by a JSON-based Pokédex database  
- 🧼 Includes a cross-platform console clear tool

---

## 🚀 How to Use

### 1. Clone the repo

```bash
git clone https://github.com/your-username/pokedex-cli.git
cd pokedex-cli
```

### 2. Run the CLI

```bash
python main.py
```

---

## 🧠 Project Structure

```plaintext
.
├── main.py              # Main CLI script
├── pokedex.json         # Pokémon data (Dex, Type, Evolution)
├── utils/
│   └── tools.py         # Utility functions like clear_console()
└── README.md            # This file
```

---

## 🔧 Sample JSON Format

```json
{
  "Pikachu": {
    "dex": 25,
    "Type": "Electric",
    "Evolution": "Pichu --> Pikachu --> Raichu"
  }
}
```

---

## 📚 Example Output

```
Welcome to Pokedex Lookup :)

Options:
1. Search Pokémon
2. List All
3. Exit

> 1
Enter Desired Pokemon: bulbasaur

Bulbasaur, I choose you!
No. 1
Type: Grass/Poison
Evolution: Bulbasaur --> Ivysaur --> Venusaur
```

---

## ✨ Credits

Built with ❤️ by  
**Nullgrimoire** & **Racer1428**

---

## 🧪 Ideas to Expand

- Filter by Generation or Type
- Add move sets or stats
- Use colorized terminal output (`rich` or `colorama`)
- Web or GUI version

---

## 🔗 License

MIT — free to use, modify, and catch 'em all.