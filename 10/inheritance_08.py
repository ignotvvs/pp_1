class Phone:
    def __init__(self,model,battery_status,has_service = True):
        self.model = model
        self.battery_status = battery_status
        self.has_service = has_service
        self.is_on = False

    def make_call(self,contact):
        if self.has_service and self.is_on:
            print(f"Calling {contact}...")
        else:
            print("No service!")

    def turn_on(self):
        if self.battery_status == "0":
            print("Recharge your phone")
        else:
            self.is_on = True

    def turn_off(self):
        self.is_on = False

    def __str__(self):
        return f"""Model:                {self.model}
Battery status:       {self.battery_status}%
Does it have servive: {self.has_service}
Is it on:             {self.is_on}        
"""


phone1 = Phone('iPhone 8','40',True)
print(phone1)
phone1.turn_on()
phone1.make_call('Michael')