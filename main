#import requests
#import json
#from lyrics_api import*
#79ecf66258437f295418ce9b4eeaaa38 
import math

#מילון שירים
songs={1:"alone",2:"see you again",3:"all falls down",4:"Diamond heart"}
artist={1:"alan walker",2:"noroz",3:"tamir bar",}
album={1:"alone",2:"see you again",3:"all falls down",4:"Diamond heart"}


class Song:
    

    def __init__(self,name, artist,album,length):
        self.name=name
        self.artist = artist
        self.album = album
        self.length = int(length)
        
        if self.isIn(1,self.name,songs,artist,album)==False:
            songs[len(songs)+1]=self.name
        if  self.isIn(2,self.artist,songs,artist,album)==False:
            songs[len(songs)+1]=self.name
        if  self.isIn(3,self.album,songs,artist,album)==False:
            songs[len(songs)+1+1]=self.name

#מחזיר את הזמר
    def get_name_of_song(self):
        print(self.name)
#מחזיר את הזמר
    def get_artist(self):
        print(self.artist)
#מחזיר את האלבום בו השיר נמצא
    def get_album(self):
        print(self.album)
#מחזיר את אורך השיר בשניות
    def get_length(self,):
        print(self.length)
       
    def print_detailes(self):
        print(f"Songs name is {self.name} by {self.artist} from the album  {self.album}")
        print(self.sec_to_min())
#ממיר זמן של שיר משניות לדקות
    def sec_to_min(self):
        min=self.length/60
        min=math.floor(min)
        min=str(min)
        sec=str(self.length%60)
        r=(f"Songs length is:" +min+ ":" +sec +" minutes ")
        return r
#בודק האם ערך מסוים נמצא ב1 מהמילונים ואם לו מוסיף את הערך
    def isIn(self,x,value,songs,artist,album):
        number=int(x)
        bool=False
        if number==1:
         if 'value' in songs.values()==True:
            bool=True
         else:
          pass

         if number==2:
          if 'value' in artist.values()==True:
             bool=True
         else:
             pass

         if number==3:
              if 'value' in album.values()==True:
                 bool=True
              else:
                   pass    
        return bool

#########################################
#מפה מתחילות הפונקציות
#########################################

#המשתמש מכניס שיר חדש אל תוך מערך השירים
def create_new_song(songsArray):
    print("would you like to create a new song?")
    choice=input()
    if choice=="yes":
       song_name= input("Enter name of song: ")
       artist_name=  input("input name of artist: ")
       album_name =input("Enter name of album: ")
       length=input("Enter length of song in seconds: ")
       songsArray.append(Song(song_name,artist_name,album_name,length))   

def createExitingSongs(songsArray):
     #יוצר 4 אובייקטים מסוג שיר
    S1=Song("alone","alan walker","all falls down",163)#1
    S2=Song("see you again","noroz","noroz is on fire",250)#2
    S3=Song("all falls down","alan walker","all falls down",163)#3
    S4=Song("Diamond heart","alan walker","all falls down",163)#4
    songsArray.append(S1)
    songsArray.append(S2)
    songsArray.append(S3)
    songsArray.append(S4)

def songList():
     #מדפיס את רשימת השירים
     print("Do you want to see the song lisg?")
     choice=input()
     if choice=="yes":
       for x in songsArray:
        print(x.get_name_of_song())

def play():
    print("Would you like to play a song?")
    choice=input()
    if choice=="yes":
        songName=input("Which song would you like to play?")
        print (songName)
        print("playing...")

def info():
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

if __name__ == "__main__":

    ###תחילת עבודה
    
    print("welcome") 
     #יוצר מערך שירים

    songsArray=[]
    exit=False
    while exit==False:
         #המשתמש יוצר שיר אשר נכנס למערך
        create_new_song(songsArray)

        #המחשב יוצר אוטומתית שירים למערך
        createExitingSongs(songsArray)

        #מדפיס את רשימת השירים הקיימים במערך
        songList()

        #מפעיל שיר שהמשתמש בחר
        play()

        #שואל את המשתמש מה ברצונו לעשות(לנגן שיר,לקבל מידע על שיר)
        info()

        print("Would you like to exit?")
        choice=input()
        if choice=="yes":
            exit=True
        
    
   
     
        
        
        

    
