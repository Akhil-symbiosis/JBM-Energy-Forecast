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

    cluster = MongoClient("localhost:27017")
    db=cluster["JBM_Data"]
    collection=db['test_jbm']
    
    obj=JBM()
    client=mqtt.Client()
    client.connect("3.7.85.13",1883)
    client.subscribe("JBMGroup/em3phase/neel5")
    client.on_message = obj.on_message
    client.loop_forever()