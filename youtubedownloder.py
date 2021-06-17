from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.font import BOLD
from pytube import YouTube



folder_name=""

#filelocaion
def openlocation():
    global folder_name
    folder_name=filedialog.askdirectory( )#ask for directory pop up
    if(len(folder_name)>1):
        locerror.config(text=folder_name,fg="green")

    else:
        locerror.config(text="please choose the folder",fg="red")


#downloading video
def download():
    choice=ytdchoices.get()#get the choices given
    url=ytdentry.get()#get the url from frontend
    
    if(len(url)>1):#if the url is given
        ytderror.config(text="")#error message to null
        yt=YouTube(url)#create object of youtube and pass url

        if(choice==choices[0]):
            select=yt.streams.filter(progressive=True).first()
            
        elif(choice==choices[1]):
            select=yt.streams.filter(progressive=True).get_by_resolution()
            
        elif(choice==choices[2]):
            select=yt.streams.filter(progressive=True,file_extension="mp4").last()
           
        elif(choice==choices[3]):
            select=yt.streams.filter(only_audio=True).first()
           git 
        else:
            ytderror.config(text="paste the link again",fg="red")

    #download function
    select.download(folder_name)
    ytderror.config(text="Download completed")







root=Tk()
root.title("youtube downloader")
root.geometry("350x400")#window size
root.grid_columnconfigure(0,weight=1)#set all content in center


#youtube link label
ytdlabel=Label(root,text="enter the Url of the video",font=("jost",15))
ytdlabel.grid()


#entry box
ytdentryvar=StringVar()#getting url in string format
ytdentry=Entry(root,width=50,textvariable=ytdentryvar )
ytdentry.grid()

#error msg
ytderror=Label(root,text="error mgs",fg="red",font=("josh",10))
ytderror.grid()


#saving lovation
savelabel=Label(root,text="select the location",font=("josh",10,BOLD))
savelabel.grid()


#btn for saving

saveentry=Button(root,width=10,bg="red",fg="white",text="choose path",command=openlocation)
saveentry.grid()

#error message location
locerror=Label(root,text="path invalid",fg="red",font=("josh",10))
locerror.grid()

#download quality
ytdqual=Label(root,text="select quality",font=("josh",10))
ytdqual.grid()

#combobox
choices=["1080p","720p","144p","audio only"]
ytdchoices=ttk.Combobox(root,value=choices)
ytdchoices.grid()

#download btn

downloadbtn=Button(root,width=10,text="Download",bg="red",fg="white",font=("josh",10),command=download)
downloadbtn.grid()






root.mainloop()