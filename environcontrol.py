"""
#! Python3
This code is to be used with a Raspberry Pi 3
It interacts with various parts of indoor garden components.
"""
import time
import RPi.GPIO as gpio


def pump_function_check():
    """Test 12v Pump"""
    gpio.setwarnings(False)
    print("Begin Pump Test")
    gpio.setmode(gpio.out)
    gpio.setup(2, gpio.out)
    time.sleep(5)
    gpio.cleanup()
    print("Pump Finished")


def led_function_check():
    """Test 12v LED Light Fixture"""
    gpio.setwarnings(False)
    print("Begin LED Lights Test")
    gpio.setmode(gpio.out)
    gpio.setup(2, gpio.out)
    time.sleep(5)
    gpio.cleanup()
    print("LED Test Finished")


def main():
    """Execute Tests"""
    print("Begin Function Checks (2 Total)")
    print("Function Check 1")
    time.sleep(1)
    pump_function_check()
    time.sleep(1)
    print("Function Check 1 Complete")
    time.sleep(3)
    print("Function Check 2")
    time.sleep(1)
    led_function_check()
    time.sleep(1)
    print("Function Check 2 Complete")


main()
    