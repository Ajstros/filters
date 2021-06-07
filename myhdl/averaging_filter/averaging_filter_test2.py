from myhdl import InstanceError, block, now, Signal, always, delay, intbv, instance, toVerilog
from clk import ClkDriver
from averaging_filter import AveragingFilter2


@block
def AveragingFilterTest():
    clk = Signal(0)
    clk_driver = ClkDriver(clk, 10)
    reset = Signal(0)
    data = Signal(intbv())
    out = Signal(intbv())
    filter = AveragingFilter2(clk, reset, data, out)

    # Set up display output
    @always(clk.posedge)
    def display_average():
        print(f'{now()}:'.rjust(4) + ' data = ' + f'0x{data}'.rjust(5) + f' ({int(data)})'.rjust(7) +
              ', out = ' + f'0x{out}'.rjust(4) + f' ({int(out)})'.rjust(7) + ', reset = ' + f'0x{reset}'.rjust(4))

    @instance
    def send_signals():
        reset.next = Signal(1)
        yield delay(20)

        reset.next = Signal(0)
        data.next = Signal(intbv(10))  # out = 5 = 0x5
        yield delay(10)

        data.next = Signal(intbv(20))  # out = 15 = 0xf
        yield delay(10)

        data.next = Signal(intbv(10))  # out = 15 = 0xf
        yield delay(10)

        data.next = Signal(intbv(55))  # out = 33 = 0x21
        yield delay(10)

        yield delay(10)  # out = 55 = 0x37

        #### Second Set ####
        # Input:  0, 0, 0, 0, 255, 255, 255, 255
        # Output:    0, 0, 0, 128, 255, 255, 255

        reset.next = Signal(1)
        data.next = Signal(intbv(0))
        yield delay(20)

        reset.next = Signal(0)
        yield delay(10 * 4)

        data.next = Signal(intbv(255))
        yield delay(10 * 4)

    return send_signals, display_average, clk_driver, filter


init = AveragingFilterTest()
init.run_sim(170)
init.quit_sim()
