from event_handlers.EventHandler import EventHandler


class GameOverHandler(EventHandler):

    def __init__(self, core, restart_handler):
        self.core = core
        self.restart_handler = restart_handler

    def handle(self):
        self.core.stop_token = True
        self.restart_handler()
