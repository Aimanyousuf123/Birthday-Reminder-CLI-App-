
from datetime import date, datetime
print ("________________________________")
print ("WELCOME TO BIRTHDAY REMINDER APP")
print ("________________________________")
while True:
    print ("1. Add Birthday")
    print ("2. Check today's Birthday")
    print ("3. View all Birthdays")
    print ("4. Exit")

    choice = input("Choose any one from above options (1,2,3,4) : ")
    print ("You selected", choice)

    if choice == "1" :
        print ("you chose to add birthday!")
        name = input("Add name: ")
        birth_date = input("Add Date of Birth in format YYYY-MM-DD:")

        with open("birthdays.txt", "a") as file: 
            file.write(f"{name},{birth_date}\n")
    
    elif choice == "2":
        today = date.today()
        today_month = today.month
        today_day = today.day
        found = False 

        try:
            with open("birthdays.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    name, birth_date_str = line.strip().split(",")
                    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
                    if birth_date.month == today_month and birth_date.day == today_day:
                        print(f"🎉 It's {name}’s birthday today!")
                        found = True

                if not found:
                    print("No birthdays today.")

        except FileNotFoundError:
            print("No birthdays file found.")

    elif choice == "3":
        with open("birthdays.txt", "r") as file:
            for line in file:
                print(line.strip())
    
    elif choice == "4" :
        print ("BYE!")
        break

    else:
        print ("choose any other option.")
