import paho.mqtt.client as mqtt

sub=mqtt.Client()
broker='broker.hivemq.com'
port=1883
sub.connect(broker,port)
print('Broker Connected')
sub.subscribe('programchasers')

def notification(sub,userdata,msg):
    print(msg.payload)

sub.on_message=notification
sub.loop_forever()
