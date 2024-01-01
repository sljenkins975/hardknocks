from tkinter import *
from pytube import YouTube
import os

root = Tk()
root.geometry('720x300')
root.resizable(0,0)
root.title("youtube video downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

##enter link
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
# Remove text from label

def remove_text():
    label.config(text="")
##function to download
def Downloader(): 
    
    url =YouTube(str(link.get()))
    print("link_enter: ",url)
    print("link: ",link)
    video = url.streams.filter(progressive = True, file_extension = "mp4").first().download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 250)  

##function to download
def audio():     
    print("Title: ",link_enter)
    print("Title: ",link)
    url =YouTube(str(link.get()))
    audio = url.streams.filter(only_audio=True).first()
    
    # # save the file
    # base, ext = os.path.splitext(audio)
    # new_file = base + '.mp3'
    # os.rename(audio, new_file)
    # Label(root, text = 'audio', font = 'arial 15').place(x= 180 , y = 250)  

Button(root,text = 'Video', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
Button(root,text = 'Audio only', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = audio).place(x=180 ,y = 200)
root.mainloop()
