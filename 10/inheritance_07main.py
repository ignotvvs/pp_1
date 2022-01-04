from inheritance_sms import SMS
from inheritance_email import Email

sms1 = SMS('2490850','2409521')
sms1.set_message('Let\'s meet on Sunday.')
sms1.send()

email1 = Email('nowak@onet.pl','kowalski@gmail.com','Meeting on Thursday')
email1.set_message('I would like to inform you that our Thursday meeting has been canceled.')
email1.send()