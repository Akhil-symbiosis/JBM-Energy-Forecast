#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
class JBM:
    
    def on_message(self, client, userdata, message):
        topic=message.topic
        payload=message.payload.decode()
        print(payload)
        print("Message received".format(topic, payload))
        print(type(payload))
        collection.insert_one(json.loads(payload))
        
if __name__ == "__main__":

    client=MongoClient('localhost',27017)
    db=client.JBM_Data
    collection=db['test_jbm']
    
    obj=JBM()
    client=mqtt.Client()
    client.connect("3.7.85.13",1883)
    client.subscribe("JBMGroup/MachineData/#")
    client.on_message = obj.on_message
    client.loop_forever()


# In[ ]:





# In[ ]:




