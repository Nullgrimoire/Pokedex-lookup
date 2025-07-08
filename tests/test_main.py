import os
import sys
import io
import json
import pytest

# Import functions from main.py
from main import load_pokedex, lookup_pokemon

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

def test_lookup_pokemon_found(example_pokedex, capsys):
    lookup_pokemon(example_pokedex, 'Pikachu')
    captured = capsys.readouterr()
    assert 'Pikachu, I choose you!' in captured.out
    assert 'No. 25' in captured.out
    assert 'Type: Electric' in captured.out
    assert 'Evolution: Pichu --> Pikachu --> Raichu' in captured.out

def test_lookup_pokemon_not_found(example_pokedex, capsys):
    lookup_pokemon(example_pokedex, 'Missingno')
    captured = capsys.readouterr()
    assert 'Missingno not found' in captured.out

def test_lookup_pokemon_case_insensitive(example_pokedex, capsys):
    lookup_pokemon(example_pokedex, 'pikachu')
    captured = capsys.readouterr()
    assert 'Pikachu, I choose you!' in captured.out 