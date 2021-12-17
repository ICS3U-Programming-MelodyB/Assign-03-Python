#!/usr/bin/env python3
# Created by: Melody Berhane
# Created on: Dec 10, 2021
# This program asks the user for the number of classes held
# and the number they attened to determine if they can write the final exam.


def ask_again():
    # Get number of classes and attenance from student
    ask_to_play = (input("\033[1;36;38mwould you like to play again(y/n): "))
    if ask_to_play == "Y" or ask_to_play == "y":
        main()
    elif ask_to_play == "N" or ask_to_play == "n":
        print("Thank you for using my app!")
    else:
        print("Please enter either y/n")
        ask_again()



def main():
    # Prints Hello
    print("\033[1;36;39mHello")
    # Get number of classes and attenance from student
    student_name = (input("\033[1;36;38mPlease enter the students name: "))
    number_of_classes_string = input("\033[1;32;38mPlease enter the number of classes held: ")
    number_of_classes_attended_string = input("\033[1;33;38mPlease enter the number of classes the student has attended:")
    try:
        #Casting strings to integers
        number_of_classes_number = int(number_of_classes_string)
        number_of_classes_attended_number = int(number_of_classes_attended_string)
        print()
        # Calculate the percentage 
        attendance_percentage = (number_of_classes_attended_number/number_of_classes_number)*100
        # Check to see if they got the right number or wrong
        if number_of_classes_attended_number > number_of_classes_number:
            print("\033[1;36;39mPlease try again it looks like you attend more classes than were offered")
        elif attendance_percentage >= 75:
            print(student_name, "attended {:.0f}% of your classes".format(attendance_percentage))
            print("They can write the exam!")
        else:
            print(student_name, "attended {:.0f}% of your classes".format(attendance_percentage))
            print("They can't write the exam.")
    except Exception:
        print("\033[1;35;38mThese are not an integer")
    ask_again()
    print()

if __name__ == "__main__":
    main()
