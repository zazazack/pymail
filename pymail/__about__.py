import os

try:
    from ._version import version as __version__
except ImportError:
    from .__version__ import __version__
