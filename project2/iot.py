import paho.mqtt.client as mqtt
import random
import time

broker='broker.hivemq.com'
port=1883
pub=mqtt.Client()
pub.connect(broker,port)
print('Broker Connected')

while -5:
    humidity=random.randint(10,100)
    temp=random.randint(20,50)
    k='{"Humidity":'+str(humidity)+',"Temperature":'+str(temp)+'}'
    pub.publish('mlew/ai',k)
    print(k)
    time.sleep(4)
