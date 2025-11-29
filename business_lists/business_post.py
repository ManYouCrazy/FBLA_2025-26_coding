class business_post:
    
    post_id = 0
    
    def __init__(self, title, description, industry, location, established, average_rating, special_deals, ratings, pre_id=-1):
        self.industry = industry
        self.title = title
        self.description = description
        self.location = location
        self.established = established
        self.average_rating = average_rating
        self.special_deals = special_deals
        self.ratings = ratings
        self.post_id = business_post.post_id
        if (pre_id != -1):
            self.post_id = pre_id
        business_post.post_id += 1
    
    def __str__(self):
        return "Business ID: " + str(self.post_id) + "\nTitle: " + self.title + "\nDescription: " + self.description + "\nLocation: " + self.location + "\nEstablished: " + str(self.established) + "\nAverage Rating: " + str(self.average_rating) + "\nSpecial Deals: " + str(self.special_deals) + "\nRatings: " + str(self.ratings)
    
    def json_format(self):
        return {
        "post_id": self.post_id,
        "title": self.title,
        "description": self.description,
        "industry": self.industry,
        "location": self.location,
        "established": self.established,
        "average_rating": self.average_rating,
        "special_deals": self.special_deals,
        "ratings": self.ratings
    }

    def disp_format(self):
        return "Business ID: " + str(self.post_id) + "\nName: " + self.title + "\nDescription: " + self.description