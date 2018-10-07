import numpy as np


class TestData:
    def __init__(self, input_file_path: str, mmap_mode: str = 'r'):
        self._ndarray = np.load(file=input_file_path, mmap_mode=mmap_mode)

    @property
    def shape(self):
        return self._ndarray.shape

    @property
    def nbytes(self):
        return self._ndarray.nbytes

    @property
    def data(self):
        return self._ndarray.data

    def get_element(self, index: int, window_size: int = 0) -> np.array:
        if window_size <= 1:
            return self._ndarray[index]
        else:
            return self._ndarray[index:index + window_size]
