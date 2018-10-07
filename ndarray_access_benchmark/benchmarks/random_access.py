from time import time
import random
from ndarray_access_benchmark.test_data import TestData


class RandomAccess:
    @classmethod
    def run(cls, data: TestData, sampling_count: int, nbytes: int, window_size: int = 1) -> list:
        result = []
        max_index = data.shape[0] - 1 - (window_size - 1)
        for i in range(sampling_count):
            index = random.randint(0, max_index)
            start = time()
            # load all elements from the ndarray
            data.get_element(index=index, window_size=window_size).tolist()
            end = time()

            # sec
            elapsed_time = end - start

            # MiB/sec
            throughput = (nbytes / (1024 ** 2)) / elapsed_time

            result.append([i, index, elapsed_time, nbytes, throughput])

        return result
