from myhdl import block, Signal
from clk import ClkDriver
from hello import Hello

@block
def Greetings():

    clk1 = Signal(0)
    clk2 = Signal(0)

    clk_driver1 = ClkDriver(clk1) # Using default period=20
    clk_driver2 = ClkDriver(clk2, 19)

    hello1 = Hello(clk1) # Using default to="World!"
    hello2 = Hello(clk2, to="MyHDL!")

    return clk_driver1, clk_driver2, hello1, hello2

inst = Greetings()
inst.run_sim(50)