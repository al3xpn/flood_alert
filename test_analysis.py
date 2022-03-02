import datetime
from floodsystem.analysis import polyfit

def test_polyfit():
    """Tests the function polyfit used for 2F."""

    x = [0.0, 1.0, 2.0, 3.0,  4.0,  5.0]
    y = [0.0, 0.8, 0.9, 0.1, 2.0, 1.0, 1.5]

    poly, d0 = polyfit(x, y, 4)
    
    #assert poly(3) == 1

    #assert 1 == 1
    #assert float('%.2g' % poly(4)) == -0.8

    #assert float('%.2g' % poly(5)) == -1.0


