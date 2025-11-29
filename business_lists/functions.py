#IMPORTS
from business_post import business_post
import json

#FUNCTIONS

#returns the password saved in the Userdata.json
def find_password(username_to_check,userdata_file_data):
    for i in userdata_file_data:
            if i['username'] == username_to_check:
                return i['pasword']
                
#checks to see if a value is in a file
def check_value(file,value):
    #checks if the file is a dictionary
    if (isinstance(file, dict)):
        #returns true if the value is detected
        if (value in file.values()):
            return True
        #secondary check if first check fails
        for item in file.values():
            if (check_value(item, value)):
                return True
    #checks if the file is a list
    elif (isinstance(file, list)):
        #returns true if the value is in the list
        for item in file:
            if (check_value(item, value)):
                return True
    #if all other checks fail returns false
    return False

#tries to open the json file
def open_json(filepath):
    #returns the data from the file
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    #if the file is not found it prints an error
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return None
    #if the file is not formated wrongs prints an error
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in: {filepath}")
        return None
    #prints any other errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

#uploads the new data to the JSON file
def uploadListing(new_job_desc,business_file_data):
    #adds the new 
    business_file_data.append(new_job_desc)
    with open("business_lists/business_lists.json",'w') as file:
        file.seek(0)
        json.dump(business_file_data, file, indent = 4)

#uploads the new data to the JSON file
def update_after_edit(newListings):
    business_file_data = []
    for listing in newListings:
        business_file_data.append(listing.json_format())
    with open("business_lists/business_lists.json",'w') as file:
        file.seek(0)
        json.dump(business_file_data, file, indent = 4)

#returns an error or sucsess for login
def login(user_data,username,password_guess):
    if (check_value(user_data,username)):
        password = find_password(username,user_data)
        if (password == password_guess):
            return (("welcome " + username),1)
        else:
            return ("Incorrect password",0)
    return ("Account not found",0)
        

#OLD CODE TO REVISIT FOR FUTURE REPURPOSING
"""while (user_input != "5"):
    #search for post
    if (user_input == "1"): 
        jobID = int(input("What is the ID of the job? "))
        for i in business_file_data:
            if i['post_id'] == jobID:
                print("\n" + str(business_archive[jobID]) + "\n")
        user_input = ""
    #view all posts
    elif (user_input == "2"): 
        for listing in business_archive:
            print(listing)
            print("\n")
        user_input = ""
    #create post
    elif (user_input == "3"): 
        createdListing = business_post(input("what is the job title\n"),input("what is the job description\n"),input("what are the requirements\n"),input("what is the pay\n"),username)
        uploadListing(createdListing.json_format())
        business_archive.append(createdListing)
        print(createdListing)
        user_input = ""
    #edit post
    elif (user_input == "4"): 
        jobID = int(input("What is the ID of the job you want to edit? "))
        for i in business_file_data:
            if i['post_id'] == jobID:
                if i['employer'] == username:
                    x = business_post(input("what is the job title\n"),input("what is the job description\n"),input("what are the requirements\n"),input("what is the pay\n"),username,jobID)
                    business_archive.pop(jobID)
                    business_archive.insert(jobID,x)
                    update_after_edit(business_archive)
                else:
                    print("You did not create this listing")
        user_input = ""
    #quit program
    elif (user_input == "5"): 
        quit()
    else:
        user_input = input(input_questions)"""