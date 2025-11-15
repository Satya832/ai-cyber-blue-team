import threading
from typing import Callable, Dict, List, Any

class EventBus:
    def __init__(self):
        self._subs: Dict[str, List[Callable[[Any], None]]] = {}
        self._lock = threading.Lock()

    def subscribe(self, topic: str, handler):
        with self._lock:
            self._subs.setdefault(topic, []).append(handler)

    def publish(self, topic: str, message: Any):
        with self._lock:
            handlers = self._subs.get(topic, []).copy()
        for h in handlers:
            try:
                h(message)
            except Exception as e:
                print(f"[EventBus] error: {e}")
