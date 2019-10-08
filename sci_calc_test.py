from sci_calc import *

def test_find_sqrt():
    assert find_sqrt(576) == 24
    assert find_sqrt(256) == 16
    assert find_sqrt(841) == 29

def test_find_ceil():
    assert find_ceil(8.4151616) == 9
    assert find_ceil(2.616516516581684896165168165) == 3
    assert find_ceil(math.pi) == 4

