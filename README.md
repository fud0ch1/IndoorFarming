# environcontrol.py - Python3 Environmental Grow Control Unit

Python Support for the Raspberry Pi 3 (RPi3) to operate as an environmental grow control unit. These functions provide controls to various mechanisms that make up an indoor 
evironmental growing station


Code contained in this repository was written by Dave Foran -- Jan 2020 to fit 
into Python3 and PEP 8 Conventions. I am desigining and building an environmental grow station that can be built from available parts online. More directions will be added as more of the project is completed.

## Getting Started / Setup

### Setting Raspberry Pi 3 to use the functions

To get started, you will need to install the python GPIO package. Functions correspond to the various pins that drive both sensors as well as 12v LED lights and a pump utilizing a [Sainsmart 2-channel Relay Module](https://www.sainsmart.com/products/2-channel-5v-relay-module). Once you've connected the GPIO Pins to the Sainsmart 2-channel Relay Module (Pictures and directions coming), lets set up our Python Environment on our RPi3
 
 ### Setting Up Python Environment

As usual, I recommend you first set up a Virtual Environment and enter into it with a set of commands like:

    sudo apt-get update
    
    sudo apt-get install python-rpi.gpio python3-rpi.gpio

    python3 -m venv <environment name>      # ex. python3 -m venv indoor_garden

    source <environment name>/bin/activate  # ex. source indoor_garden/bin/activate

You'll need to have the 'pyserial' Python module installed to use maestro.py.

Using pip3 for python3

    pip3 install RPi.GPIO

Now you can create a script and start using your RPi.GPIO to drive various servo-mechanisms, sensors, and other electrical appliances

## Example Script

Example usage of maestro.py:

    import time
    import RPi.GPIO as gpio

    def pump_function_check():
        """Test 12v Pump"""
        gpio.setwarnings(False)
        print("Begin Pump Test")
        gpio.setmode(gpio.out)   # Set GPIO to push signals to module
        gpio.setup(2, gpio.out)  # Send signal to GPIO 2
        time.sleep(5)
        gpio.cleanup()           # Stop signal to GPIO 2
        print("Pump Finished")

There are other methods provided by the module. There are also other ways of interacting with modules. I will add more documentation as the codebase for this project grows.

## Authors

* **Dave Foran** - *Original Writer* - [fud0ch1](https://github.com/fud0ch1)

## License

This project is licensed under the MIT License

## Acknowledgments

* Most of this code I learned off of various websites and other references. I will compile a list in the future

* Inspiration - I am building this grow farm to do some experimentation with indoor growing. My interest in indoor growing came as part of my studies in transnational securitys, of which food security is a big issue. Is indoor growing feasible as a sustainable way to produce food, we will see!

* Please reach out to me with any questions that you have at livefromtheabyss@gmail.com, I am always excited to see projects you are working on! If you have any recommendations on improving the code or formatting, please let me know as well.

* If you copy this project, please just link back to me!