from datetime import datetime

import time


# type custom_time
class custom_time:
    def __init__(self, input_time: float = None):
        if not input_time:
            input_time = time.time()
        self.time = input_time

    def __repr__(self):
        return str(datetime.fromtimestamp(self.time))

    def __str__(self):
        return str(datetime.fromtimestamp(self.time))

    def __eq__(self, eq_to: float):
        return self.time == eq_to

    def __ge__(self, ge_to: float):
        return self.time >= ge_to

    def __gt__(self, gt_to: float):
        return self.time > gt_to

    def __lt__(self, lt_to: float):
        return self.time <= lt_to

    def __le__(self, le_to: float):
        return self.time < le_to

    def __ne__(self, ne_to: float):
        return self.time != ne_to


def timer(time_from: custom_time, period: custom_time) -> bool:
    # returns True if time from more than period
    return time_from.time + period >= time_from.time + time.time()
