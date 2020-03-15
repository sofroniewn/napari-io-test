from .imageio_reader import IMAGEIO_EXTENSIONS, imageio_reader_function
from .npy_reader import NPY_EXTENSIONS, npy_reader_function


reader_dictionary ={
    'imageio': (IMAGEIO_EXTENSIONS, imageio_reader_function),
    'npy': (NPY_EXTENSIONS, npy_reader_function)
}
