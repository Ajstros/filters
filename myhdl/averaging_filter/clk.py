from myhdl import block, instance, delay

@block
def ClkDriver(clk, period=20):
    time_low = period//2
    time_high = period - time_low

    @instance
    def drive_clk():
        while True:
            yield delay(time_low)
            clk.next = 1
            yield delay(time_high)
            clk.next = 0
    
    return drive_clk