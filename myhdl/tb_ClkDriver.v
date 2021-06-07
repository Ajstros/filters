module tb_ClkDriver;

wire [0:0] clk;

initial begin
    $to_myhdl(
        clk
    );
end

ClkDriver dut(
    clk
);

endmodule
