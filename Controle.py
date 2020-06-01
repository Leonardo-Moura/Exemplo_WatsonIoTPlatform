import time
import json
import ibmiotf.application as ibmApp

client:ibmApp.Client

def main():
    ConnectClient()
    AssinarEvento()
    client.deviceEventCallback = eventCallBack

    while True:
        time.sleep(1)

def ConnectClient():
    options = {
        "org": "n1vgx7",
        "id": "AmbienteIoT",
        "auth-method": "apikey",
        "auth-key": "a-n1vgx7-ll2uh5snw6",
        "auth-token": "PqBSqiwuKc)@GOR?tX",
        "clean-session": True
    }

    global client
    client = ibmApp.Client(options)
    client.connect()

def AssinarEvento():
    sourceDeviceType="Sensor"
    sourceDeviceId="SensorUmidade"
    sourceEvent="umidade"

    global client
    client.subscribeToDeviceEvents(deviceType=sourceDeviceType, deviceId=sourceDeviceId, event=sourceEvent)

def eventCallBack(event):
    print("event received:" + str(event.data))
    humidity = event.data["data"]
    command = getCommand(humidity)
    Publicar(command)


def getCommand(humidity):
    if humidity < 40:
        return json.dumps({"Comando": "Ligar"})
    else:
        return json.dumps({"Comando": "Desligar"})

def Publicar(command):
    targetDeviceType="Eletrodomestico"
    targetDeviceId="Umidificador"
    commandName = "umidificador"
    global client
    client.publishCommand(targetDeviceType, targetDeviceId, commandName, "json", command)

main()