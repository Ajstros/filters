from myhdl import Signal, intbv
from averaging_filter import AveragingFilter1

clk = Signal(intbv(0, 0, 1))
reset = Signal(intbv(0, 0, 1))
data = Signal(intbv(0, 0, 255))
average = Signal(intbv(0, 0, 255))

inst = AveragingFilter1(clk, reset, data, average)
inst.convert(hdl='Verilog')
