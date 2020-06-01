import paho.mqtt.client as mqtt
import json
import time

def main():
    client = getClient()
    topic = "iot-2/cmd/umidificador/fmt/json"
    client.subscribe(topic)
    client.on_message = on_message
    client.on_connect = on_connect
    IniciarVerificacaoDeAtualizacao(client)


def getClient():
    host = "n1vgx7.messaging.internetofthings.ibmcloud.com"
    clientId = "d:n1vgx7:Eletrodomestico:Umidificador"
    userName = "use-token-auth"
    password = "umidificador1"

    client = mqtt.Client(clientId)
    client.username_pw_set(userName, password)
    client.connect(host)
    return client

def on_message(client, userdata, message):
    acao =  json.loads(json.loads(message.payload))
    print(acao["Comando"])

def on_connect(client, userdata, flags, result):
    print("Conectado de acordo com o código de resultado:" + str(result))

def IniciarVerificacaoDeAtualizacao(client: mqtt.Client):
    while True:
        client.loop()
        time.sleep(1)

main()