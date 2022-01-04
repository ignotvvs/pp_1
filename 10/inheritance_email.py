from inheritance_07 import Message


class Email(Message):
    def __init__(self, sender, recipient,subject):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        super().__init__()

    def send(self):
        print(
            f"""Sending email...
From:    {self.sender}
To:      {self.recipient}
Subject: {self.subject}
{self.message}
""")