from tkinter.messagebox import askyesno
import sys

class cmdArchiver():
    def onEncode(archiveFormatType,archiveFileLocation):
        if askyesno("Warning!","You are about to overwrite"+archiveFileLocation+",are you sure you would like to continue?"):
            rd = open(archiveFileLocation,'r')
            for each_line in rd:
                encodedFile = each_line.encode(archiveFormatType)
                wd = open(archiveFileLocation,'w')
                wd.write(str(encodedFile))
        else:
            sys.exit("User aborted operation!")
    def onDecode(archiveFormatType,archiveFileLocation):
        try:
            rd = open(archiveFileLocation,'r')
            for each_line in rd:
                byteData = bytes(each_line,archiveFormatType)
                decodedFile = each_line.decode(archiveFormatType)
                wd = open(archiveFileLocation,'w')
                wd.write(decodedFile)
        finally:
            print("error:could not recognize unicode character!")
    if __name__ == "__main__":
        aoru = input("Archive or Unarchive? >>")
        fileLocation = input("File Location >>")
        print("Types:\tutf8,\tutf16,\tlatin1")
        archiveType = input("Archive Type >>")
        if aoru == "Archive":
            onEncode(archiveType,fileLocation)
        elif aoru == "Unarchive":
            onDecode(archiveType,fileLocation)
