class Tv():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_list = []
        self.volume = 0

    def increase_v(self):
        if self.volume < 10:
            self.volume+=1

    def decrease_v(self):
        if self.volume > 0:
            self.volume-=1

    def turn_on(self):
        self.is_on = True

    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no

    def turn_off(self):
        self.is_on = False

    def set_channels(self,channels_list):
        self.channel_list = channels_list

    def show_channels(self):
        print(f"Available channels: {self.channel_list}")

    def show_status(self):
        try:
            if self.is_on:
                print(f"Tv is on, channel {self.channel_no} ({self.channel_list[self.channel_no-1]}) - {self.volume}")
            else: print("Tv is off")
        except:
            print(f"Tv is on, channel {self.channel_no} - {self.volume}")


tv1 = Tv()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.show_channels()
tv1.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery','Nickolodeon', 'Cartoon Network'])
tv1.set_channel(7)
tv1.show_status()
tv1.set_channel(8)
tv1.decrease_v()
tv1.show_status()
for i in range(14):
    tv1.increase_v()
tv1.show_status()
tv1.turn_off()
tv1.show_status()