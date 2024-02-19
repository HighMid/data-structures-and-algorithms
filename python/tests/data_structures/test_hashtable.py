import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_hash():
    hashtable = Hashtable()
    actual = hashtable.hash("Zach")
    assert 0 <= actual < hashtable.size

def test_hash_twice():
    hashtable = Hashtable()
    first = hashtable.hash("Zach")
    second = hashtable.hash("Zach")
    assert first == second

def test_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_apple_again():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("apple", "Can give to teacher")
    actual = hashtable.get("apple")
    expected = "Can give to teacher"
    assert actual == expected

def test_key_not_exists():
    hashtable = Hashtable()
    actual = hashtable.get("nonexisting key")
    expected = None
    assert actual == expected

def test_key_not_exists_again():
    hashtable = Hashtable()
    hashtable.set("cat", "meow")
    actual = hashtable.get("act")  # Assuming "act" and "cat" do not hash to the same index intentionally
    expected = None
    assert actual == expected

def test_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Great in a banana split")
    actual = hashtable.keys()
    expected = ["apple", "banana"]
    assert sorted(actual) == sorted(expected)

def test_has():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Great in a banana split")
    assert hashtable.has("apple")
    assert hashtable.has("banana")
    assert not hashtable.has("cucumber")

def test_keys_repeats():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("apple", "Can give to teacher")
    hashtable.set("banana", "Great in a banana split")
    actual = hashtable.keys()
    expected = ["apple", "banana"]
    assert sorted(actual) == sorted(expected)
