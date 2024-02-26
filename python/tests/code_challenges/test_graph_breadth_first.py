import pytest
from data_structures.graph import Graph


def test_exists():
    assert Graph


def test_bfs(graph):
    nodes = graph.get_nodes()
    root = nodes[0]
    print(root.value)
    actual = graph.breadth_first(root)
    expected = ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]
    assert actual == expected

    # DANGER: Metroville/Monstropolis could be switched as well as Narnia/Naboo and still be valid BFS. What to do?

def test_bfs_single_node(graph):
    solitary = graph.add_node("Solitary")

    actual = graph.breadth_first(solitary)
    expected = ["Solitary"]
    assert actual == expected, "BFS on a graph with a single node should return just that node."

def test_bfs_disconnected_components(graph):
    isolated = graph.add_node("Isolated")

    nodes = graph.get_nodes()
    root = nodes[0]
    actual = graph.breadth_first(root)

    assert "Isolated" not in actual, "BFS should not visit disconnected components."

def test_bfs_with_cycles(graph):

    nodes = graph.get_nodes()
    root = nodes[0]

    actual = graph.breadth_first(root)
    visited_once = set(actual)

    assert len(actual) == len(visited_once), "BFS should visit each node exactly once, even in graphs with cycles."



@pytest.fixture
def graph():

    realms = Graph()

    pandora = realms.add_node("Pandora")
    arendelle = realms.add_node("Arendelle")
    metroville = realms.add_node("Metroville")
    monstropolis = realms.add_node("Monstropolis")
    narnia = realms.add_node("Narnia")
    naboo = realms.add_node("Naboo")

    realms.add_edge(pandora, arendelle)

    realms.add_edge(arendelle, pandora)
    realms.add_edge(arendelle, metroville)
    realms.add_edge(arendelle, monstropolis)

    realms.add_edge(metroville, arendelle)
    realms.add_edge(metroville, monstropolis)
    realms.add_edge(metroville, narnia)

    realms.add_edge(monstropolis, arendelle)
    realms.add_edge(monstropolis, metroville)
    realms.add_edge(monstropolis, naboo)

    realms.add_edge(narnia, metroville)
    realms.add_edge(narnia, naboo)

    realms.add_edge(naboo, metroville)
    realms.add_edge(naboo, monstropolis)
    realms.add_edge(naboo, narnia)

    return realms
