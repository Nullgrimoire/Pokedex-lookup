import os
import sys
import io
import json
import pytest
from unittest.mock import patch

# Import functions from main.py
from main import load_pokedex, lookup_pokemon, print_pokemon_info

EXAMPLE_PATH = os.path.join(os.path.dirname(__file__), '../pokedex/pokedex_example.json')

@pytest.fixture
def example_pokedex():
    return load_pokedex(EXAMPLE_PATH)

def test_load_pokedex_success():
    pokedex = load_pokedex(EXAMPLE_PATH)
    assert isinstance(pokedex, dict)
    assert 'Pikachu' in pokedex
    assert pokedex['Pikachu']['dex'] == 25

def test_load_pokedex_file_not_found():
    pokedex = load_pokedex('nonexistent.json')
    assert pokedex == {}

def test_lookup_pokemon_found(example_pokedex):
    pokemon = lookup_pokemon(example_pokedex, 'Pikachu')
    assert pokemon is not None
    assert pokemon['dex'] == 25
    assert pokemon['Type'] == 'Electric'
    assert pokemon['Evolution'] == 'Pichu --> Pikachu --> Raichu'

def test_lookup_pokemon_not_found(example_pokedex):
    pokemon = lookup_pokemon(example_pokedex, 'Missingno')
    assert pokemon is None

def test_lookup_pokemon_case_insensitive(example_pokedex):
    pokemon = lookup_pokemon(example_pokedex, 'pikachu')
    assert pokemon is not None
    assert pokemon['dex'] == 25

def test_print_pokemon_info(example_pokedex, capsys):
    pokemon = example_pokedex['Pikachu']
    print_pokemon_info('Pikachu', pokemon)
    captured = capsys.readouterr()
    # Rich output includes ANSI color codes, so we check for key content
    assert 'Pikachu, I choose you!' in captured.out
    assert '25' in captured.out
    assert 'Electric' in captured.out
    assert 'Pichu --> Pikachu --> Raichu' in captured.out 