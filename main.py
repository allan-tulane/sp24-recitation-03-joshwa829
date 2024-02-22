"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
    def __add__(self, other):
      if isinstance(other, BinaryNumber):
          # Convert binary strings to integers, add them, and convert back to binary
          sum_val = self.decimal_val + other.decimal_val
          return BinaryNumber(sum_val)
      else:
          return NotImplemented
  
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    xvec = x.binary_vec
    yvec = y.binary_vec

    # Pad xvec and yvec with leading zeros
    max_len = max(len(xvec), len(yvec))
    xvec = ['0'] * (max_len - len(xvec)) + xvec
    yvec = ['0'] * (max_len - len(yvec)) + yvec

    # Base case
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return x * y

    # Split into two halves
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)

    # Recursively computing the four multiplications
    x_left_y_left = _quadratic_multiply(x_left, y_left)
    x_left_y_right = _quadratic_multiply(x_left, y_right)
    x_right_y_left = _quadratic_multiply(x_right, y_left)
    x_right_y_right = _quadratic_multiply(x_right, y_right)

    # Combine the results using the quadratic multiplication formula
    part1 = bit_shift(x_left_y_left, len(xvec))
    part2 = bit_shift(x_left_y_right + x_right_y_left, len(xvec) // 2)
    part3 = x_right_y_right

    # Sum the three parts to get the final result
    return part1 + part2 + part3



    
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    result = f(x, y)
    duration_ms = (time.time() - start) * 1000
    return result, duration_ms

    
    

