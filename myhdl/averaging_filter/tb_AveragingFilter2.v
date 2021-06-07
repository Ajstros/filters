module tb_AveragingFilter2;

reg [0:0] clk;
reg [0:0] reset;
reg [7:0] data;
wire [7:0] average;

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

AveragingFilter2 dut(
    clk,
    reset,
    data,
    average
);

endmodule
