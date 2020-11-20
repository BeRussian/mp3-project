import requests
import json
from song import *
import pygame
import time
from colors import TerminalColor
import threading
#import multiprocessing 

from lyrics_api import base_url
from lyrics_api import lyrics_matcher
from lyrics_api import format_url
from lyrics_api import artist_search_parameter
from lyrics_api import track_search_parameter
from lyrics_api import api_key


class MP3:
    def __init__(self):
        self.songs=[]
        self.create_existing_songs()
        pygame.init()

    def run(self):
        print(f"{TerminalColor.HEADER}welcome{TerminalColor.ENDC}") 
        print(f"{TerminalColor.OKBLUE}welcome{TerminalColor.ENDC}") 
        print(f"{TerminalColor.OKGREEN}welcome{TerminalColor.ENDC}") 
        print(f"{TerminalColor.WARNING}welcome{TerminalColor.ENDC}") 

        while True:
            self.create_new_song()

            self.print_songs()

            self.play_song()

            self.print_info_about_song()


            choice = input("Would you like to exit? (yes/no)\n")
            if choice == "yes":
                break

    def get_artists(self):
        artists = []
        for song in self.songs:
            if song.artist not in artists:
                artists.append(song.artist)
        return artists

    def create_new_song(self):
        print("would you like to create a new song?")
        choice=input()
        if choice=="yes":
            song_name = input("Enter name of song: ")
            artist_name = input("input name of artist: ")
            album_name = input("Enter name of album: ")
            length = input("Enter length of song in seconds: ")

            self.songs.append(Song(song_name,artist_name,album_name,length))

            songs = json.load(open("songs.json", "r"))
            new_song_dict = {"name": song_name, "artist": artist_name, "album": album_name, "length": length}
            songs.append(new_song_dict)
            json.dump(songs, open("songs.json", "w"))

    def create_existing_songs(self):
        songs = json.load(open("songs.json", "r"))
        for song_dict in songs:
            self.songs.append(Song(song_dict["name"], song_dict["artist"], song_dict["album"], song_dict["length"]))

    def print_songs(self):
        print("Do you want to see the song list?")
        choice=input()
        if choice=="yes":
            for x in self.songs:
                print(f"{TerminalColor.OKGREEN}{x.name}{TerminalColor.ENDC}")
    
    def print_lyrics(self, artist_name, song_name):
        lyrics = self.search_lyrics(artist_name, song_name)
        time_between_lines = self.calculate_time_between_lines(artist_name, song_name)
        for line in lyrics:
            print(line)
            time.sleep(time_between_lines)

    def run_function_in_the_background(self,function):
        thread = threading.Thread(target=function)
        thread.start()
      
    def play_song(self):
        choice=input("Would you like to play a song?\n")
        if choice=="yes":
            song_name=input("Which song would you like to play?\n")
            for song in self.songs:
                if song.name==song_name:
                    artist_name=song.artist
                    break
            try:
                pygame.mixer.music.load(f"songs\\{song_name}.mp3")
                pygame.mixer.music.play()
                print(f"{TerminalColor.WARNING}If you wish to pause the song enter 'p'{TerminalColor.ENDC}")
                self.run_function_in_the_background(self.print_lyrics(artist_name,song_name))
                self.pause_music()
            except pygame.error as error:
                print(f"{TerminalColor.FAIL}Failed to play song. {error}{TerminalColor.ENDC}")
                
    def pause_music(self):
        if input()=="p":
            pygame.mixer.music.pause()
        
    
    def resume_music(self):
        pygame.mixer.music.unpause()

    def calculate_time_between_lines(self, artist, name):
        for song in self.songs:
            if song.name == name and song.artist == artist:
                lyrics = self.search_lyrics(artist, name)
                return (song.length / len(lyrics))/4

    def print_info_about_song(self):
        choice=input("would you like to get information about a spesific song?\n")
        if choice=="yes":
            search_type=input("Search song by 1:name,2:artist,3:album (enter digit)\n")
            if search_type=="1":
                song_name=input("Enter songs name\n")
                for i in self.songs:
                    if i.name==song_name:
                        i.print_details()
                        
            if search_type=="2":
                artist_name=input("Enter artist name\n")
                for i in self.songs:
                    if i.artist==artist_name:
                        i.print_details()

            if search_type=="3":
                album_name=input("Enter album name\n")
                for i in self.songs:
                    if i.album==album_name:
                        i.print_details()

    def search_lyrics(self,artist_name,track_name):
        api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
        request = requests.get(api_call)
        data = request.json()
        data = data['message']['body']
        #print("API Call: " + api_call)
        print()
        lyrics=(data['lyrics']['lyrics_body'])
        return lyrics.split("\n")[:-2]

        

# HW: now that you know python much better, fix all the code to be better

if __name__ == "__main__":
    #create's new mp3 player
    mp3 = MP3()
    #runs the mp3 player
    mp3.run()

    #check's if songs has lyrics and if not return a message
    
