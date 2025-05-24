`default_nettype none
`timescale 1ns / 1ps

/* This testbench just instantiates the module and makes some convenient wires
   that can be driven / tested by the cocotb test.py.
*/
module tb ();

  // Dump the signals to a VCD file. You can view it with gtkwave or surfer.
  initial begin
    $dumpfile("tb.vcd");
    $dumpvars(0, tb);
    #1;
  end

  // Wire up the inputs and outputs:
  reg clk;
  reg rst;
  reg load;
  reg out_en;
  reg [7:0] base_count;
  reg [7:0] counter_state;

  eight_bit_sync_counter user_project (
    .clk(clk),
    .rst(rst),
    .load(load),
    .out_en(out_en),
    .base_count(base_count),
    .counter_state(counter_state)
  );

endmodule
