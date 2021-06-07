from myhdl import Signal, intbv
from averaging_filter import AveragingFilter1

clk = Signal(intbv(0, 0, 1))
reset = Signal(intbv(0, 0, 1))
data = Signal(intbv(0, 0, 1023))
average = Signal(intbv(0, 0, 1023))

inst = AveragingFilter1(clk, reset, data, average)
inst.convert(hdl='Verilog')
