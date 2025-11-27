import authorization_window as aw
import tkinter as tk
from functions import open_json
from business_post import business_post

#creates root window
root = tk.Tk()
root.wm_geometry("500x500")
root.title("root")

#runs authorization
auth_wind = aw.auth_window(root)
auth_wind.run()

#waits to be logged in
root.wait_variable(auth_wind.logged_in)

#stores data
username = auth_wind.username
userdata = auth_wind.userdata_file_data
business_data = open_json('business_lists/business_lists.json')
business_archive = []

for listing in business_data:
    x = business_post(listing['title'],listing['description'],listing['industry'],listing['location'],listing['established'],listing['average_rating'],listing['special_deals'],listing['ratings'],listing['post_id'])
    business_archive.append(x)



root.mainloop()