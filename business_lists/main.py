import authorization_window as aw
from tkinter import *
from functions import open_json
from business_post import business_post

#creates root window
root = Tk()
root.wm_geometry("750x500")
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

#creates the display frame
Business_disp_frame = Frame(root)
Business_disp_frame.pack(fill="both", expand=True)
Business_disp_frame.grid_rowconfigure(0, weight=1)

#creates the display canvas and scrollbar
Business_disp_canvas = Canvas(Business_disp_frame,width=325)
Business_disp_scrollbar = Scrollbar(Business_disp_frame, orient="vertical", command=Business_disp_canvas.yview,width=20)

#creates the display scrolable frame
Business_disp_scrollable_frame = Frame(Business_disp_canvas,width=325)
Business_disp_scrollable_frame.bind("<Configure>",lambda e: Business_disp_canvas.configure(scrollregion=Business_disp_canvas.bbox("all")))

#configures the canvas
Business_disp_canvas.create_window((0, 0), window=Business_disp_scrollable_frame)
Business_disp_canvas.configure(yscrollcommand=Business_disp_scrollbar.set)

#displays the businesses
for business in business_archive:
    Button(Business_disp_scrollable_frame, text=business.disp_format(), wraplength=325).pack(pady=5)

#packs/displays the canvas and scrollbar
Business_disp_canvas.grid(column=0,row=0,sticky="nsew")
Business_disp_scrollbar.grid(column=1,row=0,sticky="ns")

root.mainloop()