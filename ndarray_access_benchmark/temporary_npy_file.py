import tempfile
import numpy as np
import os
import uuid
import shutil


class TemporaryNpyFile:
    def __init__(self, shape: tuple):
        self._shape = shape
        self._file_exists = True

        self._store_directory = tempfile.mkdtemp()
        temporary_npy_file_name = f'{uuid.uuid4()}.npy'
        self._npy_file_path = os.path.join(self._store_directory, temporary_npy_file_name)

        print(f'generating and saving ndarray... shape: {shape}, path: {self._npy_file_path}')
        np.save(self._npy_file_path, np.random.rand(*shape))

    @property
    def npy_file_path(self):
        return self._npy_file_path

    def delete_file(self):
        shutil.rmtree(self._store_directory)
        self._file_exists = False
