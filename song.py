import random, os
song_list = 'E:\\songs'
songs = os.listdir(song_list)
song = random.randint(0,len(songs))
#Print the name of the song
print(songs[song])  
os.startfile(os.path.join(song_list, songs[0])) 
