class SessionState(dict):
    def clear(self):
        super().clear()

session_state = SessionState()

class Sidebar:
    def write(self, *args, **kwargs):
        pass

sidebar = Sidebar()
