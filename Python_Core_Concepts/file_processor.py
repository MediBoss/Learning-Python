"""
Important methods: 

open(text_file) -> opens a textfile
close() - closes a text file
readline() - reads one line
readlines() - reads multiple lines
linecach.getline(text_file, line_of_textfile) = gets a line from the text file given the number
string.split() = split sentence into words

"""
import os

def main():
    
    # good practice to handle error that could happen when opening/closing a file object
    try:
        # when opened with the with statement, no need to close the file object
        with open("user_info.txt","r") as file_one:
            # file modes : r(read),w(write), a(append), r+(read and write)
            for line in file_one:
             print line
            
    except IOError:
        print "Error 404 : File Not Found"

if __name__ == "__main__":
    main()
