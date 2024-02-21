import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join

def test_left_join():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected
    
def test_right_join():
    legit = {
        "BASED": "Genuine",
        "Chill": "Calm",
    }
    hoax = {
        "BASED": "pretentious",
        "Chill": "Tense",
    }

    expected = [
        ["BASED", "pretentious", "Genuine"],
        ["Chill", "Tense", "Calm"],
    ]

    actual = left_join(legit, hoax, join='right')

    assert actual == expected
    
def test_empty_hash():
    nothing = {}
    
    actual = left_join(nothing, nothing)
    
    assert actual == []
    
def test_left_join_no_keys():
    empty1 = {}
    empty2 = {}
    with pytest.raises(AssertionError):
        assert left_join(empty1, empty2) != []
    

def test_left_join_with_incorrect_types():
    with pytest.raises(TypeError):
        left_join(["not", "a", "dict"], {"this": "is a dict"})