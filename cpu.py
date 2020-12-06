import argparse

import m5
from m5.objects import *


def simulate_system(cpu_type, clock_freq, ram_type, command, mem_size='512MB'):
    system = System()
    system.clk_domain = SrcClockDomain()
    system.clk_domain.clock = clock_freq
    system.clk_domain.voltage_domain = VoltageDomain()
    system.mem_mode = 'timing'
    system.mem_ranges = [AddrRange(mem_size)]

    system.cpu = globals()[cpu_type]()

    system.membus = SystemXBar()

    system.cpu.icache_port = system.membus.cpu_side_ports
    system.cpu.dcache_port = system.membus.cpu_side_ports

    system.cpu.createInterruptController()
    system.cpu.interrupts[0].pio = system.membus.mem_side_ports
    system.cpu.interrupts[0].int_master = system.membus.cpu_side_ports
    system.cpu.interrupts[0].int_slave = system.membus.mem_side_ports

    system.mem_ctrl = MemCtrl()
    system.mem_ctrl.dram = globals()[ram_type]()
    system.mem_ctrl.dram.range = system.mem_ranges[0]
    system.mem_ctrl.port = system.membus.mem_side_ports

    system.system_port = system.membus.cpu_side_ports

    process = Process()
    process.cmd = command.split(' ')
    system.cpu.workload = process
    system.cpu.createThreads()

    # set up the root SimObject and start the simulation
    root = Root(full_system = False, system = system)
    # instantiate all of the objects we've created above
    m5.instantiate()

    print("Beginning simulation!")
    exit_event = m5.simulate()
    print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))


parser = argparse.ArgumentParser()
parser.add_argument('-cpu', '--cpu_type', choices=['MinorCPU', 'TimingSimpleCPU'], default='TimingSimpleCPU',
                    help='What CPU type to use, default: TimingSimpleCPU.')
parser.add_argument('-clk', '--clock_freq', type=str, help='CPU Clock frequency, default: 1GHz.', default='1GHz')
parser.add_argument('-ram', '--ram_type', choices=['DDR3_1600_8x8', 'DDR3_2133_8x8', 'LPDDR2_S4_1066_1x32', 'HBM_1000_4H_1x64'],
                    default='DDR3_1600_8x8', help='What RAM type to use, default: DDR3_1600_8x8.')
parser.add_argument('-cmd', '--command', type=str, default='memtest',
                    help='Command to run on simulated CPU, default: memtest')
args = parser.parse_args()

simulate_system(**vars(args))

