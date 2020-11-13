import math


class Song:
    def __init__(self, name, artist, album, length):
        self.name = name
        self.artist = artist
        self.album = album
        self.length = int(length)
        
    def print_details(self):
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
