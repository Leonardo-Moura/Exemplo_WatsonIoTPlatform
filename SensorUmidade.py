import paho.mqtt.client as mqtt
import time
import random
import json

def main():
    client = getClient()
    topic = "iot-2/evt/umidade/fmt/json"
    while True:
        PublicarValorAleatorio(client, topic)
        time.sleep(3)


def getClient():
    host = "n1vgx7.messaging.internetofthings.ibmcloud.com"
    clientId = "d:n1vgx7:Sensor:SensorUmidade"
    userName = "use-token-auth"
    password = "sensorUmidade1"

    client = mqtt.Client(clientId)
    client.username_pw_set(userName, password)
    client.connect(host)
    return client

def PublicarValorAleatorio(client: mqtt.Client, topic):
    try:
        value = random.randint(20, 75)
        message = json.dumps({"data": value})
        print(message)
        client.publish(topic, message)
    except :
        print("Erro.")

main()