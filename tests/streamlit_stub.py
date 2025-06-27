class SessionState(dict):
    def clear(self):
        super().clear()

session_state = SessionState()

class Sidebar:
    def write(self, *args, **kwargs):
        pass

sidebar = Sidebar()

# capture error messages for assertions
errors = []


def set_page_config(*args, **kwargs):
    pass


def error(message):
    errors.append(message)


def stop():
    raise RuntimeError("stop")
