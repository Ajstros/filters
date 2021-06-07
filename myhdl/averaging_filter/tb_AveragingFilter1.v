module tb_AveragingFilter1;

reg [0:0] clk;
reg [0:0] reset;
reg [9:0] data;
wire [9:0] average;

initial begin
    $from_myhdl(
        clk,
        reset,
        data
    );
    $to_myhdl(
        average
    );
end

AveragingFilter1 dut(
    clk,
    reset,
    data,
    average
);

endmodule
