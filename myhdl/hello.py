from myhdl import block, always, now

@block
def Hello(clk, to="World!"):
    
    @always(clk.posedge)
    def say_hello():
        print(f'{now()}: Hello {to}')

    return say_hello