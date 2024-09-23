import time
from collections import defaultdict
from threading import Lock


# Sliding Window Log algorithm for rate limit
class SlidingWindowRateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_requests = defaultdict(list)
        self.lock = Lock()

    def allow_request(self, user_id):
        current_time = time.time()

        with self.lock:
            valid_requests = []
            for req_time in self.user_requests[user_id]:
                if current_time - req_time < self.time_window:
                    valid_requests.append(req_time)

            self.user_requests[user_id] = valid_requests

            if len(self.user_requests[user_id]) < self.max_requests:
                self.user_requests[user_id].append(current_time)
                return True
            else:
                return False


rate_limiter = SlidingWindowRateLimiter(max_requests=5, time_window=60)
user_id = "user_123"

for i in range(6):
    if rate_limiter.allow_request(user_id):
        print(f"Request {i + 1} allowed")
    else:
        print(f"Request {i + 1} denied")

    time.sleep(10)
