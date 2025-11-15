COUNTERS = {}

class Telemetry:
    def increment(self, k):
        COUNTERS[k] = COUNTERS.get(k, 0) + 1

    def snapshot(self):
        return COUNTERS
