from typing import Tuple, List


class EventBroker:

    def __init__(self):
        self.subscriptions: List[Tuple[type, callable]] = []

    def subscribe(self, handler, instance_type):
        self.subscriptions.append((instance_type, handler))

    def publish_event(self, event):
        handlers_for_event = self._get_subscribers_for_event(event)
        [handler() for _, handler in handlers_for_event]

    def _get_subscribers_for_event(self, event):
        return filter(lambda x: x[0] == type(event), self.subscriptions)
