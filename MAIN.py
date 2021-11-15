import json
import random
import time
import sys

def login(username, signed_up):
    user_list = get_user_list()
    user_data = ""
    
    move_level = 0
    level = 0

    deleted = False
    
    if signed_up:
        level = 2
        history_username = ''
        print("Logged In Automatically.\n")
        time.sleep(0.1)
        
        user_data = get_user_info(username, user_list)

        
    else:
        print("Logging In!")
        
    while True:
        if level == 0:
            print("\nType 'ADMIN' to gain access to all accounts.")
            print("Type '<' to go back the the start menu.\n")
            username = get_username()
            history_username = username
            
            if username == 'q' or username == 'Q':
                print("Quitting...")
                sys.exit()
            elif username == '<':
                move_level = -1
                break
                    
            else:
                username_valid = check_username(username, user_list)
        
                if username_valid == True:
                    print("---Correct Username---")
                    move_level = 1
                else:
                    print("---Incorrect Username---")
                    move_level = 0

            user_data = get_user_info(username, user_list)

                    
        elif level == 1:
            
            memPIN = check_memPIN(username, user_list)
            if memPIN == False:
                if username == "ADMIN":
                    print("\nADMIN --> PIN = 'qwerty'.")
                    
                PIN = get_PIN()
                move_level = get_move_level_PIN(PIN)
                
                PIN_valid = False
                
                if PIN != '<':
                    PIN_valid = check_PIN(username, PIN, user_list)
                    
                if PIN_valid == True and PIN != '<':
                    print("---Correct PIN---")
                    print("Your account has been logged into.")
                    move_level = 1
                    
                    if username == 'ADMIN':
                        move_level = 0.5
                        
                elif PIN_valid == False and PIN != '<':
                    print("---Incorrect PIN---")
                    move_level = 0
                    
            elif memPIN == True:
                print("---Correct PIN---")
                print("Your account has been logged into.")
                move_level = 1
                if username == 'ADMIN':
                    move_level = 0.5
                    
                
        elif level == 1.5 and history_username == 'ADMIN':
            #ADMIN settings
            deleted = False
            history_username = "ADMIN"
            print_menu()
            print("As an admin user, you can access anyone's account:\n")
            username_info = get_admin_username_info()
            for i in username_info:
                print(i)
            
            username = get_admin_username()
            
            for list_username in username_info:
                if username ==  list_username:
                    if username == "":
                        move_level = 0
                    else:
                        move_level = 0.5
                        break
                else:
                    move_level = 0
                    
            if move_level == 0:
                if username == "<":
                    print("Logging Out...")
                    move_level = -1.5
                elif username == "q":
                    print("Quitting...")
                    
                    sys.exit()
                else:
                    print("Please try again.")
                    
                    username = "ADMIN"
                  
        elif level == 2:
            option = get_option(history_username)
            move_level = get_move_level_option(option, history_username)
            
        elif level == 2.5:
            if history_username == "ADMIN":
                move_level = 0.5
                
            else:
                print("To access settings, you will need to type in your PIN for security.")
                PIN_valid = False
                while PIN_valid == False:
                    PIN = get_PIN()
                    if PIN == "<":
                        move_level = -0.5
                        break
                    elif PIN == "q":
                        print("Quitting...")
                        sys.exit()
                    else:
                        PIN_valid = check_PIN(username, PIN, user_list)
                    
                        if PIN_valid == True:
                            print("---Correct PIN---")
                            print("You can now access settings.")
                            move_level = 0.5
                            break
                        else:
                            print("---Incorrect PIN---")
                        
            history_level = level
            
        elif level == 3:
            #user_settings_decision = get_user_settings_decision(history_username, username)

            #user_list = get_userlist_info(username)
            #list_counter = get_list_counter_info(username)
            
            
            #move_level = check_user_settings_decision(user_settings_decision, history_username, username)
            move_level = 1
            
            user_data = get_user_info(username, user_list)

        elif level == 3.5:
            move_level = delete_user(user_data, user_list)
            deleted = True

        elif level == 4:
            print_settings_categories(username)
            
            username_info = user_data["Username"]
            PIN_info = user_data["PIN"]
            age_info = user_data["Age"]
            score_info = user_data["Score"]
            funfact_info = user_data["Fun Fact"]
            memPIN_info = user_data["Remember PIN"]
            
            #Get settings number
            settings_number = get_settings_number(history_username)
            move_level = move_level_settings_number(settings_number, history_username)
            
        elif level == 4.1:
            category = username_info
            category_type = 'Username'
            move_level = 0.9
            
        elif level == 4.2:
            category = PIN_info
            category_type = 'PIN'
            move_level = 0.8

        elif level == 4.3:
            category = age_info
            category_type = 'Age'
            move_level = 0.7
            
        elif level == 4.4:
            category = score_info
            category_type = 'Score'
            move_level = 0.6
            
        elif level == 4.5:
            category = funfact_info
            category_type = 'Fun Fact'
            move_level = 0.5

        elif level == 4.6:
            category = memPIN_info
            category_type = 'Remember PIN'
            move_level = 0.4
        
        elif level == 5:
            
            #See what the user wants to change it to
            change_to = get_change_to(category)
            
            changeto_movelevel = check_change_to(username, PIN, category_type, category, change_to, user_list, user_data, history_username)
            
            change_to = changeto_movelevel[0]
            move_level = changeto_movelevel[1]
            username = changeto_movelevel[2]
            PIN = changeto_movelevel[3]

            
        elif level == 6:
            move_level = double_check_with_user()
            
        elif level == 7:
            
            run_change_to(category_type, user_list, user_data, change_to)
            
            user_list = get_user_list()
            user_data = get_user_info(username, user_list)
            
            move_level = -3
            
        elif level == 8:
            move_level = 1
            
            if deleted == False:
                print("\nWhat the settings look like now:")
                print_send_data(username)
            else:
                print("")
                
        elif level == 9:

            move_level = get_another_go_move_level(history_username, deleted)
            
        elif level == 9.5:
            read_quiz_data(username, history_username)
            move_level = -0.5
            
        elif level == 10:
            #Play Quiz
            move_level = 2
            break

        else:
            if level < 0:
                print("Error: level is less than 0")
                level = 0
                move_level = 0
                break
            else:
                print("Error: level not an option (FIX)")
                print(move_level)
                break
                
        level = move_level + level


    return_package = [move_level, user_data, user_list]


    return return_package


def get_admin_username():
    username = input("Who's username would you like to access?\n")
    return username

def get_admin_username_info():
    username_info_print = ""
    user_list = get_user_list()
    list_counter = -1
    for user in user_list:
        list_counter += 1

        #Info for checking later
        username_info = user["Username"]

        username_info_print = username_info + ";" + username_info_print
        
    username_info = username_info_print.split(";")

    return username_info

def get_username():
    #Asks user for input
    username = input("Type in your username:\n")
    return username

def get_PIN():
    PIN = input("Type in your PIN:\n")
    return PIN

def check_memPIN(username, user_list):
    #Checks users info against database
    memPIN = False

    #Check user ID in data        
    for user in user_list:
        username_info = user["Username"]
        if username_info == username:
            memPIN_info = user["Remember PIN"]
            if memPIN_info == "True":
                memPIN = True

    return memPIN

def check_username(username, user_list):
    #Checks users info against database
    username_valid = False

    #Check user ID in data        
    for user in user_list:
        username_info = user["Username"]
        if username_info == username:
            username_valid = True

    return username_valid

def check_PIN(username, PIN, user_list):
    #Checks users info against database
    PIN_valid = False
    #Check user ID in data        
    for user in user_list:
        username_info = user["Username"]
        if username_info == username:
            PIN_info = user["PIN"]
            if PIN_info == PIN:
                PIN_valid = True

    return PIN_valid

def get_move_level_PIN(PIN):
    if PIN == '<':
        print("Back...")
        
        move_level = -1
    elif PIN == 'q':
        print("Quitting...")        
        sys.exit()
        
    else:
        move_level = 1

    return move_level

def get_user_list():
    # Get data from file
    user_list = []
    with open("%") as user_info:
        for jsonObj in user_info:
            #Creates a python dictionary out of json file
            user_dict = json.loads(jsonObj)
            #Creates a list out for the user dictionary
            user_list.append(user_dict)

    return user_list


#---------------------------------------#
def get_list_counter_info(username):
    user_list = get_user_list()
    list_counter = -1
    for user in user_list:
        list_counter += 1

        #Info for checking later
        username_info = user["Username"]
        
        if username_info == username:
            break

    return list_counter


def get_username_info(username):
    user_list = get_user_list()
    list_counter = -1
    for user in user_list:
        list_counter += 1

        #Info for checking later
        username_info = user["Username"]
        
        if username_info == username:
            break

    return username_info

###############################################################################################
def get_user_info(username, user_list):                                                       #
    list_counter = -1                                                                         #
    for user in user_list:                                                                    #
        list_counter += 1                                                                     #
                                                                                              #
        #Info for checking later                                                              #
        username_info = user["Username"]                                                      #
        user_data = user                                                                      #
                                                                                              #
        if username_info == username:                                                         #
            break                                                                             #
                                                                                              #
    return user_data                                                                          #
###############################################################################################

def get_score_info(username):
    user_list = get_user_list()
    list_counter = -1
    for user in user_list:
        list_counter += 1

        #Info for checking later
        username_info = user["Username"]
        score_info = user["Score"]
        
        if username_info == username:
            break

    return score_info

def get_PIN_info(username):
    user_list = get_user_list()
    list_counter = -1
    for user in user_list:
        list_counter += 1

        #Info for checking later
        username_info = user["Username"]
        PIN_info = user["PIN"]
        
        if username_info == username:
            break

    return PIN_info


def get_funfact_info(username):
    user_list = get_user_list()
    list_counter = -1
    for user in user_list:
        list_counter += 1

        #Info for checking later
        username_info = user["Username"]
        funfact_info = user["Fun Fact"]
        
        if username_info == username:
            break

    return funfact_info


def get_age_info(username):
    user_list = get_user_list()
    list_counter = -1
    for user in user_list:
        list_counter += 1

        #Info for checking later
        username_info = user["Username"]
        age_info = user["Age"]
        
        if username_info == username:
            break

    return age_info

def get_memPIN_info(username):
    user_list = get_user_list()
    list_counter = -1
    for user in user_list:
        list_counter += 1

        #Info for checking later
        username_info = user["Username"]
        memPIN_info = user["Remember PIN"]
        
        if username_info == username:
            break

    return memPIN_info

#----------------------------------------#

def print_settings_categories(username):
    user_list = get_user_list()
    list_counter = -1
    for user in user_list:
        username_info = user['Username']
        
        #Info for printing later
        heading1 =  "Option Number"

        #Number of spaces after heading 1 after the
        space1 = ""
        for i in range(len(heading1)-3):
            space1 += " "
            
        username_key = "|Username:"
        PIN_key = "|PIN:"
        age_key = "|Age:"
        score_key = "|Score:"
        funfact_key = "|Fun Fact:"
        memPIN_key = "|Remember PIN:"

        heading2 = "Option Type"
        
        key_list = [username_key, PIN_key, age_key, score_key, funfact_key, memPIN_key, heading2]
        longest_key = max(key_list, key=len)

        for i in range(len(longest_key)-len(username_key)+1):
            username_key += " "
        username_key += "|'"

        for i in range(len(longest_key)-len(PIN_key)+1):
            PIN_key += " "
        PIN_key += "|'"

        for i in range(len(longest_key)-len(age_key)+1):
            age_key += " "
        age_key += "|'"

        for i in range(len(longest_key)-len(score_key)+1):
            score_key += " "
        score_key += "|'"

        for i in range(len(longest_key)-len(funfact_key)+1):
            funfact_key += " "
        funfact_key += "|'"

        for i in range(len(longest_key)-len(memPIN_key)+1):
            memPIN_key += " "
        memPIN_key += "|'"

        space2 = ""
        for i in range(len(heading2)-len(longest_key)):
            space2 += " "

        for i in range(len(longest_key)-len(heading2)):
            heading2 += " "
        
        username_val = user["Username"]
        PIN_val = user["PIN"]
        age_val = user['Age']
        score_val = user["Score"]
        funfact_val = user["Fun Fact"]
        memPIN_val = user["Remember PIN"]
        
        
        heading3 = "Option Value"
        
        values_list = [username_val, PIN_val, age_val, score_val, funfact_val, memPIN_val, heading2]
        longest_val = max(values_list, key=len)
        
                
        username_print = "|(1)"+space1+ username_key + space2 +username_val + "'"
        PIN_print = "|(2)"+space1+ PIN_key + PIN_val + space2 +"'"
        age_print = "|(3)"+space1+ age_key + age_val + space2 +"'"
        score_print = "|(4)"+space1+ score_key + score_val + space2 +"'"
        funfact_print = "|(5)"+space1+ funfact_key + funfact_val + space2 +"'"
        memPIN_print = "|(6)"+space1+ memPIN_key + memPIN_val + space2 +"'"

        
        total_heading = "|"+heading1+"|"+heading2 + "|" + heading3
        
        details_list = [username_print, PIN_print, age_print, score_print, funfact_print, memPIN_print, total_heading]
        longest_line = max(details_list, key=len)

        for i in range(len(longest_line)-len(username_print)):
            username_print += " "
        username_print += "|"
        
        for i in range(len(longest_line)-len(PIN_print)):
            PIN_print += " "
        PIN_print += "|"
        
        for i in range(len(longest_line)-len(age_print)):
            age_print += " "
        age_print += "|"
        
        for i in range(len(longest_line)-len(score_print)):
            score_print += " "
        score_print += "|"
        
        for i in range(len(longest_line)-len(funfact_print)):
            funfact_print += " "
        funfact_print += "|"
        
        for i in range(len(longest_line)-len(memPIN_print)):
            memPIN_print += " "
        memPIN_print += "|"
        
        for i in range(len(longest_line)-len(total_heading)):
            total_heading += " "
        total_heading += "|"
        
        horizontal_lines = ""
        
        for i in range(len(longest_line)-1):
            if len(horizontal_lines) == len(heading1):
                horizontal_lines += '+'
            elif len(horizontal_lines) == len(heading1)+len(heading2)+1:
                horizontal_lines += '+'
            else:
                horizontal_lines += '-'
            
        horizontal_lines = "+"+horizontal_lines+"+"
        
        if username == username_info:
            break
    print("\nHere are the categories you can change:")
    print(horizontal_lines)
    print(total_heading)
    print(horizontal_lines)
    print(username_print+"\n"+PIN_print+"\n"+age_print+"\n"+score_print+"\n"+funfact_print+"\n"+memPIN_print)
    print(horizontal_lines+"\n")
    
        
#------------------------------------------------------------------------------------------------------------------#
    
def get_option(history_username):
    print("\nUser Options:")
    print("Type 's' for user SETTINGS.")
    
    if history_username == "ADMIN":
        print("Type '<' to go BACK.")
        print("Type '>' to CONINUE (and see data on quiz)")
    else:
        print("Type '<' to go BACK (log out).")
        print("Type '>' to CONTINUE (and go to quiz options)")
        
    print("Type 'q' to Quit.")
    option = input()
    option = option.lower()
    
    return option

def read_quiz_data(username, history_username):
    with open("Quiz Statistics.txt") as statistics_file:
        ratio = statistics_file.readline()
        ratio = ratio.split(":")
        yes = ratio[0]
        no = ratio[1]
        
        total = int(yes) + int(no)

        
    print("\n"+str(total)+" votes in total.")
    print(str(yes)+" said they LIKED they liked the quiz.")
    print(str(no)+" said they DISLIKED the quiz.\n")

    all_likes = []
    all_improvements = []

    user_likes = []
    user_improvements = []
    
    if history_username == "ADMIN":
        print("Here are the likes and improvements from everyone:\n")
        print("LIKES:")
        with open("likes.txt") as likes_file:
            likes = False
            for line in likes_file:
                line = line.rstrip()
                all_likes.append(line)
                
            for item in all_likes:
                print(item)
                    
                
        if all_likes == []:
            print("(nothing)")

        print("\nIMPROVEMENTS:")
        with open("improvements.txt") as improvements_file:
            improvements = False
            for line in improvements_file:
                line = line.rstrip()
                all_improvements.append(line)
                
            for item in all_improvements:
                print(item)
                
        if all_improvements == []:
            print("(nothing)")
        print("")


    else:
        print("YOUR LIKES:")
        with open("likes.txt") as likes_file:
            likes = False
            for line in likes_file:
                line = line.rstrip()
                user_likes.append(line)
                
                for item in user_likes:
                    name = line.split(" ")
                    output = line.split(": ")
                    if name[0] == username:
                        print(output[1])
                        likes = True
                        break
                    
        if likes == False:
            print("(nothing)")
        
        print("\nYOUR IMPROVEMENTS:")
        with open("improvements.txt") as improvements_file:
            improvements = False
            for line in improvements_file:
                line = line.rstrip()
                user_improvements.append(line)
                
                for item in user_improvements:
                    name = line.split(" ")
                    output = line.split(": ")
                    if name[0] == username:
                        print(output[1])
                        improvements = True
                        break
                    
        if improvements == False:
            print("(nothing)")

        print("")
                
############################################################################################################################################################################################
def get_move_level_option(option, history_username):
    if option == 's':
        print("\nSettings:")
        move_level = 0.5
        
    elif option == '<':
        if history_username == "ADMIN":
            print("Back...")
            move_level = -0.5
            
        else:
            print("Logging Out...")            
            move_level = -2
            
    elif option == 'q':
        print("Quitting...")
        sys.exit()
        
    elif option == '>':
        print("Continue...")
        move_level = 7
        
    else:
        print("Please try again...")
        move_level = 0
        
    return move_level
############################################################################################################################################################################################
#-----------------------------------------------------------#
def get_user_settings_decision(history_username, username):
    print("\nSettings Options:")
    print("Type '>' to change Settings.")
    print("Type '<' to go back (log out).")
    
    if history_username == "ADMIN":
        print("Type 'd' to delete the account: '"+ username+"'.")
        
    print("Type 'q' to Quit.")
    
    user_settings_decision = input()
    user_settings_decision = user_settings_decision.lower()

    return user_settings_decision

def check_user_settings_decision(user_settings_decision, history_username, username):
    if user_settings_decision == '>':
        move_level = 1
        
    elif user_settings_decision == '<':
        print("Logging Out...")
        move_level = -4
    elif user_settings_decision == 'd' and history_username == 'ADMIN':
        while True:
            is_user_sure = input("Are you sure you want to delete the account: '"+username+"'? (y/n)\n")
            is_user_sure = is_user_sure.lower()
            if is_user_sure == 'y' or is_user_sure == '>':
                move_level = 0.5
                break
            elif is_user_sure == "n" or is_user_sure == "<":
                move_level = 0
                break
            else:
                print("Please try again.")
        
    elif user_settings_decision == 'q':
        print("Quitting...")        
        sys.exit()
        
    else:
        print("Please try again.")
        move_level = 0

    return move_level

def delete_user(user_data, user_list):
    while True:
        double_check = input("Are you sure?(y/n)\n")
        double_check = double_check.lower()
        if double_check == "y" or double_check == "yes":        
            print("Deleting user...")
            delete = True
            move_level = -2
            break
        
        elif double_check == "<" or double_check == "n" or double_check == "no":
            print("Back...")
            delete = False
            move_level = -0.5
            break
        
        else:
            print("Please try again.")
            
    if delete == True:
        #Removing your data (user_data) from 'user_list'...
        user_list.remove(user_data)

        #Deleting all contents of the 'user_info.txt' file...
        with open("user_info.txt", "w") as user_info:
            user_info.write("")

        #Appending the new 'user_list', line by line to 'user_info.txt' in JSON (JavaScript Object Notation) format...
        with open("user_info.txt", "a") as user_info:
            for part in user_list:
                json.dump(part, user_info)
                user_info.write("\n")
                
    return move_level
    

        
def get_settings_number(history_username):
    print("Options:")
    print("Type '<' to go back.")    
    if history_username == "ADMIN":
        print("Type 'd' to delete the account.")        
    print("Type 'q' to quit.")

    print("\nType in the number or letter of the option you want to change.")
    settings_number = input()
    settings_number = settings_number.lower()
    return settings_number


def move_level_settings_number(settings_number, history_username):
    if settings_number == '1':
        move_level = 0.1
        
    elif settings_number == '2':
        move_level = 0.2
        
    elif settings_number == '3':
        move_level = 0.3
        
    elif settings_number == '4':
        move_level = 0.4
        
    elif settings_number == '5':
        move_level = 0.5
        
    elif settings_number == '6':
        move_level = 0.6
        
    elif settings_number == '<':
        print("Back...\n")
        move_level = -2
        
    elif settings_number == 'q':
        print("Quitting...")
        sys.exit()
        
    else:
        if history_username == 'ADMIN':
            if settings_number == 'd':
                move_level = -0.5
            else:
                print("Please try again.")
                move_level = 0
                
        else:
            print("Please try again.")
            move_level = 0
        
    return move_level
       
def get_change_to(category):
    change_to = input("Type in what you want to change '"+category+"' into:\n")
    return change_to

def double_check_with_user():
    while True:
        double_check = input("Are you sure? (y/n)")
        double_check = double_check.lower()
        
        if double_check == "y" or double_check == "yes":        
            print("Changing data...")
            move_level = 1
            break

        elif double_check == '<' or double_check == "n" or double_check == "no":
            print("Back...")
            move_level = -1
            break
        
        else:
            print("Please try again.")
            
    return move_level


def run_change_to(category_type, user_list, user_data, change_to):
        
    #Removing your data (user_data) from 'user_list'...
    user_list.remove(user_data)

    #Changing value of the '"+category_type+"' to '"+str(category)+"' to a variable called 'change_to'...
    user_data[category_type] = change_to

    #Appending changed dictionary (user_data) to user_list...
    user_list.append(user_data)

    #Deleting all contents of the 'user_info.txt' file...
    with open("user_info.txt", "w") as user_info:
        user_info.write("")

    #Appending the new 'user_list', line by line to 'user_info.txt' in JSON (JavaScript Object Notation) format...
    with open("user_info.txt", "a") as user_info:
        for part in user_list:
            json.dump(part, user_info)
            user_info.write("\n")
                


def check_change_to(username, PIN, category_type, category, change_to, user_list, user_data, history_username):
    
    move_level = 1
    
    if change_to == '<':
        print("Back...")
        move_level = -1
        
    else:
        if category_type == 'Remember PIN':
            if category == 'True':
                change_to = 'False'
            
            elif category == 'False':
                change_to = 'True'

            else:
                #User's Error
                change_to = "False"
                    
        elif category_type == 'Age':
            age = change_to
            try:
                int(age)
                integer = True
                
            except ValueError:
                print("Not an integer. Please Retype.")
                integer = False
                move_level = 0

            if integer == True:
                if int(age) > 121:
                    print("Too old.")
                    move_level = 0
                    
                elif int(age) < 9:
                    print("Too young.")
                    move_level = 0
            
        elif category_type == 'Username':
            new_username = change_to
            username_valid = check_newusername_valid(new_username, user_list)
            
            if len(new_username) > 15 or len(new_username) < 4:
                username_valid = False
                print("Invalid number of characters.")
            
            if username_valid == True:
                print("-Username Available-")
                username = new_username

            elif username_valid == False:
                print("-Username Unavailable-")
                move_level = 0
            
            
        elif category_type == 'PIN':
            new_PIN = change_to
            
            if len(new_PIN) < 4:
                
                while True:
                    PIN_length = input("Your PIN is too short. Are you sure you want to use this PIN? (y/n)\n")
                    PIN_length = PIN_length.lower()
                
                    if PIN_length == "y" or PIN_length == "yes":
                        break
                
                    elif PIN_length == "n" or PIN_length == "no":
                        print("Good choice. A secure PIN should be:\n1-Short enough to remember (more than 4 characters)\n2-Long enough so that a hacker can't guess it (less than 15 characters)")
                        move_level = 0
                        break
                
                    else:
                        print("Please try again.")
                        
            elif len(new_PIN) > 15:
                print("Your PIN is too long. Please try again.")
                move_level = 0
                
            else:
                PIN = new_PIN
                        
        elif category_type == 'Score':
            if history_username == "ADMIN":
                try:
                    int(change_to)
                except ValueError:
                    print("Not an integer. Please Retype.")
                    move_level = 0
            else:
                print("The score can only be changed when you play a game, not from settings.")
                move_level = 0

        elif category_type == 'Fun Fact':
            funfact = change_to
            if len(funfact) > 150:
                print("The character limit is 150, unfortunately.")
                move_level = 0



    changeto_movelevel = [change_to, move_level, username, PIN]
            
            
    return changeto_movelevel


def get_another_go_move_level(history_username, deleted):
    
    if history_username == 'ADMIN':
        print("\nOPTIONS:")
        if deleted == True:
            print("Type '1' to go back to list of usernames.")
            print("Type '2' to Log Out.")
            print("Type 'q' to QUIT.")
            print("Type 'QS' to see Quiz Statistics.")

        elif deleted == False:
            print("Type '1' to go back to settings options.")
            print("Type '2' to go back to list of usernames.")
            print("Type '3' to Log Out.")
            print("Type 'q' to QUIT.")
            print("Type 'QS' to see Quiz Statistics.")
    else:
        print("\nQUIZ OPTIONS:")
        print("Type '1' or '<' to Go Back.")
        print("Type '2' to Log Out.")
        print("Type 'q' to QUIT.\n")
        print("Type 'QS' to see Quiz Statistics.")
        print("Type 'P' to Play the Quiz.")
        
        
    another_go = input().lower()
    
    if another_go == '1' or another_go == "<":
        move_level = -7
        if history_username == 'ADMIN' and deleted == True:
            move_level = -7.5
        elif history_username == "ADMIN" and deleted == False:
            move_level = -5
            
    elif another_go == "2":
        print("Logging out...")        
        move_level = -9
        if history_username == 'ADMIN' and deleted == False:
            move_level = -7.5
                
    elif another_go == 'p' and history_username != "ADMIN":
        check = input("\nType '<' to go back to menu.\nPress enter to start quiz.\n").lower()

        if check == "<":
            move_level = 0
        else:
            move_level = 1

    elif history_username == 'ADMIN' and deleted == False and another_go == "3":
        print("Logging out...")
        move_level = -9
        
    elif another_go == 'q':
        print("Quitting...")        
        sys.exit()

    elif another_go == "qs":
        move_level = 0.5
        
    else:
        print("Please try again:")
        move_level = 0

        
    return move_level

        
#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------#
def signup():
    print("Signing Up!")
    #Note --> They can  write '<' to go back, '>' to skip something or 'q' to quit.
    level = 0.00
    move_level = 1.00
    user_list = get_user_list()
    while True:
        # Set level to next level by default 
        if level == 0.00:
            print("\nUsername Options:")
            print("Type '<' to go back to the main menu")            
            print("Type '>', to generate a random username.")
            print("Type 'q' to quit.\n")
            
            username = get_new_username()
            random_username = False
            move_level = get_move_level_username(username)
            
            if username == '<':
                break
            elif len(username) < 4 and username != ">":
                print("Not enough characters. Please retype.")
                move_level = 0
                
        elif level == 0.10:
            
            username_valid = check_username_valid(username, user_list)
            
            if username_valid == True:
                print("-Username Available-")
                print("\nYour username is set to '"+username+"'.\n")
                time.sleep(0.5)
                move_level = 0.90
            elif username_valid == False:
                print("-Username Unavailable-")
                move_level = -0.10
            
                    
        elif level == 0.20:
            username = generate_username()
            
            random_username = True
            move_level = -0.10

        elif level == 1.00:
            #2. Ask them whether they want a password or PIN and get PIN
            PIN_valid = False
            #Checking PIN_options to generate or ask for PIN
            PIN_options = get_PIN_options()
            
            move_level = move_level_PIN_options(PIN_options)

        elif level == 1.10:
            print_menu()
            
            PIN_gen_options = get_PIN_gen_options()
            move_level = move_level_PIN_gen(PIN_gen_options)
            
        elif level == 1.11:
            PIN = PIN_generator(PIN_gen_options)
            print("Your PIN is '"+PIN+"'.")
            time.sleep(0.5)
            move_level = 0.89

        elif level == 1.20:
            print_menu()
            PIN = get_signup_PIN()
            
            move_level = move_level_typed_PIN(PIN)
            
        elif level == 1.21:
            print("Your PIN is set to '"+PIN+"'.")
            time.sleep(0.5)
            move_level = 0.79
            
        elif level == 1.5:
            option = display_menu_school()
            move_level = check_option_school(option)
            typed = False
            generated = False
            if option == '<':
                print("Back...")
                move_level = -0.5
            elif option == '1' or option == 'check pin':
                while True:
                    password = get_password_school()
                    typed = True
                    generated = False
            
                    if password == "<":
                        print("Back...")
                        move_level = 0
                        break
                    elif password == ">":
                        print("Unavailable.")
                
                    elif password == 'c':
                        print("""\nCriteria:
For the PIN to be valid, it must follow most of the following criteria:
- Must be 8 - 24 charcters
- Can contain at least 1 upper case letter
- Can contain at least 1 lower case letter
- Can contain at least 1 digit
- Can contain 1 allowed symbol:
    !,$,^,&,*,(,),-,_,=,%,+
    The character space is not allowed.\n""")
                        
                    elif password == 'q':
                        print("Quitting...")
                        sys.exit()
                    else:
                        
                        move_level = check_password_school(password, typed, generated)
                        if move_level == -2:
                            print("Please type in the correct PIN.")
                            password = "Error"
                        else:
                            print("It seems your PIN is fine.")
                            move_level = 0.5
                            break
                        
                PIN = password

                        

            elif option == "2" or option == "generate pin":
                password = ''
                generated = True
                typed = False
                password = password_generator_main(move_level, typed, generated, password)
                PIN = password
                move_level = 0.5
                
            else:
                move_level = 0

                

        elif level == 2.00:
            #Ask age
            print_menu()
            age = get_age()
            move_level = move_level_age(age)
        elif level == 2.10:
            #Check Age
            age = check_age(age)
            move_level = move_level_check_age(age)
            
        elif level == 3.00:
            #9. Asks fun fact
            print_menu()
            fun_fact = get_fun_fact()
            move_level = move_level_fun_fact(fun_fact)
            fun_fact = check_fun_fact(fun_fact)

        elif level == 4.00:
            print("Your funfact '"+fun_fact+"' is valid.")
            #10. Tells them score and explains what it does
            score = show_score()
            move_level = 1.00

        elif level == 5.00:
            print_menu()
            #11. Asks them whether they want the computer to remember their ID with 'mem_ID'
            memPIN = get_memPIN()
            move_level = move_level_memPIN(memPIN)
            
        elif level == 6.00:
            #13. Creates a dictionary to send data
            data_send = create_data_send(username, PIN, age, score, fun_fact, memPIN)
            #Sends data to file
            send_data(data_send)
                            
            move_level = 1

            
        elif level == 7.00:
            #12. If they choose not to do this, they will be remined of their PIN/Password
            print("\nThe following data has now been sent to the 'user_info' file:")
            print_send_data(username)
            time.sleep(1)

            move_level = -1

            break
        
        else:
            if level < 0:
                print("Error: level is less than 0")
                level = 0
                move_level = 0
            else:
                print("Error: level not an option (FIX)")
                move_level = 0
                break
                
        
        # Go to next level
        move_level = float(move_level)
        
        level = move_level + level
        
        if level < 0:
            level = 0
            print("\nYou may have encountered an error.\n")

    signup_return_package = [move_level, username]    
            
    return signup_return_package
    


def get_move_level_username(username):
    if username == '>':
        print("Continue...")
                    
        print("\nYou will have a randomly generated username.")
        move_level = 0.20
        
    elif username == '<':
        print("Back...")
        
        move_level = -2
        
    elif username == 'q':
        print("Quitting...")     
        sys.exit()
        
    else:
        if len(username) > 15:
            print("This username is too long. Please try again.")
            move_level = 0

        else:
            print("Checking username...")
            move_level = 0.10
        
    return move_level
    
def get_new_username():
    username = input("Please type in your username:\n")
    return username

def check_username_valid(username, user_list):  
    for user in user_list:
        username_info = user["Username"]    
        if username_info == username:
            username_valid = False
            break
        else:
            username_valid = True
            if username == '':
                username_valid = False
                break
        
    return username_valid

def check_newusername_valid(new_username, user_list):   
    for user in user_list:
        username_info = user["Username"]    
        if username_info == new_username:
            username_valid = False
            break
        else:
            username_valid = True
            if new_username == '':
                username_valid = False
                break
        
    return username_valid

def get_user_list():
    user_list = []
    #Checks username against database
    with open("user_info.txt") as user_info:
        for jsonObj in user_info:
            user_dict = json.loads(jsonObj)
            user_list.append(user_dict)
    return user_list


def generate_username():
    animal_list = []
    with open("animal_list.txt") as animal_file:
        animals = animal_file.read()
        animal_list = animals.split()

    random.shuffle(animal_list)
    animal = animal_list[0]
        
    number = random.randint(10,99)
    str_number = str(number)
    
    username = animal+str_number
    
    return username

#-----------------------------------#
def print_menu():
    print("\nExtra Options:\nType '<' to go back;\nType '>' to skip ahead;\nType 'q' to quit.\n")

def get_PIN_options():
    print("PIN Options:")
    print("Type '<' to go back.")
    print("Type 'q' to quit.")
    print("Type '1' to make a randomly generated PIN.")
    print("Type '2' to type in your PIN of choice.")
    print("Type 's' to use the School method of writing the PIN.")
    PIN_options = input()
    return PIN_options


def move_level_PIN_options(PIN_options):
    if PIN_options == '1':
        #Generate PIN
        move_level = 0.10
        
    elif PIN_options == '2':
        #Ask user for PIN
        move_level = 0.20
        
    elif PIN_options == '<':
        print("Back...")
        
        move_level = -1.00
                    
    elif PIN_options == '>':
        print("Continue...")
        
        move_level = 0.10
                    
    elif PIN_options == 'q':
        print("Quitting...")
        
        sys.exit()
    elif PIN_options == "s":
        print("You can do the PIN in school fashion.")
        move_level = 0.5
            
    else:
        print("Please try again...")
        move_level = 0.00
        
    return move_level

def get_signup_PIN():
    PIN = input("Type in your PIN here:")
    return PIN
        
def move_level_typed_PIN(PIN):
    if PIN == '<':
        print("Back...")
        
        move_level = -0.20
        
    elif PIN == '>':
        #Doesn't work for some stupid reason
        print("Continue...")
        
        move_level = -0.0999999999999999
        
    elif PIN == 'q':
        print("Quitting...")
        
        sys.exit()
        
    else:
        if len(PIN) < 4:
            while True:
                PIN_length = input("Your PIN is too short. Are you sure you want to use this PIN? (y/n)\n")
                PIN_length = PIN_length.lower()
                
                if PIN_length == "y" or PIN_length == "yes":
                    move_level = 0.01
                    break
                
                elif PIN_length == "n" or PIN_length == "no":
                    print("Good choice. A secure PIN should be:\n1-Short enough to remember (more than 4 characters)\n2-Long enough so that a hacker can't guess it (less than 15 characters)")
                    move_level = 0.00
                    break
                
                else:
                    print("Please try again.")
        elif len(PIN) > 15:
            print("Your PIN is too long. Please try again.")
            move_level = 0

            
        else:
            move_level = 0.01

    return move_level
    
def PIN_generator(PIN_gen_options):
    #The number of each option.
    if PIN_gen_options == '1':
        #length = 6
        num_UPPER_letters = 0
        num_lower_letters = 2
        num_numbers = 4
        num_special_chars = 0
        
    elif PIN_gen_options == '2':
        #length = 8
        num_UPPER_letters = 2
        num_lower_letters = 2
        num_numbers = 3
        num_special_chars = 1
        
    elif PIN_gen_options == '3':
        #length = 10
        num_UPPER_letters = 3
        num_lower_letters = 2
        num_numbers = 3
        num_special_chars = 2


    #Get letters needed for password
    UPPER_letter = get_UPPER_letter(num_UPPER_letters)
    lower_letter = get_lower_letter(num_lower_letters)
    number = get_number(num_numbers)
    special_char = get_special_char(num_special_chars)    

    #Concatenate
    PIN = UPPER_letter + lower_letter + number + special_char
    #Make this a list
    PIN_list = list(PIN)
    #Shuffl elist
    random.shuffle(PIN_list)

    #Adding list to PIN
    PIN = ''
    for i in range(len(PIN_list)):
        PIN = PIN + PIN_list[i]
    
    return PIN

def move_level_PIN_gen(PIN_gen_options):
    if PIN_gen_options == '<':
        print("Back...")
        
        move_level = -0.10
    elif PIN_gen_options == '>':
        print("You must tell the PIN how to be generated first. Please type in an option (number) to continue.")
        move_level = 0.00
        
    elif PIN_gen_options == 'q':
        print("Quitting...")
        sys.exit()
        
    elif PIN_gen_options == '1' or PIN_gen_options == '2' or PIN_gen_options == '3':
        move_level = 0.01
    else:
        print("Please try again...")
        move_level = 0.00

    return move_level


def get_UPPER_letter(num_UPPER_letters):
    UPPER_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    random.shuffle(UPPER_letters)

    UPPER_letter = ''
    UPPER_letter_list = []
    for i in range(num_UPPER_letters):
        UPPER_letter_list.append(UPPER_letters[i])
        UPPER_letter = str(UPPER_letter_list[i]) + UPPER_letter
        
    return UPPER_letter

def get_lower_letter(num_lower_letters):
    lower_letters = ["a","b","c","d","e","f","q","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    random.shuffle(lower_letters)

    lower_letter_list = []
    lower_letter = ''
    for i in range(num_lower_letters):
        lower_letter_list.append(lower_letters[i])
        lower_letter = str(lower_letter_list[i]) + lower_letter
        
    return lower_letter

def get_number(num_numbers):
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    random.shuffle(numbers)
    
    number_list = []
    number = ''    
    for i in range(num_numbers):
        number_list.append(numbers[i])
        number = str(number_list[i]) + number
        
    return number

def get_special_char(num_special_chars):
    special_chars = ["!","\"","£","$","%","^","&","*","=","+","#","@","_",":",";","~","?","/","<",">"]
    random.shuffle(special_chars)
    
    special_char_list = []
    special_char = ''
    for i in range(num_special_chars):
        special_char_list.append(special_chars[i])
        special_char = str(special_char_list[i]) + special_char
        
    return special_char

    
def get_PIN_gen_options():
    PIN_gen_options = input("\nWhat type of PIN would you like to have?\n1. Easy to remember\n2. Balanced.......\n3. Secure........\n")
    return PIN_gen_options

#-------------------------#
    
def get_age():
    age = input("How old are you?\n")
    return age
def check_age(age):
    
    split_age = list(age)

    for char in split_age:
        if char == '-' or char == '+':
            age = "False"
    try:
        int(age)
    except ValueError:
        print("Not an integer. Please Retype.")
        
    age = str(age)
    
    return age

def move_level_check_age(age):
    move_level = 0.9
    is_int = True
    
    try:
        int(age)
    except ValueError:
        move_level = -0.1
        is_int = False
        
    if is_int == True:
        if int(age) > 122:
            print("The age is too high. Only Jeanne Calment has lived up to this age - 122 yrs and 164 days. Google it!.")
            move_level = -0.1
        elif int(age) < 9:
            print("The age is too low. You are not elegible for sign up at this age.")
            move_level = -0.1
        else:
            print("The age '"+str(age)+"' is valid.")

    return move_level


def move_level_age(age):
    if age == '>':
        age = 0
        print("Continuing...")
        
        move_level = 0.10
    elif age == '<':
        print("Back...")
        
        move_level = -1.00
    elif age == 'q':
        print("Quitting...") 
        sys.exit()
        
    else:
        move_level = 0.10

    return move_level
#-----------------------------------#

def get_fun_fact():
    fun_fact = input("Please type in something fun about yourself:\n")
    return fun_fact

def check_fun_fact(fun_fact):    
    if fun_fact == "" or fun_fact == ">" or fun_fact == "<":
        fun_fact = "N/A"
    elif fun_fact == 'q':
        print("Quitting...")
        sys.exit()
            
    return fun_fact

def move_level_fun_fact(fun_fact):
    if fun_fact == "" or fun_fact == ">":
        print("Continuing...")
        
        move_level = 1
        
    elif fun_fact == "<":
        print("Back...")
        
        move_level = -1
        
    else:
        move_level = 1
        len_fun_fact = len(fun_fact)
        if len_fun_fact > 150:
            print("You used "+str(len_fun_fact)+" characters. Only use under 150 characters.")
            move_level = 0

    return move_level

def show_score():
    print("\nYour SCORE is set to '0' and will increase when you get questions right in the quiz.")
    time.sleep(0.5)
    score = "0"
    return score

def get_memPIN():
    memPIN = input("Do you want the computer to remember your PIN, for the next time you log in?(y/n)\n")
    memPIN = memPIN.lower()
     
    if memPIN == ">" or memPIN == "":
        memPIN = "True"
        
    elif memPIN == "q":
        print("Quitting...")
        
        sys.exit()

    elif memPIN == "yes" or memPIN == "y":
        memPIN = "True"
    elif memPIN == "n" or memPIN == "no":
        memPIN = "False"
            
        
    return memPIN

def move_level_memPIN(memPIN):
    if memPIN == "<":
        print("Back...")
        
        move_level = -2.00
        
    elif memPIN == "True" or memPIN == "False":
        move_level = 1.00
        
    else:
        print("Please try again.")
        move_level = 0.00
        
    return move_level

def remind_details(username, PIN):
    print("\nHere is some useful information, the next time you log in:")
    print("Your username is '"+username+"'.")
    print("Your PIN is '"+PIN+"'.\n")
    time.sleep(0.5)

def create_data_send(username, PIN, age, score, fun_fact, memPIN):
    data_send = {'Username': username,
        'PIN': PIN,
        'Age': age,
        'Score': score,
        'Fun Fact': fun_fact,
        'Remember PIN': memPIN
    }
    return data_send

def print_send_data(username):
    user_list = get_user_list()
    list_counter = -1
    for user in user_list:
        username_info = user['Username']
        
        #Info for printing later
        heading1 = "Option Type"       
            
        username_key = "|Username:"
        PIN_key = "|PIN:"
        age_key = "|Age:"
        score_key = "|Score:"
        funfact_key = "|Fun Fact:"
        memPIN_key = "|Remember PIN:"

        key_list = [username_key, PIN_key, age_key, score_key, funfact_key, memPIN_key, heading1]
        longest_key = max(key_list, key=len)

        for i in range(len(longest_key)-len(username_key)+1):
            username_key += " "
        username_key += "|"

        for i in range(len(longest_key)-len(PIN_key)+1):
            PIN_key += " "
        PIN_key += "|"

        for i in range(len(longest_key)-len(age_key)+1):
            age_key += " "
        age_key += "|"

        for i in range(len(longest_key)-len(score_key)+1):
            score_key += " "
        score_key += "|"

        for i in range(len(longest_key)-len(funfact_key)+1):
            funfact_key += " "
        funfact_key += "|"

        for i in range(len(longest_key)-len(memPIN_key)+1):
            memPIN_key += " "
        memPIN_key += "|"

        for i in range(len(longest_key)-len(heading1)):
            heading1 += " "
            
        heading2 = "Option Value"
        
        username_val = "'"+ user["Username"]+"'"
        PIN_val = "'"+ user["PIN"]+"'"
        age_val = "'"+ user['Age']+"'"
        score_val ="'"+ user["Score"]+"'"
        funfact_val ="'"+ user["Fun Fact"]+"'"
        memPIN_val = "'"+ user["Remember PIN"] +"'"
        
        
        val_list = [username_val, PIN_val, age_val, score_val, funfact_val, memPIN_val, heading2]
        longest_val = max(val_list, key=len)

        for i in range(len(longest_val)-len(username_val)+1):
            username_val += " "
        

        for i in range(len(longest_val)-len(PIN_val)+1):
            PIN_val += " "
        

        for i in range(len(longest_val)-len(age_val)+1):
            age_val += " "
        

        for i in range(len(longest_val)-len(score_val)+1):
            score_val += " "
        

        for i in range(len(longest_val)-len(funfact_val)+1):
            funfact_val += " "
        

        for i in range(len(longest_val)-len(memPIN_val)+1):
            memPIN_val += " "
        
        if len(longest_val) > len(heading2):
            for i in range(len(longest_val)-len(heading2)+1):
                heading2 += " "
       
        
        total_heading = "|"+heading1 + "|" + heading2
        
        username_print = username_key +username_val
        PIN_print = PIN_key +PIN_val
        age_print = age_key + age_val
        score_print = score_key + score_val
        funfact_print = funfact_key + funfact_val
        memPIN_print = memPIN_key + memPIN_val

        details_list = [username_print, PIN_print, age_print, score_print, funfact_print, memPIN_print, total_heading]
        longest_line = max(details_list, key=len)

        for i in range(len(longest_line)-len(username_print)+1):
            username_print += " "
        username_print += "|"
        
        for i in range(len(longest_line)-len(PIN_print)+1):
            PIN_print += " "
        PIN_print += "|"
        
        for i in range(len(longest_line)-len(age_print)+1):
            age_print += " "
        age_print += "|"
        
        for i in range(len(longest_line)-len(score_print)+1):
            score_print += " "
        score_print += "|"
        
        for i in range(len(longest_line)-len(funfact_print)+1):
            funfact_print += " "
        funfact_print += "|"
        
        for i in range(len(longest_line)-len(memPIN_print)+1):
            memPIN_print += " "
        memPIN_print += "|"
        
        for i in range(len(longest_line)-len(total_heading)+1):
            total_heading += " "
        total_heading += "|"
        
        horizontal_lines = ""
        
        for i in range(len(longest_line)):
            if len(horizontal_lines) == len(heading1):
                horizontal_lines += '+'
            else:
                horizontal_lines += '-'
            
        horizontal_lines = "+"+horizontal_lines+"+"
        
        if username == username_info:
            break
        
    print(horizontal_lines)
    print(total_heading)
    print(horizontal_lines)
    print(username_print+"\n"+PIN_print+"\n"+age_print+"\n"+score_print+"\n"+funfact_print+"\n"+memPIN_print)
    print(horizontal_lines+"\n")



def send_data(data_send):
    with open("user_info.txt", "a") as new_user:
        json.dump(data_send, new_user)
        new_user.write("\n")


def main_login_signup():
    option_type = 'False'
    option = input("Start Options:\nEnter '1' to Log In.\nEnter '2' to Sign Up.\n")
    option = option.lower()
    if option == 'login' or option == '1':
        move_level = login()
        option_type = 'login'
    elif option == 'signup' or option == '2':
        move_level = signup()
        option_type = 'signup'
    elif option == 'q':
        option_type = 'q'
    else:
        print("Please try again.")
        
    return option_type
        

################################################################
def password_generator_main(move_level, typed, generated, password):
    level = 0
    typed = False
    generated = False
    wrong_typed = False
    while True:
        
        if level == 0:
            move_level = 1
            
        elif level == 1:
            password = generate_password_school()
            move_level = 1
            typed = False
            generated = True
            
            
        elif level == 2:
            move_level = check_password_school(password, typed, generated)

            
        elif level == 3:
            break
        
        else:
            if level < 0:
                print("Error: Level number less than 0 - main()")
                level = 0
                move_level = 0
            else:
                print("Error: Level not available - main()")
                move_level = 0
                level = 0
                
        level = level + move_level

    return password


def display_menu_school():
    print("MENU:")
    print("1 - Check PIN")
    print("2 - Generate PIN")
    print("'q' - Quit")
    option = input()
    option = option.lower()
    return option

def check_option_school(option):
    if option == '1' or option == 'check pin':
        move_level = 1
        print(move_level)
    elif option == '2' or option == 'generate pin':
        move_level = 2
    elif option == '3' or option == 'quit' or option == 'q':
        print("Quitting...")
        sys.exit()
        
    elif option == '<':
        move_level = -0.5
        
    else:
        print("Please try again.")
        move_level = 0

    return move_level

def get_password_school():
    print("MENU:")
    print("'<' - Back")
    print("'c' - Criteria of PIN")
    print("'q' - Quit")
    password = input("Type in a PIN of your choice:")

    return password

def check_password_school(password, typed, generated):
    points = 0
    
    split_password = list(password)
    
    upper_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    symbols = ["!","$","^","&","*","(",")","-","_","=","%","+"] #Space character is not allowed
    
    while True:
        
        if len(password) > 24 or len(password) < 8  :
            print("\nError, the PIN is the wrong length.\nIt must be between 8 and 24 characters.\n")
            move_level = -2
            break
        else:
            #Correct length

            split_password = list(password)
            len_split_password = len(split_password)
            
            upper_position = []
            lower_position = []
            numbers_position = []
            symbols_position = []
            new_list = split_password
        
            
            
            
            #Use position values to remove this position from the split password list
            num_upper_letters = count_upper(password, upper_letters, upper_position, split_password)
            upper_position.sort()
            counter = 0
            while True:
                for char in range(len_split_password):
                    len_upper_position = len(upper_position)
                    for upper in range(len_upper_position):
                        split_password.pop(upper_position[char]-counter)
                        upper_position.pop(upper - counter)
                        counter += 1
                break

            num_lower_letters = count_lower(password, lower_letters, lower_position, split_password)
            lower_position.sort()
            counter = 0
            while True:
                for char in range(len_split_password):
                    len_lower_position = len(lower_position)
                    for lower in range(len_lower_position):
                        split_password.pop(lower_position[char]-counter)
                        lower_position.pop(lower - counter)
                        #I need to change each number in the list to 1 less not.
                        counter += 1
                break

                        
            num_numbers = count_number(password, numbers, numbers_position, split_password)
            numbers_position.sort()
            counter = 0
            while True:
                for char in range(len_split_password):
                    len_numbers_position = len(numbers_position)
                    for num in range(len_numbers_position):
                        split_password.pop(numbers_position[char]-counter)
                        numbers_position.pop(num - counter)
                        counter += 1
                break


            num_symbols = count_symbols(password, symbols, symbols_position, split_password)
            symbols_position.sort()
            counter = 0
            while True:
                for char in range(len_split_password):
                    len_symbols_position = len(symbols_position)
                    for sym in range(len_symbols_position):
                        split_password.pop(symbols_position[char]-counter)
                        symbols_position.pop(sym - counter)
                        counter += 1
                break
       
            
            

        if split_password != []:
            if len(split_password) == 1:
                print("Please retype. You have used an incorrect character.")
            else:
                print("Please retype. You have used incorrect characters.")
            move_level = -2
            break
        else:
            split_password = list(password)
            
            points = len(password)
            #Adding points
            if num_upper_letters >= 1 or num_lower_letters >= 1:
                points += 5

                
            if num_numbers >= 1:
                points += 5
            
            if num_symbols >= 1:
                points += 5

            if num_upper_letters >= 1 and num_lower_letters >= 1 and num_numbers >= 1 and num_symbols >= 1:
                points += 10

            #Deducting points
            if num_upper_letters >= 1 or num_lower_letters >= 1 and num_numbers == 0 and num_symbols == 0:
                points -= 5

            if num_upper_letters == 0 and num_lower_letters == 0 and num_numbers >= 1 and num_symbols == 0:
                points -= 5

            if num_upper_letters == 0 and num_lower_letters == 0 and num_numbers == 0 and num_symbols >= 1:
                points -= 5

            #Determining whether password is strong.
            if points >= 25:
                password_quality = "strong"
                if typed == True:
                    print("Good job - you had a '"+password_quality+"' PIN and scored an incredible '"+str(points)+"' out of 54 possible points.")
                    move_level = 1
                    break
                elif generated == True:
                    print("Your generated PIN is '"+password+"' which got a score of '"+str(points)+"'.")
                    time.sleep(0.5)
                    move_level = 1
                    break
            else:
                password_quality = "weak"
                
                if typed == True:
                    print("Unfortunately, you had a '"+password_quality+"' password and scored '"+str(points)+"' out of a possible 54 points.")
                    print("""Criteria:
For the PIN to be valid, it must follow most of the following criteria:
- Must be 8 - 24 charcters
- Can contain at least 1 upper case letter
- Can contain at least 1 lower case letter
- Can contain at least 1 digit
- Can contain 1 allowed symbol:
    !,$,^,&,*,(,),-,_,=,%,+
    The character space is not allowed.\n""")
                    move_level = -2
                    break
                
                elif generated == True:
                    move_level = -1
                    break
                
    return move_level
                
                    
def count_upper(password, upper_letters, upper_position, split_password):
    num_upper_letters = 0
    
    while True:
        upper_len = len(upper_letters)
        password_len = len(split_password)
            
        for letter in range(upper_len):           
            
            for i in range(password_len):
                
                if split_password[i] == upper_letters[letter]:
                    num_upper_letters += 1
                    upper_position.append(i)
                    
        break
    
    return num_upper_letters

def count_lower(password, lower_letters, lower_position, split_password):
    num_lower_letters = 0
    
    while True:
        lower_len = len(lower_letters)
        password_len = len(split_password)
            
        for letter in range(lower_len):
            for i in range(password_len):
                if split_password[i] == lower_letters[letter]:
                    num_lower_letters +=1
                    lower_position.append(i)
        break
    
    return num_lower_letters

def count_number(password, numbers, numbers_position, split_password):
    num_numbers = 0
    
    while True:
        numbers_len = len(numbers)
        password_len = len(split_password)
            
        for number in range(numbers_len):
            for i in range(password_len):
                if split_password[i] == numbers[number]:
                    num_numbers +=1
                    numbers_position.append(i)
        break
    
    return num_numbers

def count_symbols(password, symbols, symbols_position, split_password):
    num_symbols = 0
    
    while True:
        symbols_len = len(symbols)
        password_len = len(split_password)
            
        for symbol in range(symbols_len):
            for i in range(password_len):
                if split_password[i] == symbols[symbol]:
                    num_symbols +=1
                    symbols_position.append(i)
        break
    
    return num_symbols

                       
def generate_password_school():
    len_password = random.randint(8,24)

    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "1","2","3","4","5","6","7","8","9","0","!","$","^","&","*","(",")","-","_","=","%","+"]
    len_letters = len(letters)
    
    password = ""
    password_list = []
    counter = 0
    
    while True:
        counter += 1
        letter_index = random.randint(1,len_letters-1)
        password_list.append(letters[letter_index])

        if counter == len_password:
            break
        
    num_password_list = len(password_list)
    for i in range(num_password_list):
        password = password + password_list[i]
   
    return password
##############################################################################################
def main():   
    move_level = 0  
    
    global username
    username = ''
    
    signed_up = False
    
    level = 0
    
    while True:
        if level == 0:
            
            option = input("Main Menu:\nType '1' to Log In.\nType '2' to Sign Up.\nType 'q' to Quit.\n")
            option = option.lower()
            if option == 'login' or option == '1':
                signed_up = False
                move_level = 1

            elif option == 'signup' or option == '2':
                move_level = 2

            elif option == 'q':
                move_level = 5

            else:
                print("Please try again.")
                move_level = 0            
                
        elif level == 1:
            return_package = login(username, signed_up)
            #LOGIN RETURN PACKS
            move_level = return_package[0]
            user_data = return_package[1]
            user_list = return_package[2]
            
        elif level == 2:
            signup_return_package = signup()
            #SING UP RETURN PACKS
            move_level = signup_return_package[0]
            username = signup_return_package[1]
            
            signed_up = True
            
        elif level == 3:
            new_score = 0

            ##---------------PLAYS QUIZ
            return_package = play_quiz(user_data)
            #----------------^^^^^^^^^^^^^^^^^^^^

            #NEW SCORE
            new_score = return_package[0]
            #MOVE LEVEL
            move_level = return_package[1]
            
            old_score = user_data["Score"]
            old_score = int(old_score)

            new_score += old_score
            
            category_type = "Score"
            change_to = str(new_score)
            
            run_change_to(category_type, user_list, user_data, change_to) #For changing score
            
            print("\n")
            
            
        elif level == 4:
            break
            
        else:
            if level < 0:
                print("Error: level is less than 0: main()")
                level = 0
                move_level = 0
                break
            else:
                print("Error: level not an option (FIX)")
                move_level = 0
                break

        level = move_level + level


def play_quiz(user_data):
    cont = "True"
    score = 0
    
    question_counter = 0
    
    print("Welcome to my revision quiz!")
    time.sleep(0.5)
    print("""

OPTIONS during quiz:

Don't worry if you make a mistake - it allows you to go back and retype your answer :)

Type 'p' to view your percentage.
Type '<' or 'Log' to Log Out
Type 'q' to QUIT.
""")
    
    time.sleep(0.5)
    
    move_level = 0
    while cont == "True":
        
        questions = []
        question_counter += 5
          
        questions = create_questions(questions)
        score_cont = ask_question(questions, score, question_counter)
        
        score = score_cont[0]
        cont = score_cont[1]
        

        if cont == "True":
            cont = go_again(score, question_counter)

        username = user_data["Username"]
        
        if cont == "True":
            print("\nReshuffling...\n")
            time.sleep(0.5)
            
        elif cont == "log out":
            get_statistic(username)
            print("Logging out...")
            move_level = -2
            
        elif cont == "False":
            get_statistic(username)
            print("\nSee ya!")
            sys.exit()

    new_score = score
    return_package = [new_score, move_level]
    
    return return_package
    

def create_questions(questions):
    with open("questions.txt", "r") as questions_file:
        for line in questions_file:
            line = line.rstrip()
            questions.append(line)
            
        random.shuffle(questions)
        
    return questions

        
def ask_question(questions, score, question_counter):
    counter = 0
    
    cont = "True"
    for q in questions:
        p = False
        #Work out percentage

        current = question_counter - 5 + counter #Current question number = total question counter - 5 + counter for this loop

        #if total is more than 0, do score / total, else, percent is 0
        percent = (score/current) * 100 if current > 0 else 0

        if percent >= 1.0:
            percent = int(percent)
    

        #Increment question counter
        counter += 1        
        current = question_counter - 5 + counter #Current question number = total question counter - 5 + counter for this loop 

        #while the user wants to go back, loop this code
        back = "<"
        while back == "<" or answer == "p":

            #Split file by colon and space
            questions = q.split(": ")
            print("\n"+str(counter)+") "+questions[1])

            answer = input()
            answer = answer.lower()

            #Checking if user wanted to quit or see percentage
            if answer == "q":
                print("\nYou had a percentage of "+str(percent)+"%!")
                cont = "False"
                break

            elif answer == "<" or answer == "log" or answer == "log out":
                print("\nYou had a percentage of "+str(percent)+"%!")
                cont = "log out"
                answer = "q"
                break

            elif answer == "p":
                print("\nYou have a percentage of "+str(percent)+"%!")
                p = True
                

            back = ""
            if answer != "p":
                print("\nDOUBLE check your answer...")
                print("\nIF you THINK have made a mistake, TYPE '<' and press ENTER.")
                print("OTHERWISE, press ENTER to continue.")
            
                back = input()
                
            if back != "<" and answer != "p":
                break

        
        n = 2
        max_n = len(questions)
        #percent = (score/5) * 100
        while n < max_n and answer != "q":
            if answer == questions[n].lower():
                print("\nCorrect.")
                score += 1
                print("Score: ("+ str(score)+"/"+str(current)+")\n")
                break
            else:
                n+=1
                if n == max_n:
                    print("\nIncorrect, the answer is '"+questions[2]+"'.")
                    print("Score: ("+ str(score)+"/"+str(current)+")\n")

        if counter >= 5 or answer == "q":
            break
        
    score_cont = [score, cont]
    
    return score_cont

def go_again(score, question_counter):
    percent = (score/question_counter) * 100
    
    if percent >= 1.0:
        percent = int(percent)

    counter = 0
    cont = 'False'
    while True:
        again = input("Type 'yes' to continue.\nType 'no' to discontinue the quiz.\nType '<' to log out.\n").lower()
        if again == "y" or again == "yes" or again == "ya" or again == "ye" or again == "yee" or again == "yeee" or again == "yaa" or again == "yaa":
            cont = 'True'
            print("\nYou have a percentage of "+str(percent)+"%!")
            break
        
        elif again == "n" or again == "no" or again == "noo" or again == "nooo":
            while True:
                option = input("\nType 'Q' to quit.\nType 'LOG' to log out.\n").lower()

                if option == "q":
                    cont = 'False'
                    break
                elif option == "log" or option == "<":
                    cont = "log out"
                    break
                else:
                    print("Please try again.")
            
            
            print("\nYou had a percentage of "+str(percent)+"%!")
            break
        
        elif again == "<":
            cont = "log out"
            print("\nYou had a percentage of "+str(percent)+"%!")
            break
        
        else:
            counter += 1
            if counter <= 3:
                print("Please try again. ("+str(3 - counter)+" time(s) left)")
                
            else:
                cont = 'False'
                break
            
    return cont

def get_statistic(username):
    level = 0
    move_level = 1

    #Statisitcs - reading file
    yes = get_ayes()
    no = get_noes()
    counter = 0
    
    while True:
        if level == 0:
            statistic = input("\nDid you like this quiz? (y/n)\n").lower()
            
            yes = get_ayes()
            no = get_noes()
        
            #If they liked quiz, updatate yes so it has increased by 1
            if statistic == "y" or statistic == "yes":     
                move_level = 1
        
        
                #If they didn't like quiz, updatate no so it has increased by 1
            elif statistic == "n" or statistic == "no":
                move_level = 2  

            else:
                move_level = 3
                counter += 1
                while counter <= 3:
                    print("Please try again. ("+str(3 - counter)+" time(s) left)")
                    move_level = 0
                    break

            
        elif level == 1:
            move_level = get_good_feedback(username)
            
        elif level == 1.5:
            yes += 1
            send_statistic_data(yes, no)
            move_level = 1.5
            
        elif level == 2:
            move_level = get_bad_feedback(username)
            
        elif level == 2.5:
            no += 1
            send_statistic_data(yes, no)
            move_level = 0.5
            
        else:
            break

        level += move_level

def check_statistic(statistic, counter):
    yes = get_ayes()
    no = get_noes()
        
    #If they liked quiz, updatate yes so it has increased by 1
    if statistic == "y" or statistic == "yes":     
        move_level = 1
        
        
        #If they didn't like quiz, updatate no so it has increased by 1
    elif statistic == "n" or statistic == "no":
        move_level = 2  

    else:
        move_level = 3
        while counter <= 3:
            print("Please try again. ("+str(3 - counter)+" time(s) left)")
            move_level = 0
            break

    return move_level

def get_ayes():
    #Reading the first line of quiz statistics file
    data = ""
    with open("Quiz Statistics.txt", "r") as statistics_file:
        data = statistics_file.readline()

    #Split data by colon and yes is first part
    data = data.split(":")
    yes = data[0]
    yes = int(yes)

    return yes

def get_noes():
    #Reading the first line of quiz statistics file
    data = ""
    with open("Quiz Statistics.txt", "r") as statistics_file:
        data = statistics_file.readline()

    #Split data by colon and no is second part
    data = data.split(":")
    no = data[1]
    no = int(no)

    return no


def send_statistic_data(yes, no):
    #Writing data back to statistics file
    with open("Quiz Statistics.txt", "w") as statistics_file:
        data_send = str(yes) + ":" + str(no)
        statistics_file.write(data_send)
    

def get_good_feedback(username):            
    like = input("\nTo go back, type '<'.\nYou don't have to write anything if you don't want to.\n\nWhat did you like about the quiz?\n")
        
    if like == "<":
        print("Back...")
        move_level = -1
        
    elif like == "":
        print("You have decided not suggest any positive feedback.")
        move_level = 0.5
        
    else:
        like = username + " said: " + like
        #Appending improvement to improvement file
        with open("likes.txt", "a") as likes_file:
            likes_file.write(like)
            likes_file.write("\n")
            
        print("\nThanks for the positive feedback!")
        move_level = 0.5

    return move_level


def get_bad_feedback(username):            
    improvement = input("\nTo go back, type '<'.\nYou don't have to write anything if you don't want to.\n\nWhat do you think I should improve?\n")

    if improvement == "<":
        print("Back...")
        move_level = -2
        
    elif improvement == "":
        print("You have decided not suggest any improvements.")
        move_level = 0.5
        
    else:
        improvement = username + " said: " + improvement
        #Appending improvement to improvement file
        with open("improvements.txt", "a") as improvements_file:
            improvements_file.write(improvement)
            improvements_file.write("\n")

        print("\nOk, thanks for the feedback!")
        move_level = 0.5

    return move_level

main()
