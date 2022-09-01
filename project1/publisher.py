import paho.mqtt.client as mqtt
broker='broker.hivemq.com'
port=1883
pub=mqtt.Client()
pub.connect(broker,port)
print('Broker Connected')
pub.publish('mlew','its break time')
