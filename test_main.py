from main import *



## Feel free to add your own tests here.

def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3

    assert quadratic_multiply(BinaryNumber(29), BinaryNumber(-10)) == 29*(-10)

    assert quadratic_multiply(BinaryNumber(104), BinaryNumber(62)) == 104*62

    assert quadratic_multiply(BinaryNumber(57), BinaryNumber(-33)) == 57*(-33)

