# Copyright 2011, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


_GOODBYE_MESSAGE = u'Goodbye'


def web_socket_do_extra_handshake(request):
    # This example handler accepts any request. See origin_check_wsh.py for how
    # to reject access from untrusted scripts based on origin value.

    pass  # Always accept.

def action_device(device_no, act):
    #initial gpio
    print "try initial gpio"+device_no
    open_io = open("/sys/class/gpio/export", "w")
    open_io.write(light_no)
    # open_io.close()
    print "initial finish"
    # set gpio mode
    print "try to set mode"
    mode_io = open("/sys/class/gpio/gpio"+device_no+"/direction", "wb")
    mode_io.write("out")
    mode_io.close()
    print "set finish"
    # write date and control the device
    print "set data"
    write_io = open("/sys/class/gpio/gpio66/value", "wb")
    write_io.write(act)
    write_io.close()
    print "data set finish"
    print "#########################"
    print "#########################"
    return

def answer_device(device_no):
    print "try initial gpio"+device_no
    open_io = open("/sys/class/gpio/export", "w")
    open_io.write(light_no)
    # open_io.close()
    print "initial finish"
    # set gpio mode
    print "try to set mode"
    mode_io = open("/sys/class/gpio/gpio" + device_no + "/direction", "wb")
    mode_io.write("out")
    mode_io.close()
    print "set finish"
    # write date and control the device
    print "set data"
    read_io = open("/sys/class/gpio/gpio66/value", "wb")
    read_date = read_io.read()
    read_io.close()
    print "data read finish"
    print "#########################"
    print "#########################"
    if read_date == "1":
        return "This device is open"
    else:
        return "This device is closed"

def answer_sensor(sensor_no):
    print "try initial sensor"+sensor_no
    open_sensor = open("/sys/devices/bone_capemgr.9/slots", "w")
    open_sensor.write("BB-ADC")
    print "initial finish"
    print "try to get date"
    read_sensor = open("/sys/bus/iio/devices/iio:device0/in_voltage"+sensor_no+"_raw", "wb")
    read_date = read_sensor.read()

def answer_all():
    print "try to read all date"
    date_light1 = answer_device("66")
    date_light2 = answer_device("67")
    date_light3 = answer_device("69")
    date_light4 = answer_device("68")
    date_fan1 = answer_device("45")
    # date_sensor = answer_sensor("0")
    # process date
    date_return = "light1"+date_light1+"\n"+"light2"+date_light2+"\n"+"light3"+date_light3+"\n"+"light4"+date_light4\
                  + "\n"+"fan1"+date_fan1+"\n"
    #              +"sensor"+date_sensor+"\n"

    return date_return



def web_socket_transfer_data(request):
    while True:
        line = request.ws_stream.receive_message()
        if line is None:
            return

        if isinstance(line, unicode):
            # here is the example date reaction
            if line == "000100":
                print "000100, receive"
                action_device("66", "1")
                request.ws_stream.send_message("commend 000100 receive,light 1 has opened", binary=False)

            elif line == "000101":
                print "000101, receive"
                action_device("66", "0")
                request.ws_stream.send_message("commend 000101 receive,light 1 has closed", binary=False)

            elif line == "000111":
                print "000111,receive"
                device_date = answer_device("66")
                request.ws_stream.send_message("commend 000111 receive"+device_date, binary=False)

            elif line == "000200":
                print "000200, receive"
                action_device("67", "1")
                request.ws_stream.send_message("commend 000200 receive,light 1 has closed", binary=False)

            elif line == "000201":
                print "000201, receive"
                action_device("67", "0")
                request.ws_stream.send_message("commend 000201 receive,light 1 has closed", binary=False)

            elif line == "000211":
                print "000211,receive"
                device_date = answer_device("67")
                request.ws_stream.send_message("commend 000211 receive"+device_date, binary=False)

            elif line == "000300":
                print "000300, receive"
                action_device("69", "1")
                request.ws_stream.send_message("commend 000300 receive,light 1 has closed", binary=False)

            elif line == "000301":
                print "000301, receive"
                action_device("69", "0")
                request.ws_stream.send_message("commend 000301 receive,light 1 has closed", binary=False)

            elif line == "000311":
                print "000311,receive"
                device_date = answer_device("69")
                request.ws_stream.send_message("commend 000311 receive"+device_date, binary=False)

            elif line == "000400":
                print "000400, receive"
                action_device("68", "1")
                request.ws_stream.send_message("commend 000400 receive,light 1 has closed", binary=False)

            elif line == "000401":
                print "000401, receive"
                action_device("68", "0")
                request.ws_stream.send_message("commend 000401 receive,light 1 has closed", binary=False)

            elif line == "000411":
                print "000411,receive"
                device_date = answer_device("68")
                request.ws_stream.send_message("commend 000411 receive"+device_date, binary=False)

            elif line == "000500":
                print "000500, receive"
                action_device("45", "1")
                request.ws_stream.send_message("commend 000500 receive,light 1 has closed", binary=False)

            elif line == "000501":
                print "000501, receive"
                action_device("45", "0")
                request.ws_stream.send_message("commend 000501 receive,light 1 has closed", binary=False)

            elif line == "000511":
                print "000511,receive"
                device_date = answer_device("45")
                request.ws_stream.send_message("commend 000511 receive"+device_date, binary=False)


            elif line == "000000":
                print "000000, receive"
                all_date = answer_all()
                request.ws_stream.send_message(all_date, binary=False)

            else:
                print "illegal command"
                request.ws_stream.send_message("error")
                # reaction finish
            if line == _GOODBYE_MESSAGE:
                return
        else:
            request.ws_stream.send_message(line, binary=True)

# vi:sts=4 sw=4 et
