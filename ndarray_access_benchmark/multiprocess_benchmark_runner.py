from ndarray_access_benchmark.benchmarks.random_access import RandomAccess
from ndarray_access_benchmark.benchmark_runner import BenchmarkRunner
import multiprocessing
import os
import numpy as np

RANDOM_ACCESS = 'random_access'
CSV_HEADER = ['id', 'accessed_index', 'elapsed_time']


class MultiProcessBenchmarkRunner(BenchmarkRunner):
    def __init__(self, data: np.array, window_size: int, sampling_count: int,
                 result_path: str, result_format: str, process_size: int):
        self._process_size = process_size
        super(MultiProcessBenchmarkRunner, self).__init__(data=data, window_size=window_size,
                                                          sampling_count=sampling_count,
                                                          result_path=result_path, result_format=result_format)

    def run_random_access(self):
        self.run_benchmark(benchmark_type=RANDOM_ACCESS)

    def run_benchmark(self, **kwargs):
        if kwargs['benchmark_type'] == RANDOM_ACCESS:
            benchmark = RandomAccess
        else:
            raise ValueError(f"Invalid benchmark_type: {kwargs['benchmark_type']}")

        processes = []
        for pid in range(self._process_size):
            process = multiprocessing.Process(target=self.__execute_benchmark_process, args=(benchmark, pid))
            process.start()
            processes.append(process)

        [process.join() for process in processes]

    def __execute_benchmark_process(self, benchmark, process_id):
        result = benchmark.run(data=self._data, sampling_count=self._sampling_count,
                               window_size=self._window_size)

        os.makedirs(self._result_path, exist_ok=True)
        output_path = os.path.join(self._result_path, f'result_{process_id}.csv')
        super()._BenchmarkRunner__output_result(result=result, output_path=output_path)
