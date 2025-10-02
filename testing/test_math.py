import maths

def test_add():
    assert maths.add(2,2) == 4
    assert maths.add(1,1) == 2
    assert maths.add(-4,3) == -1
    assert maths.add(10,1) == 11
    for i in range(-1000,1000):
        for k in range(-1000,1000):
            assert maths.add(i,k) == i + k
    assert 3.29999 < maths.add(1.1,2.2) < 3.30001
    assert maths.add(1.234,1.0) == 2.234
    
