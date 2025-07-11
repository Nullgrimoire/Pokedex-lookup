# 🧭 Pokédex Lookup CLI

Welcome to the **Pokédex Lookup CLI**, a simple but powerful terminal tool built by two passionate Pokémon fans — perfect for searching Pokémon data like types and evolution chains, directly from your terminal.

---

## 📦 Features

- 🔍 Search Pokémon by name  
- 📜 View Type (with Type1/Type2 combined)  
- 🔗 See full Evolution Chains  
- 💾 Uses a SQLite database for fast lookups  
- 🧼 Includes a cross-platform console clear tool
- 🧪 Includes unit tests for core logic (see below)
- 📝 Type hints and improved docstrings for maintainability

---

## 🚀 How to Use

### 1. Clone the repo

```bash
git clone https://github.com/Nullgrimoire/Pokedex-lookup.git
cd Pokedex-lookup
```

### 2. Install requirements

```bash
pip install --user -r requirements.txt
```

### 3. Run the CLI

```bash
python3 -m pokedexcli
```

---

## 🧪 Running Tests

This project uses `pytest` for unit testing. To run the tests:

```bash
pytest
```

Tests are located in the `tests/` directory and cover core logic such as Pokédex loading and Pokémon lookup.

---

## 🧠 Project Structure

```plaintext
.
├── pokedex.db              # SQLite database
├── pokedexcli/             # Main application package
│   ├── __init__.py
│   ├── main.py             # CLI entry point
│   └── utils.py            # Utility functions (clear_console, etc.)
├── tests/                  # Unit tests for core logic
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt        # Python dependencies
└── README.md               # This file
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
- Use colorized terminal output (`rich`)
- Web or GUI version

---

## 🔗 License

MIT — free to use, modify, and catch 'em all.
