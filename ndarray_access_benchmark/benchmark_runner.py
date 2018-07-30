from ndarray_access_benchmark.benchmarks.random_access import RandomAccess
import numpy as np
import csv

RANDOM_ACCESS = 'random_access'
CSV_HEADER = ['id', 'accessed_index', 'elapsed_time']


class BenchmarkRunner:
    def __init__(self, data: np.array, window_size: int, sampling_count: int, result_path: str, result_format: str):
        self._data = data
        self._window_size = window_size
        self._sampling_count = sampling_count
        self._result_path = result_path
        self._result_format = result_format

    def run_random_access(self):
        self.run_benchmark(benchmark_type=RANDOM_ACCESS)

    def run_benchmark(self, benchmark_type: str):
        if benchmark_type == RANDOM_ACCESS:
            result = RandomAccess.run(data=self._data, sampling_count=self._sampling_count,
                                      window_size=self._window_size)
        else:
            raise ValueError(f'Invalid benchmark_type: {benchmark_type}')

        self.__output_result(result)

    def __output_result(self, result: list):
        with open(self._result_path, 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(CSV_HEADER)
            for value in result:
                writer.writerow(value)
