
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
