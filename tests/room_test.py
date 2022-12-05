import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.instance_of_room = Room("Come and Have a Go if You think You're Bard Enough", [], 15)
        self.instance_of_guest = Guest("Calum Lorimer", 37, 100)

    def test_room_is_empty(self):
        self.assertEqual(0, self.instance_of_room.no_of_people_in_room())

    def test_can_check_guest_in(self):
        self.guest_1 = Guest("Lionel Richie", 73, 500)
        self.instance_of_room.check_guest_in(self.guest_1)
        self.assertEqual(1, self.instance_of_room.no_of_people_in_room())

    def test_can_check_guest_out(self):
        self.guest_2 = Guest("Adam Buxton", 53, 200)
        self.instance_of_room.check_guest_in(self.guest_2)
        self.instance_of_room.check_guest_out(self.guest_2)
        self.assertEqual(0, self.instance_of_room.no_of_people_in_room())

    def test_playlist_starts_unloaded(self):
        self.assertEqual(0, self.room.playlist_starts_unloaded())

    def test_can_add_song_to_playlist(self):
        song_1 = Song("Supersharpbasslinez", "Lenkemz & Axewound", "wobble techno")
        self.instance_of_room.add_song_to_playlist(song_1)
        self.assertEqual(1, len(self.instance_of_room.list_of_songs))


    # def test_guest_old_enough_to_enter(self):
    #     old_enough = self.guest_old_enough_to_enter(self.guest_2)
    #     self.assertEqual(True, old_enough)
    #     # self.instance_of_room.guest_old_enough_to_enter(self.guest_2.instance_of_age)
    #     # self.assertEqual(True, self.guest_2.instance_of_age)
