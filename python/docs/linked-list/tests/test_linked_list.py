import pytest
from linked_list.linked_list_cli import LinkedList, EmptyListError


def test_instantiate_empty_list():
    linked_list = LinkedList()
    assert linked_list.head is None

def test_insert_into_linked_list():
    linked_list = LinkedList()
    linked_list.insert(1)
    assert linked_list.head.value == 1

def test_head_points_to_first_node():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    assert linked_list.head.value == 2

def test_insert_multiple_nodes():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    assert linked_list.head.value == 2
    assert linked_list.head.next.value == 1

def test_find_value_exists():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    assert linked_list.includes(2)

def test_find_value_not_exists():
    linked_list = LinkedList()
    linked_list.insert(1)
    assert not linked_list.includes(3)

def test_return_all_values():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    assert linked_list.to_string() == "{ 2 } -> { 1 } -> NULL"

def test_get_first_from_empty_list():
    linked_list = LinkedList()
    with pytest.raises(EmptyListError):
        linked_list.get_first()
