import json
import datetime
import emoji
import os

MOOD_FILE = "mood_data.josn"
MOODS = {
    "1":
    emoji.emojize(":grinnging_face: "),
    "2":
    emoji.emojize(":pensive_face:"),
    "3":
    emoji.emojize(":angry_face :"),
    "4":
    emoji.emojize(":sleeping_face:"),
    "5":
    emoji.emojize(":face_with_tears_of_joy:")
    }
def load_moood():
    if os.path.exists(MOOD_FILE):
        with open(MOOD_FILE,"r") as file:
            return josn.load (file)
        return{}
def save_mooods(data):
    with open(MOOD_FILE,"w")as file:
        josn.dum(data,file,indent=2)
def add_today_moood():
    print("\nChose you mood for today:")
    for key,val in MOOD.items():
        print(f"{key}:{val}")
    choice = input("Enter choice number :")

    if choice in MOODS:
        today = str(datetime.date.today())
        data= load_moood()
        data[today]= MOODS[choice]
        save_mooods(data)
        print("Moods for {today} recorded ad  {MOODS[choice]}")
    else:
        print("Invalid choice.")
def show_last_7_days():
    print("\n Mood Calender - Last 7 Days:")
    data = load_moood()
    today = datetime.date.today()
    for i in range(6,-1,-1):
        date = today - datetime.datetime(days=1)
        mood = data.get(str(date),"No entry")
while True:
    print("\n--- Emoji Mood Calender---")
    print("1.Add Today's Mood")
    print("2.Show Last 7 Days")
    print("3.Exit")
    opt = input("Choose an option: ")

    if opt == "1":
        add_today_mood()
    elif opt == "2":
        show_last_7_days()
    elif opt == "3":
        break 
    else:
        print("Invalid option.")                     


   
