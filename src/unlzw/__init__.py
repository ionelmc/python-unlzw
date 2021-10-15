__version__ = '0.1.2'

from ._unlzw import ffi as _ffi
from ._unlzw import lib as _lib


def unlzw(data):
    tmp_out = _ffi.new('unsigned char**')
    outlen = _ffi.new('size_t*')
    retcode = _lib.unlzw(
        _ffi.new('unsigned char[]', data), len(data),
        tmp_out, outlen
    )
    if not retcode:
        out = bytearray(outlen[0])
        _ffi.memmove(out, tmp_out[0], outlen[0])
        _lib.free(tmp_out[0])
        return out
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
