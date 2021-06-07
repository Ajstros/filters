from myhdl import block, delay, always, now, Signal


@block
def HelloWorld():

    clk = Signal(0)

    @always(delay(10))
    def drive_clk():
        clk.next = not clk

    @always(clk.posedge)
    def say_hello():
        print(f"{now()}: Hello World!")

    return say_hello, drive_clk


inst = HelloWorld()
inst.run_sim(50)
