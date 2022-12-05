import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Blue Skies", "Willie Nelson", "country")
        self.song_2 = Song("On a Ragga Tip", "SL2", "hardcore")
        self.song_3 = Song("Concrete Schoolyard", "Jurassic 5", "hip-hop")

    def test_song_has_genre(self):
        self.assertEqual("hardcore", self.song_2.instance_of_genre)

    def test_song_has_title(self):
        self.assertEqual("Concrete Schoolyard", self.song_3.instance_of_title)

    def test_song_has_artist(self):
        self.assertEqual("Willie Nelson", self.song_1.instance_of_artist)