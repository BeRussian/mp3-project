import requests
import json
 # HW: use it
from lyrics_api import *
from song import *
from playsound import playsound

import pygame
import time

import math
from song import *

class MP3:
    def __init__(self):
        self.songs=[]
        self.create_existing_songs()

    def run(self):
        print("welcome") 

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
            song_name= input("Enter name of song: ")
            artist_name=  input("input name of artist: ")
            album_name =input("Enter name of album: ")
            length=input("Enter length of song in seconds: ")
            self.songs.append(Song(song_name,artist_name,album_name,length))   

    def create_existing_songs(self):
        #create's 4 songs
        
        S1=Song("alone","alan walker","all falls down",163)#1
        S2=Song("see you again","noroz","noroz is on fire",250)#2
        S3=Song("all falls down","alan walker","all falls down",163)#3
        S4=Song("Diamond heart","alan walker","all falls down",163)#4
        self.songs.append(S1)
        self.songs.append(S2)
        self.songs.append(S3)
        self.songs.append(S4)

    def print_songs(self):
        print("Do you want to see the song list?")
        choice=input()
        if choice=="yes":
            for x in self.songs:
                print(x.name)

    def play_song(self):
        # HW: try to actually play the song (hint: you need an external package (import and stuff))
        # HW: print lyrics line every second (hint: use time.sleep function)
        path="C:\\Users\\user\\Desktop\\cyberWithRon\\pyhton\mp3-project\\songs\\"
        artist_name=""
        choice=input("Would you like to play a song?\n")
        if choice=="yes":
            songName=input("Which song would you like to play?")
            for i in self.songs:
                if i.name==songName:
                    artist_name=i.artist
            if(songName=="alone"):
                print(self.search_lyrics(artist_name,songName))
                #playsound(f""+path+songName+".mp3")
                pygame.init()
                pygame.mixer.music.load(f""+path+songName+".mp3")
                pygame.mixer.music.play(0)
                time.sleep(5)
                print("5 seconds")
                 

    def caculate_time_between_lines(self,name):
        for i in self.songs:
            if i.name==name:
                length=i.length

    def print_info_about_song(self):
        choice=input("would you like to get information about a spesific song?\n")
        if choice=="yes":
            search_type=input("Search song by 1:name,2:artist,3:album (enter digit)\n")
            if search_type=="1":
                song_name=input("Enter songs name\n")
                for i in self.songs:
                    if i.name==song_name:
                        i.toString
                        
            if search_type=="2":
                artist_name=input("Enter artist name\n")
                for i in self.songs:
                    if i.artist==artist_name:
                        i.toString

            if search_type=="3":
                album_name=input("Enter album name\n")
                for i in self.songs:
                    if i.album==album_name:
                        i.toString

    
   

    

    def search_lyrics(self,artist_name,track_name,):
        api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
        request = requests.get(api_call)
        data = request.json()
        data = data['message']['body']
        print("API Call: " + api_call)
        print()
        lyrics=(data['lyrics']['lyrics_body'])
        return lyrics

        

# HW: now that you know python much better, fix all the code to be better

if __name__ == "__main__":
    #create's new mp3 player
    mp3 = MP3()
    #runs the mp3 player
    mp3.run()

    #check's if songs has lyrics and if not return a message
    
