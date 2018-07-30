# ndarray access benchmark
- This benchmark measures how long it takes to load element from 
the ndarray which is loaded by numpy.load with `mmap_mode` option.
- In Numpy, if we call `numpy.load` with `mmap_mode` arguments except None, 
Numpy load npy file from disk into memory as `numpy.memmap` object.

# requirements
- python>=3.5.0

# how to use

```sh
git clone ndarray_access_benchmark
cd ndarray_access_benchmark
pip install .
nadm # or python ndarray_access_benchmark/cli.py
```

And then you can see `test.csv` to your current directory.

# options

```sh
$ nabm --help
usage: nabm [-h] [--mmap_mode MMAP_MODE] [--shape SHAPE [SHAPE ...]]
            [--window_size WINDOW_SIZE] [--sampling_count SAMPLING_COUNT]
            [--result_format RESULT_FORMAT] [--input_path INPUT_PATH]
            [--result_path RESULT_PATH]

optional arguments:
  -h, --help            show this help message and exit
  --mmap_mode MMAP_MODE, -m MMAP_MODE
  --shape SHAPE [SHAPE ...], -s SHAPE [SHAPE ...]
  --window_size WINDOW_SIZE, -ws WINDOW_SIZE
  --sampling_count SAMPLING_COUNT, -sc SAMPLING_COUNT
  --result_format RESULT_FORMAT, -rf RESULT_FORMAT
  --input_path INPUT_PATH, -ip INPUT_PATH
  --result_path RESULT_PATH, -rp RESULT_PATH
```

# motivation of this product
- [Numpy](https://github.com/numpy/numpy)
 is widely used in machine learning systems 
 written by python to handle matrix data.
- In particular, deep learning system handles large scale
matrix data as a input data.
- The official Numpy reference says 
"Memory-mapped files are used for accessing small segments of large files on disk, without reading the entire file into memory."
(from [numpy.memmap](https://docs.scipy.org/doc/numpy-1.9.0/reference/generated/numpy.memmap.html#numpy.memmap))
- But I wonder that `numpy.memmap` is really fast to access to the ndarray buffer ?
- To confirm the question, I wrote this benchmark script.

# LICENSE
MIT
