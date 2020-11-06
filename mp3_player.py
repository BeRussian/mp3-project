#import requests
#import json
#from lyrics_api import*  # HW: use it
#79ecf66258437f295418ce9b4eeaaa38 
import math
from song import Song


def read_lyrics(song_name):
    file_name = f"lyrics\{song_name}.txt"
    try:
        with open(file_name, "r") as lyrics_file:
            lyrics = lyrics_file.read()
    except FileNotFoundError:
        lyrics = ""
    return lyrics


class MP3:
    def __init__(self):
        self.songs = [Song(...), ...]
        self.create_existing_songs()

    def run(self):
        print("welcome") 

        while True:
            self.create_new_song()

            self.print_songs()

            self.play_song()

            #שואל את המשתמש מה ברצונו לעשות(לנגן שיר,לקבל מידע על שיר)
            self.info()

            choice = input("Would you like to exit? (yes/no)\n")
            if choice == "yes":
                break

    def get_artists(self):
        artists = []
        for song in self.songs:
            if song.artist not in artists:
                artists.append(song.artist)
        return artists
        #########################
        artists = set()
        for song in self.songs:
            artists.add(song.artist)
        return list(artists)

    #המשתמש מכניס שיר חדש אל תוך מערך השירים
    def create_new_song(self):
        print("would you like to create a new song?")
        choice=input()
        if choice=="yes":
            song_name= input("Enter name of song: ")
            artist_name=  input("input name of artist: ")
            album_name =input("Enter name of album: ")
            length=input("Enter length of song in seconds: ")
            self.songsArray.append(Song(song_name,artist_name,album_name,length))   

    def create_existing_songs(self):
        #יוצר 4 אובייקטים מסוג שיר
        S1=Song("alone","alan walker","all falls down",163)#1
        S2=Song("see you again","noroz","noroz is on fire",250)#2
        S3=Song("all falls down","alan walker","all falls down",163)#3
        S4=Song("Diamond heart","alan walker","all falls down",163)#4
        self.songsArray.append(S1)
        self.songsArray.append(S2)
        self.songsArray.append(S3)
        self.songsArray.append(S4)

    def songList(self):
        #מדפיס את רשימת השירים
        print("Do you want to see the song lisg?")
        choice=input()
        if choice=="yes":
            for x in self.songsArray:
                print(x.get_name_of_song())

    def play_song(self):
        # HW: try to actually play the song (hint: you need an external package (import and stuff))
        # HW: print lyrics line every second (hint: use time.sleep function)
        print("Would you like to play a song?")
        choice=input()
        if choice=="yes":
            songName=input("Which song would you like to play?")
            print (songName)
            print("playing...")

    def info(self):
        print("would you like to get information about a spesific song?")
        choice=input()
        if choice=="yes":
            search_type=input("Search song by 1:name,2:artist,3:album (enter digit)")
            if search_type==1:
                print("Enter songs name")
                song_name=input()

            if search_type==2:
                print("Enter artist name")
                artist_name=input()

            if search_type==3:
                print("Enter album name")
                album_name=input()

# HW: now that you know python much better, fix all the code to be better

if __name__ == "__main__":
    # mp3 = MP3()
    # mp3.run()
    lyrics = read_lyrics("baby")
    if lyrics is not "":
        print(lyrics)
    else:
        print("this song doesn't have any lyrics... :(")
