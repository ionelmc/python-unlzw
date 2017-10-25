from os.path import dirname
from os.path import join

from unlzw import unlzw


def test_decode():
    assert unlzw(open(join(dirname(__file__), 'test.txt.Z'), 'rb').read()) == '''
foobar
123
'''
