import androidhelper
import socket
import time

droid = androidhelper.Android()

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('192.168.2.6', 5000))

def readAcc():
    dt = 100
    endTime = 3000
    timeSensed = 0
    droid.startSensingTimed(2,dt)
    while timeSensed <= endTime:
        senout = droid.sensorsReadAccelerometer().result
        time.sleep(dt/1000.0)
        timeSensed+=dt

    print senout
    clientsocket.send(str(senout).strip('[]'))


readAcc()

droid.stopSensing()
