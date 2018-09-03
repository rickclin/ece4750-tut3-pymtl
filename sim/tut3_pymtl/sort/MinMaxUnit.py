#=========================================================================
# MinMaxUnit
#=========================================================================
# This module takes two inputs, compares them, and outputs the larger
# via the "max" output port and the smaller via the "min" output port.

from pymtl import *

class MinMaxUnit( Model ):

  # Constructor

  def __init__( s, nbits=8 ):

    s.in0     = InPort  ( nbits )
    s.in1     = InPort  ( nbits )
    s.out_min = OutPort ( nbits )
    s.out_max = OutPort ( nbits )

    # ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will insert
    # logic here to implement the min/max unit. You should also write a
    # unit test from scratch named MinMaxUnit_test.py.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    s.elm = [ Wire(nbits) for _ in range(2) ]

    @s.combinational
    def minmax_compare():
      if s.in0 <= s.in1:
        s.elm[0].value = s.in0
        s.elm[1].value = s.in1
      else:
        s.elm[0].value = s.in1
        s.elm[1].value = s.in0
      
    s.connect(s.out_min, s.elm[0])
    s.connect(s.out_max, s.elm[1])

