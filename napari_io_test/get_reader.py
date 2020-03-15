"""
This module is an example of a barebones plugin, using imageio.imread.

It implements the ``napari_get_reader`` hook specification, (to create
a reader plugin) but your plugin may choose to implement any of the hook
specifications offered by napari.

Type annotations here are OPTIONAL!
If you don't care to annotate the return types of your functions
your plugin doesn't need to import, or even depend on napari at all!

Replace code below accordingly.
"""
from pluggy import HookimplMarker
from .typing import PathLike, ReaderFunction, Optional
from .readers import reader_dictionary


napari_hook_implementation = HookimplMarker("napari")


@napari_hook_implementation
def napari_get_reader(path: PathLike) -> Optional[ReaderFunction]:
    """A basic implementation of the napari_get_reader hook specification."""
    if isinstance(path, list):
        # reader plugins may be handed single path, or a list of paths.
        # if it is a list, it is assumed to be an image stack...
        # so we are only going to look at the first file.
        path = path[0]
    
    for extensions, reader in reader_dictionary.values():
        if path.endswith(extensions):
            return reader
    
    return None
