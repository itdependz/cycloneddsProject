from dataclasses import dataclass
from cyclonedds.idl import IdlStruct
from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic 
from cyclonedds.pub import DataWriter
import time

@dataclass
class Message(IdlStruct):
    text: int
@dataclass
class Announcements(IdlStruct):
    text: str

count = 0

announc = "hello world"

participant = DomainParticipant()
topic = Topic(participant, "Message", Message)
topic1 = Topic(participant, "Announcements", Announcements)
writer = DataWriter(participant, topic)
writer1 = DataWriter(participant, topic1)

while True:
    msg = Message(count)
    msg1 = Announcements(announc)
    writer.write(msg)
    writer1.write(msg1)
    print(msg.text)
    print(msg1.text)
    count = count+1
    time.sleep(1)