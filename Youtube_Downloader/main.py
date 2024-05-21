from pytube import YouTube
from sys import argv

url=argv[1]                         # argument at index[1] in terminal is url of video 

try:
    ytv=YouTube(url) 
except:
    print("Connection Error")

Duration=round(ytv.length/60,2)     #Converting seconds into minutes

print("Title:",ytv.title )          #-> Gives title of video
print("Channel:",ytv.author)        #-> Gives channel name   
print("Duration:",Duration,"mins")  #-> Gives length of video
print("Views:",ytv.views)           #-> Gives total views of video
print("Uploaded:",ytv.publish_date) #-> Gives date of upload

yd=ytv.streams.get_highest_resolution() # to get highest available resolution of video
try:
    yd.download("/Users/LEO/Desktop/Downloads") # destination location 
    print("Download Succesful")
except:
    print("Error! Try Again ")


