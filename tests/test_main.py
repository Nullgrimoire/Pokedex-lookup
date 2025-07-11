import os
import sys
import io
import json
import pytest
from unittest.mock import patch

# Import functions from main.py
from pokedexcli.main import load_pokedex, lookup_pokemon, print_pokemon_info

@pytest.fixture(scope="module")
def example_pokedex():
    return load_pokedex()

def test_load_pokedex_success(example_pokedex):
    assert isinstance(example_pokedex, dict)
    assert 'Pikachu' in example_pokedex
    assert example_pokedex['Pikachu']['dex'] == 25

def test_lookup_pokemon_found(example_pokedex):
    pokemon = lookup_pokemon(example_pokedex, 'Pikachu')
    assert pokemon is not None
    assert pokemon['dex'] == 25
    assert 'Electric' in pokemon['Type']
    assert 'Pichu' in pokemon['Evolution']

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
    assert 'Pikachu, I choose you!' in captured.out
    assert '25' in captured.out
    assert 'Electric' in captured.out
    assert 'Pichu' in captured.out