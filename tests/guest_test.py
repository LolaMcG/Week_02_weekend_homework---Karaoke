import unittest
from classes.guest import Guest
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.instance_of_guest = Guest("Bob McJim", 37, 20)
        self.instance_of_room = Room("", [], 15)

    def test_guest_has_name(self):
        guest_name = self.instance_of_guest.instance_of_name
        self.assertEqual("Bob McJim", guest_name)

    def test_guest_has_age(self):
        guest_age = self.instance_of_guest.instance_of_age
        self.assertEqual(37, guest_age)

    def test_guest_has_wallet(self):
        self.assertEqual (20, self.instance_of_guest.wallet)



    # def test_guest_can_afford_entry(self):
    #     self.assertEqual(True, self.guest_can_afford_entry(instance_of_guest))

    # def test_guest_can_afford_entry(self):
    #     self.assertEqual(True, self.guest_can_afford_entry(self.instance_of_guest))