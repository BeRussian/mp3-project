class Song:
    def __init__(self, name, artist, album, length):
        self.name = name
        self.artist = artist
        self.album = album
        self.length = int(length)
        
        if self.isIn(1,self.name,songs,artist,album)==False:
            songs[len(songs)+1]=self.name
        if  self.isIn(2,self.artist,songs,artist,album)==False:
            songs[len(songs)+1]=self.name
        if  self.isIn(3,self.album,songs,artist,album)==False:
            songs[len(songs)+1+1]=self.name

# HW: fix... s.get_name_of_song() == s.name
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
    def get_length(self):
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
