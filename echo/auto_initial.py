# copyright 2017, Yellow One Study.
# All rights reserved.
#
# initial the GPIO and and other devices before the service start
# to avoid the repeat initial change the value of some port
# It is the part of Yellow One Study's remote control system
#
# This remote control system hardware version is beaglebone black REV.C
# Hardware detail information can reference
# http://www.ti.com/tool/beaglebk
# Operation system: Debian
# CPU: AM3358BZCZ100 from Texas Instruments
# the detail of this process can reference
# http://www.ti.com/lsds/ti/processors/sitara/arm_cortex-a8/am335x/overview.page

def gpio_init(device_no)
    print "try initial gpio" + device_no
    open_io = open("/sys/class/gpio/export", "w")
    open_io.write(device_no)
    # open_io.close()
    print "initial finish"
    # set gpio mode
    print "try to set mode"
    mode_io = open("/sys/class/gpio/gpio" + device_no + "/direction", "w+")
    mode_io.write("out")
    mode_io.close()
    print "set finish"
    # here display present mode
    print "try display the present port situation"
    mode_io = open("sys/class/gpio/gpio"+device_no+"/direction","r")
    present_mode = mode_io.read()
    mode_io.close()
    print "device"+device_no+"date direction is"+present_mode
    #here display present value
    value_io = open("sys/class/gpio/gpio"+device_no+"value","r")
    present_value = value_io.read()
    value_io.close()
    print "device"+device_no+"present date is "+present_value
    print "now device"+device_no+"initial success"
    print "#########################"
    print "#########################"
    return

def adc_init()
    print "try initial sensor"
    open_sensor = open("/sys/devices/bone_capemgr.9/slots", "w")
    open_sensor.write("BB-ADC")
    print "initial finish"
    print "test date reading"
    read_sensor = open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw", "rb")
    read_date = read_sensor.read()
    read_sensor.close()
    print "here is the example date"
    print read_date
    print "sensor 0 initial success"
    print "#########################"
    print "#########################"
    return

print "try to initial"
gpio_init("66")
gpio_init("67")
gpio_init("69")
gpio_init("68")
gpio_init("45")
# warning the function adc_initial() can initial all the adc port at a time don't try to repeat this function
# the example date is from adc0
#the dir "/sys/devices/bone_capemgr.9/slots" may be difference in difference devices for example
# some of the adc dir is "/sys/devices/bone_capemgr.8/slots"
adc_init()



















