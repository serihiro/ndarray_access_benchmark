from time import time
import random
from ndarray_access_benchmark.test_data import TestData


class RandomAccess:
    @classmethod
    def run(cls, data: TestData, sampling_count: int, window_size: int = 1,) -> list:
        result = []
        max_index = data.shape[0] - 1 - (window_size - 1)

        for i in range(sampling_count):
            index = random.randint(0, max_index)
            start = time() * 1000
            data.get_element(index=index, window_size=window_size)
            end = time() * 1000
            elapsed_time = end - start
            result.append([i, index, elapsed_time])

        return result
