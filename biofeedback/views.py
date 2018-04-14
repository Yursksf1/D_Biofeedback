from django.shortcuts import render
import os
from django.http import JsonResponse
import _thread as thread
#from subprocess import run


#from .models import Question



def index(request):

    thread.start_new_thread(plotters, ())
    #plotters()
    print("yes")

    context = {'1': 1}
    return render(request, 'bio/index.html', context)


def plotters():
    cmd = 'python luz3.py'
    os.system(cmd)


import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

temp_ant = 0
def get_seriales(request):
    global temp_ant 
    try:
        temp = ser.readline()
        try:
            
            temp = int(temp)
            
        except ValueError as Ve:
                    temp = 'none'
                    
    except AttributeError as Ae:
        temp = 'none'

    except TypeError as Te:
        temp = 'none'

    except Exception as e:
        temp = 'none'

    change = True 
    if (temp == 'none'):
        temp = temp_ant
        change = False
    
    if (temp_ant != temp):
        temp_ant = temp

    data = {
                'serial': temp,
                'serial_1': temp,
                'serial_2': temp,
                'serial_3': temp,
                'change': change
            }

    return JsonResponse(data)

def index_2(request):
    context = {'1': 1}
    return render(request, 'bio/index_2.html', context)   