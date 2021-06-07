from myhdl import Signal, intbv
from clk import ClkDriver

clk = Signal(intbv(0, 0, 1))
clk_driver = ClkDriver(clk, 10)
clk_driver.convert(hdl='Verilog')