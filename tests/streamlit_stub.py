class SessionState(dict):
    def clear(self):
        super().clear()

session_state = SessionState()

class Sidebar:
    def write(self, *args, **kwargs):
        pass

    def button(self, *args, **kwargs):
        return False

    def text_input(self, *args, **kwargs):
        return ""

sidebar = Sidebar()



def set_page_config(*args, **kwargs):
    pass



def info(*args, **kwargs):
    pass


def button(*args, **kwargs):
    return False


class Placeholder:
    def empty(self):
        pass


def empty(*args, **kwargs):
    return Placeholder()


def columns(n):
    return [Sidebar() for _ in range(n)]


def image(*args, **kwargs):
    pass


def title(*args, **kwargs):
    pass


def markdown(*args, **kwargs):
    pass


def caption(*args, **kwargs):
    pass


def subheader(*args, **kwargs):
    pass


def write(*args, **kwargs):
    pass

