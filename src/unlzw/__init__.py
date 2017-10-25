__version__ = '0.1.0'

from ._unlzw import ffi as _ffi
from ._unlzw import lib as _lib


def unlzw(data):
    out = _ffi.new('char*')
    outlen = _ffi.new('size_t*')
    retcode = _lib.unlzw(
        _ffi.new('char[]', data), len(data),
        out, outlen
    )
    if not retcode:
        return _ffi.string(out, int(outlen))
    elif retcode == 1:
        raise MemoryError("Failed to allocate memory.")
    elif retcode == -1:
        raise ValueError("Bad header.")
    elif retcode == -2:
        raise ValueError("The first code is not a literal or there's an invalid code.")
    elif retcode == -3:
        raise ValueError("Stream ended in the middle of a code.")
    else:
        raise RuntimeError("Unexpected return code %r" % retcode)
