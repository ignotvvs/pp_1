from inheritance_07 import Message

class SMS(Message):
    def __init__(self,sender,recipient):
        self.sender = sender
        self.recipient = recipient
        super().__init__()

    def send(self):
        print(
f"""Sending SMS...
Sender:     {self.sender}
Recipient:  {self.recipient}
{self.message}
""")
