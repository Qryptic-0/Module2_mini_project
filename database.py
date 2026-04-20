from datetime import datetime

class InMemoryDB:
    def __init__(self):
        self.users = {}
        self.projects = {}
        self.tasks = {}
        self._user_id_counter = 1
        self._project_id_counter = 1
        self._task_id_counter = 1

db = InMemoryDB()

