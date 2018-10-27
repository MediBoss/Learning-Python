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
    try:
        file_one = open("user_info.txt","r")
        for line in file_one:
            print line

        file_one.close()

    except IOError:
        print "Error 404 : File Not Found"

if __name__ == "__main__":
    main()
