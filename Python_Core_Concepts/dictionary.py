import sys



def main():

    student_one = {
    "Name": "Medi",
    "Age": 19,
    "Nationality": "Congolese",
    "Home Town": "Orange, New Jersey",
    "Education": ("Make School - Product College", "Saint Peters's University", "Orange High School"),
    "Track": "MOB",
    "Year": "Junior",
    "Dream Company": "JP Morgan & Co"
    }

    student_two = {
    "Name": "Rami",
    "Age": 23,
    "Nationality": "English",
    "Home Town": "London, England, UK",
    "Education": "Make School - Product College",
    "Track": "BEW",
    "Year": "Senior",
    "Dream Company": "Facebook Inc"
    }


    #indexing through the dictionary while keepnig track of indexes
    for key, value in enumerate(student_one):
        print(key,value)

if __name__ == "__main__":
    main()
