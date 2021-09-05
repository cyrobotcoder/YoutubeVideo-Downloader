import tkinter as tk
from tkinter import*
from pytube import YouTube
from PIL import Image, ImageTk

tkinter = tk.Tk()
# Function to download youtube video
def Youtubedownload():
    yt = YouTube(y.get())
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Downloaded")

tkinter.title("Youtube Downloader")

#BACKGROUNG IMAGE
canvas = tk.Canvas(tkinter, width=450, height=200)
img = ImageTk.PhotoImage(Image.open("unnamed.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()

# Heading
x = tk.Label(tkinter, text="Youtube Downloader", fg="black", bg="red",font=("Bahnschrift", 20))
x.pack(ipady=20,pady=30)

# Label
urllable = tk.Label(tkinter, text="Enter URL:",font=("Bahnschrift", 10))
urllable.pack()

# Url Entry
y = tk.Entry(tkinter, width=50, bg="white", fg="black",borderwidth=2, relief="solid")
y.pack(ipady=10,pady=10)

# Download Button
b = tk.Button(tkinter, text="Download", command=Youtubedownload,width=16, height=4, bg="red", fg="white",borderwidth=2, relief="solid")
b.pack(pady=20)

#Exit Button
quitbutton = tk.Button(tkinter,text="Quit",width=8,height=2,bg="green",command=tkinter.quit,borderwidth=2, relief="solid")
quitbutton.pack(pady=20)

tkinter.mainloop()

