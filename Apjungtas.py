import time
import pyvisa
import serial
from serial import Serial
#from os.path import joinpy 
from time import sleep
import serial.tools.list_ports
#global dMM1
def find(Port1, Visa1, Visa2):
    global supply, dMM1, rm, rigol, state
    # try:
        
    state = True
    supply = serial.Serial(
        port=Port1,
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_NONE,
        #stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        dsrdtr=True 
)
    rm = pyvisa.ResourceManager()
    dMM1 = rm.open_resource(Visa1)
    rigol = rm.open_resource(Visa2)
    print(Port1)
    print('Prijungta')
    # except:
    #     supply.close()
    #     dMM1.close()
    #     rigol.close()
    #     state = True
    #     supply = serial.Serial(
    #         port=Port1,
    #         baudrate=9600,
    #         timeout=1,
    #         parity=serial.PARITY_NONE,
    #         #stopbits=serial.STOPBITS_ONE,
    #         bytesize=serial.EIGHTBITS,
    #         dsrdtr=True 
    # )
    #     rm = pyvisa.ResourceManager()
    #     dMM1 = rm.open_resource(Visa1)
    #     rigol = rm.open_resource(Visa2)
    #     print(Port1)
    #     print('Prijungta')
        
def ijungti():
    #global supply
    #global dMM1
    try:
        supply.flushInput()  # clear input buffer
        supply.isOpen()  # open serial port

        commands = ['*IDN?\n','Output on\n']
        for com in commands:
            send = com.encode()
            supply.write(send)

            print(supply.read())
            print('Ok')
            time.sleep(0.5)
    except:
        print("Jau yra arba niekad nebuvo")
       
def matavimas(Itampa):
    global I
    global U
    #Itampa = 1
    if supply.isOpen() is True:
        command = 'Voltage %0.01f\n'%(Itampa)
        send = command.encode()
        supply.write(send)
        i = 0
        Isum = 0
        Usum = 0
        while i<1:
            
            I=float(dMM1.query('MEAS:CURR:DC? 1'))
            Isum = I + Isum
            U=float(dMM1.query('MEAS:VOLT:DC? 20'))
            Usum = U + Usum
            i = i + 1
        I = Isum/i
        U = Usum/i
        return I, U
    else:
        supply.isOpen()
        command = 'Voltage %0.01f\n'%(Itampa)
        send = command.encode()
        supply.write(send)
        i = 0
        Isum = 0
        Usum = 0
        while i<1:
            
            I=float(dMM1.query('MEAS:CURR:DC? 1'))
            Isum = I + Isum
            U=float(dMM1.query('MEAS:VOLT:DC? 20'))
            Usum = U + Usum
            i = i + 1
        I = Isum/i
        U = Usum/i
        return I, U
def nulinimas():
    command = 'Voltage 0\n'
    send = command.encode()
    supply.write(send)
def find_com():
    comms = serial.tools.list_ports.comports()
    #print(comms)
    list = []
    for port in comms:
        list.append(str(port))
    #print(list)
    print('COM paimta')
    
    return list
def find_visa():
    rm = pyvisa.ResourceManager()
    a = rm.list_resources()
    #print(type(a))
    list = []
    for i in a:
        list.append(str(i))
    #print(list)
    print('Visa paimta')
    return list
def output1():
    time.sleep(0.5)
    command = 'INST:NSEL 1\n'
    send = command.encode()
    supply.write(send)
def output2():
    time.sleep(0.5)
    command = 'INST:NSEL 2\n'
    send = command.encode()
    supply.write(send)
def set_voltage(voltage):
    command = 'VOLTAGE %0.01f\n'%voltage
    send = command.encode()
    supply.write(send)



def rigol_matavimas(Itampa):
    global I
    global U
    #Itampa = 1
    if supply.isOpen() is True:
        command = 'Voltage %0.01f\n'%(Itampa)
        send = command.encode()
        supply.write(send)
        i = 0
        Isum = 0
        Usum = 0
        while i<1:
            
            I=float(rigol.query(':measure:current:DC?'))
            Isum = I + Isum
            U=float(rigol.query(':measure:voltage:DC?'))
            Usum = U + Usum
            i = i + 1
        I = Isum/i
        U = Usum/i
        return I, U
    else:
        supply.isOpen()
        command = 'Voltage %0.01f\n'%(Itampa)
        send = command.encode()
        supply.write(send)
        i = 0
        Isum = 0
        Usum = 0
        while i<1:
            
            I=float(rigol.query(':measure:current:DC?'))
            Isum = I + Isum
            U=float(rigol.query(':measure:voltage:DC?'))
            Usum = U + Usum
            i = i + 1
        I = Isum/i
        U = Usum/i
        return I, U
def disc():
    supply.close
    dMM1.close
    rigol.close





#time.sleep(0.25)
#find(Port='COM3',Visa='USB0::0x164E::0x0DB6::TW00022471::INSTR')
#output1()
#time.sleep(2)
#output2()
#ijungti
#vidurkinimas() 
#nulinimas()
#saltinison()
#matavimas()
        