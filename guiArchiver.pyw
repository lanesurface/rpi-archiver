from tkinter import *
from archiver import cmdArchiver
import tkinter.filedialog

archiveTypes = ["utf8","utf16","latin1"]

class archiveViewer():
    def onArchiveRequest(archiveFormatType,archiveFileLocation):
        cmdArchiver.onEncode(archiveFormatType,archiveFileLocation)
    def onUnarchiveRequest(archiveFormatType,archiveFileLocation):
        cmdArchiver.onDecode(archiveFormatType,archiveFileLocation)
    def onArchiveFormatRequest(self):
        pick = self.var.get()
        print("Archive Format: "+pick)
    def onBrowse(self,ent):
        filename = tkinter.filedialog.askopenfilename()
        if filename:
            ent.delete(0,END)
            ent.insert(0,filename)
    def __init__(self):
        root = Tk()
        root.title("RPi-Archiver")
        #frames
        labelFrame = Frame(root)
        entryFrame = Frame(root)
        radiobuttonFrame = Frame(root)
        #labels and buttons
        butt_archive = Button(root,text="Archive",
                              command=(lambda:archiveViewer.onArchiveRequest(self.var.get(),
                                                               entry_fileLocation.get())))
        butt_unarchive = Button(root,text="Unarchive",
                                command=(lambda:archiveViewer.onUnarchiveRequest(self.var.get(),
                                                                   entry_fileLocation.get())))
        butt_browse = Button(entryFrame,text="Browse",command=(lambda:archiveViewer.onBrowse(self,entry_fileLocation)))
        label_fileLocation = Label(labelFrame,text="File Location: ",width=15)
        entry_fileLocation = Entry(entryFrame,width=25)
        #radio buttons
        self.var = StringVar()
        for archiveType in archiveTypes:
            Radiobutton(radiobuttonFrame,text=archiveType,
                                             command=self.onArchiveFormatRequest,
                                             variable=self.var,value=archiveType).pack(side=TOP)
        self.var.set(archiveType)
        #pack items
        butt_archive.pack(side=BOTTOM,fill=X)
        butt_unarchive.pack(side=BOTTOM,fill=X)
        radiobuttonFrame.pack(side=BOTTOM)
        labelFrame.pack(side=LEFT)
        entryFrame.pack(side=RIGHT)
        label_fileLocation.pack(side=RIGHT,fill=X)
        entry_fileLocation.pack(side=LEFT)
        butt_browse.pack(side=RIGHT)
        #initilize root
        root.mainloop()
archiveViewer()
