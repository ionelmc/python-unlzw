from os.path import dirname
from os.path import join

from cffi import FFI

ffi = FFI()
ffi.cdef('''
    static int unlzw(unsigned const char *in, size_t inlen, unsigned char **out, size_t *outlen);
''')

ffi.set_source(
    'unlzw._unlzw',
    open(join(dirname(__file__), '_unlzw.c')).read()
)

if __name__ == '__main__':
    ffi.compile()
