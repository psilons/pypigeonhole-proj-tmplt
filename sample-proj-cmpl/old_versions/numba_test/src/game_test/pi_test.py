import random

import time
from numba import jit


# @jit(nopython=True)
def estimate_pi(num_tesets):
    in_cycles = in_squares = 0

    for i in range(num_tesets):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        d = x * x + y * y

        in_squares += 1
        if d <= 1:
            in_cycles += 1

    return 4 * in_cycles / in_squares


start = time.time()
print(estimate_pi(10 ** 8))
end = time.time()
print(end - start)
# with njit, it take 1.53 seconds. Without it, it takes 100 seconds
