class Guest:
    def __init__(self, name, age, wallet):
        self.instance_of_name = name
        self.instance_of_age = age
        self.wallet = wallet



    def guest_can_afford_entry(self, guest):
        if self.wallet >= self.instance_of_room.entry_fee:
            return True

    # def guest_can_afford_entry(self, guest):
    #     if guest.wallet >= self.room.entry_fee:
    #         return True
