import numpy as np
import imageio
from ..typing import PathLike, LayerData, List


NPY_EXTENSIONS = tuple('.npy')


def npy_reader_function(path: PathLike) -> List[LayerData]:
    """Take a path or list of paths and return a list of LayerData tuples."""
    paths = [path] if isinstance(path, str) else path
    # stack a list of strings, but also works for a single path string
    data = np.squeeze(np.stack([np.load(_path) for _path in paths]))
    # Readers are expected to return data as a list of tuples, where each tuple
    # is (data, [meta_dict, [layer_type]])
    meta = {}  # optional kwargs for the corresponding viewer.add_* method
    return [(data, meta)]
