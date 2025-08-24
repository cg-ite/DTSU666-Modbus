#!/usr/bin/env python3
import minimalmodbus
import argparse
import sys

def read_values(instr):
    """Liest die wichtigsten Werte aus dem DTSU666 aus"""
    try:
        data = {}
        data["Voltage L1-L2"] = instr.read_float(0x2000, 3, 2) / 10
        data["Voltage L2-L3"] = instr.read_float(0x2002, 3, 2) / 10
        data["Voltage L3-L1"] = instr.read_float(0x2004, 3, 2) / 10
        data["Voltage L1"]    = instr.read_float(0x2006, 3, 2) / 10
        data["Voltage L2"]    = instr.read_float(0x2008, 3, 2) / 10
        data["Voltage L3"]    = instr.read_float(0x200A, 3, 2) / 10

        data["Current L1"]    = instr.read_float(0x200C, 3, 2) / 1000
        data["Current L2"]    = instr.read_float(0x200E, 3, 2) / 1000
        data["Current L3"]    = instr.read_float(0x2010, 3, 2) / 1000

        data["Active Power L1"] = instr.read_float(0x2014, 3, 2) / 10
        data["Active Power L2"] = instr.read_float(0x2016, 3, 2) / 10
        data["Active Power L3"] = instr.read_float(0x2018, 3, 2) / 10

        data["Reactive Power L1"] = instr.read_float(0x201C, 3, 2) / 10
        data["Reactive Power L2"] = instr.read_float(0x201E, 3, 2) / 10
        data["Reactive Power L3"] = instr.read_float(0x2020, 3, 2) / 10

        data["Power Factor L1"] = instr.read_float(0x202C, 3, 2) / 1000
        data["Power Factor L2"] = instr.read_float(0x202E, 3, 2) / 1000
        data["Power Factor L3"] = instr.read_float(0x2030, 3, 2) / 1000

        data["Total System Active Power"]   = instr.read_float(0x2012, 3, 2) / 10
        data["Total System Reactive Power"] = instr.read_float(0x201A, 3, 2) / 10
        data["Total System Power Factor"]   = instr.read_float(0x202A, 3, 2) / 1000

        data["Frequency"] = instr.read_float(0x2044, 3, 2) / 100

        data["Total Import kWh"] = instr.read_float(0x401E, 3, 2)
        data["Total Export kWh"] = instr.read_float(0x4028, 3, 2)

        return data

    except Exception as e:
        print("Fehler beim Lesen:", e)
        return None


def main():
    parser = argparse.ArgumentParser(description="Chint DTSU666 Modbus Reader")
    parser.add_argument("--port", default="/dev/ttyUSB0", help="Serieller Port (z.B. /dev/ttyUSB0)")
    parser.add_argument("--baudrate", type=int, default=9600, help="Baudrate (default: 9600)")
    parser.add_argument("--slave", type=int, default=1, help="Modbus Slave ID (default: 1)")
    args = parser.parse_args()

    instr = minimalmodbus.Instrument(args.port, args.slave)
    instr.serial.baudrate = args.baudrate
    instr.serial.bytesize = 8
    instr.serial.parity   = minimalmodbus.serial.PARITY_NONE
    instr.serial.stopbits = 1
    instr.serial.timeout  = 1
    instr.mode = minimalmodbus.MODE_RTU

    values = read_values(instr)
    if values:
        for k, v in values.items():
            print(f"{k:30}: {v:.3f}")

if __name__ == "__main__":
    main()
