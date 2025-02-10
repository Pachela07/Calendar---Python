"""Basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event """

# Module imports 
from time import sleep, strftime
import os

USER_NAME = "Dholglas Rodrigues"

# Empty dictionary for the calendar 
calendar = {}


# Function to clear the screen
def clear():
  os.system("cls" if os.name == "nt" else "clear")


# Welcome function 
def welcome():
  print(f"Welcome {USER_NAME}")
  print("...")
  sleep(2)
  print(" The Calender is Opening:")
  sleep(5)
  print("...")


# Function to show the date
def show_date():
  # Using strftime to speed up the program
  new_date = strftime("%d/%m/%Y %H:%M:%S")
  print(new_date)
  print("...")
  sleep(3)
  print("What would you like to do?")


# Function to update the calendar
def update():
  event_date =  input(" What date would you like to update? ")
  print("...")
  update = input("Enter the update: ")
  calendar[event_date] = update
  sleep(2)
  print("Update successful")
  print("...")
  print(calendar)

# Calendar functionability 
def start_calendar():
  welcome()
  show_date()
  # Variable to control the while loop
  start = True

  while start:
    sleep(3)
    clear()
    print("A - to add an event")
    print("U - to update an event")
    print("D - to delete an event")
    print("V - to view the calendar")
    print("E - to exit the calendar")
    print("...")
    user_choice = input("Enter your choice: ").upper()

    if user_choice == "V":
      print(calendar)
      # Check if the calendar is empty
      if not calendar:
        print("The calendar is empty")
      else:
        print(calendar)
    elif user_choice == "U":
      update()

    elif user_choice == "A":
      print("...")
      event = input("Enter the event: ")
      event_date = input("Enter the date: (dd/mm/yyyy): ")
      # Check if the date is in the correct format
      if len(event_date) != 10 or event_date[2] != "/" or event_date[5] != "/":
        print("Invalid date format")
      else:
      # Add the event to the calendar
        calendar[event_date] = event
        print("Event added successfully")

    elif user_choice == "E":
      # Exit the calendar
      start = False
      sleep(2)
      print("Goodbye!")

    elif user_choice == "D":
      print("...")
      # Check if the calendar is empty
      if not calendar:
        print("The calendar is empty")
      else:
        event = input("Enter the event: ")
        # Delete the event
        # Use a for loop to check if the event is in the calendar
        for date, event in calendar.items():
          # Check if the event is in the calendar
          if event == event:
            # Delete the event
            del calendar[date]
            print("Event deleted successfully")
            break
          else:
            print("Event not found")

    else:
      print("Invalid choice. Please try again.")

# Start the f.- calendar
start_calendar()
