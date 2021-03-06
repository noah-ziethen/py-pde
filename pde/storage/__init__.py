"""
Module defining classes for storing simulation data.

.. autosummary::
   :nosignatures:

   ~memory.get_memory_storage
   ~memory.MemoryStorage
   ~file.FileStorage
   
.. codeauthor:: David Zwicker <david.zwicker@ds.mpg.de> 
"""

from .memory import MemoryStorage, get_memory_storage
from .file import FileStorage
