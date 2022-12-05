class Room:
    def __init__(self, name, guest_list, entry_fee):
        self.instance_of_room_name = name
        self.guest_list = []
        self.list_of_songs = []
        self.entry_fee = entry_fee
        

    def no_of_people_in_room(self):
        return len(self.guest_list)

    def check_guest_in(self, guest):
        self.guest_list.append(guest)

    def check_guest_out(self, guest_to_remove):
        self.guest_list.remove(guest_to_remove)

    def playlist_starts_unloaded(self):
        return len(self.list_of_songs)

    def add_song_to_playlist(self, song_to_add):
        self.list_of_songs.append(song_to_add)

    

    # def guest_old_enough_to_enter(self, guest):
    #     return guest.instance_of_age >= 18