# We want to average the incoming data with the last data point
# Ex. Input: 0, 0, 0, 0, 1023, 1023, 1023, 1023
#    Output:    0, 0, 0, 512,  1023, 1023, 1023

from myhdl import block, always, intbv, Signal, always_comb

@block
def AveragingFilter1(clk, reset, data, average):
    # This block uses an always block to change the values, but this ends up
    # changing the values 1 clock cycle too late

    # data must be an intbv so the previous.next assignment works
    previous = Signal(intbv(0, 0, 255))

    @always(clk.posedge)
    def update_previous():
        if (reset):
            previous.next = Signal(intbv(0))
            average.next = Signal(intbv(0))

        else:
            average.next = (previous + data + 1) >> 1 # Add 1 so the bit shift rounds up at halves (9/2 = 4.5 ~ 5)
            previous.next = data

    return update_previous

@block
def AveragingFilter2(clk, reset, data, average):
    # This block achieves the same averaging filter using a combinational always block,
    # changing the values exactly on time

    # datastream holds incoming data, new data goes on the left
    datastream = Signal(intbv(0, 0, 65535))

    @always(clk.posedge)
    def update_previous():
        if (reset):
            datastream.next = Signal(intbv(0, 0, 255))

        else:
            datastream.next = (data * 2**(len(datastream) - 8)) + datastream[:8]

    @always_comb
    def assign_average():
        nonlocal average

        if (reset):
            average.next = Signal(intbv(0, 0, 255))
        else:
            # Add 1 so the bit shift rounds up at halves (9/2 = 4.5 ~ 5)
            average.next = sum(datastream) + 1 >> 1

    return update_previous, assign_average
