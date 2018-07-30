import argparse
import sys
from ndarray_access_benchmark.test_data import TestData
from ndarray_access_benchmark.temporary_npy_file import TemporaryNpyFile
from ndarray_access_benchmark.benchmark_runner import BenchmarkRunner
from memory_profiler import profile


class Cli:
    @profile
    def __init__(self, shape: tuple, sampling_count: int,
                 result_format: str, result_path: str,
                 mmap_mode: str = None,
                 input_path: str = None):
        self._shape = shape
        self._sampling_count = sampling_count
        self._mmap_mode = mmap_mode
        self._input_path = input_path
        self._result_path = result_path
        self._result_format = result_format

        if self._input_path is None:
            self._tmp_npy_file = TemporaryNpyFile(shape=shape)
            test_data = TestData(input_file_path=self._tmp_npy_file.npy_file_path, mmap_mode=self._mmap_mode)
        else:
            test_data = TestData(input_file_path=self._input_path, mmap_mode=self._mmap_mode)

        runner = BenchmarkRunner(data=test_data, sampling_count=self._sampling_count, result_path=self._result_path,
                                 result_format=self._result_format)
        runner.run_random_access()
        if self._tmp_npy_file is not None:
            self._tmp_npy_file.delete_file()

    def run(self):
        if self._input_path is None:
            self._tmp_npy_file = TemporaryNpyFile(shape=self._shape)
            test_data = TestData(input_file_path=self._tmp_npy_file.npy_file_path, mmap_mode=self._mmap_mode)
        else:
            test_data = TestData(input_file_path=self._input_path, mmap_mode=self._mmap_mode)

        runner = BenchmarkRunner(data=test_data, sampling_count=self._sampling_count, result_path=self._result_path,
                                 result_format=self._result_format)
        print('benchmark start')
        runner.run_random_access()
        print('benchmark finish')
        
        if self._tmp_npy_file is not None:
            self._tmp_npy_file.delete_file()
            print(f'{self._tmp_npy_file.npy_file_path} was deleted')


def main():
    if sys.version_info[:3] < (3, 5, 0):
        print('ndarray_access_benchmark requires python >= 3.5.0')
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument('--mmap_mode', '-m', type=str, default='r')
    parser.add_argument('--shape', '-s', type=int, nargs='+', default=[1000, 1000])
    parser.add_argument('--sampling_count', '-c', type=int, default=1000)
    parser.add_argument('--result_format', '-f', type=str, default='csv')
    parser.add_argument('--input_path', '-i', type=str)
    parser.add_argument('--result_path', '-r', type=str, default='./result.csv')
    args = parser.parse_args()
    print(f'mmap_mode: {args.mmap_mode}')
    print(f'shape: {args.shape}')
    print(f'sampling_count: {args.sampling_count}')
    print(f'result_format: {args.result_format}')
    print(f'input_path: {args.input_path}')
    print(f'result_path: {args.result_path}')

    c = Cli(shape=tuple(args.shape),
            sampling_count=args.sampling_count,
            mmap_mode=args.mmap_mode,
            input_path=args.input_path,
            result_path=args.result_path,
            result_format=args.result_format
            )
    c.run()


if __name__ == '__main__':
    main()
