# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.rst = 1
    await ClockCycles(dut.clk, 1)
    dut.rst = 0
    await ClockCycles(dut.clk, 1)

    dut._log.info("UP from 0")

    dut.load.value = 0
    dut.out_en.value = 1
    dut.base_count.value = 0
    await ClockCycles(dut.clk, 1)
    assert dut.counter_state.value == 1
    await ClockCycles(dut.clk, 30)

    dut.load.value = 1
    dut.out_en.value = 1
    dut.base_count.value = 250
    await ClockCycles(dut.clk, 1)
    dut.load.value = 0
    await ClockCycles(dut.clk, 2)
    assert dut.counter_state.value == 251
    await ClockCycles(dut.clk, 5)
    # overflows ^

    # Reset
    dut._log.info("Reset")
    dut.rst.value = 1
    await ClockCycles(dut.clk, 2)
    dut.rst.value = 0
    assert dut.counter_state.value == 0

    await ClockCycles(dut.clk, 10)

    # Add tri-state testing
    dut.out_en.value = 0  # Disable outputs
    await ClockCycles(dut.clk, 1)

