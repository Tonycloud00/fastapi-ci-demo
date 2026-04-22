
class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, item: str):
        self.todos.append(item)

    def get_all(self):
        return self.todos
