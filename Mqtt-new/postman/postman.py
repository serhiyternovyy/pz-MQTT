import paho.mqtt.client as mqtt
import time
from datetime import datetime

BROKER = "broker"
PORT = 1883
TOPIC = "#"

def on_connect(client, userdata, flags, rc):
    print("[Постман] Підключився до брокера!")
    client.subscribe(TOPIC)
    print("[Постман] Слухаю всі топіки...")

def on_message(client, userdata, msg):
    time_now = datetime.now().strftime("%H:%M:%S")
    print(f"[Постман][{time_now}] Топік: {msg.topic} | Повідомлення: {msg.payload.decode()}")

client = mqtt.Client(client_id="postman-logger")
client.on_connect = on_connect
client.on_message = on_message

time.sleep(3)

client.connect(BROKER, PORT)
client.loop_forever()
