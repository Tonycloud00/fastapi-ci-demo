from app.todo import TodoList

def test_add():
    t = TodoList()
    t.add("apple")
    assert "apple" in t.get_all()

def test_multiple():
    t = TodoList()
    t.add("A")
    t.add("B")
    assert t.get_all() == ["A", "B"]

"""
from app.todo import TodoList

def test_add_item():
    t = TodoList()
    t.add("apple")
    assert "apple" in t.get_all()

def test_multiple_items():
    t = TodoList()
    t.add("A")
    t.add("B")
    assert t.get_all() == ["A", "B"]
"""