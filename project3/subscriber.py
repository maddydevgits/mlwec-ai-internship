import paho.mqtt.client as mqtt
import json
import pandas as pd

sub=mqtt.Client()
sub.connect('broker.hivemq.com',1883)
print('Broker Conntected')
sub.subscribe('datapirates')
dataset=[]
i=0

def notification(sub,userdata,msg):
  global i
  data=(msg.payload).decode('utf-8')
  data=json.loads(data)
  h=data['Humidity']
  t=data['Temperature']
  dummy=[]
  dummy.append(h)
  dummy.append(t)
  dataset.append(dummy)
  print(dataset)
  i+=1
  if i==10:
    df=pd.DataFrame(dataset)
    df.to_csv('iot.csv')
    i=0

sub.on_message=notification
sub.loop_forever()
