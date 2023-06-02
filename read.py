from dataclasses import dataclass
from cyclonedds.domain import DomainParticipant
from cyclonedds.topic import Topic
from cyclonedds.sub import DataReader
from cyclonedds.util import duration
from cyclonedds.idl import IdlStruct

@dataclass
class Message(IdlStruct):
    text: int

@dataclass
class Announcements(IdlStruct):
    text: str


participant = DomainParticipant()
topic = Topic(participant, "Message", Message)
topic1 = Topic(participant, "Announcements", Announcements)
reader = DataReader(participant, topic)
reader1 = DataReader(participant, topic1)

for msg in reader.take_iter(timeout=duration(minutes=5)):
    for msg1 in reader1.take_iter(timeout=duration(minutes=5)):
        print(msg1.text)
        break
    print(msg.text)

