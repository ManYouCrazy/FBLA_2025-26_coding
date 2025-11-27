class business_post:
    
    post_id = 0
    
    def __init__(self, Job_title, Description, requirements, pay, creator,pre_id=-1):
        self.creator = creator
        self.job_title = Job_title
        self.description = Description
        self.requirements = requirements
        self.pay = pay
        self.post_id = business_post.post_id
        if (pre_id != -1):
            self.post_id = pre_id
        business_post.post_id += 1
    
    def __str__(self):
        return "Job ID: " + str(self.post_id) + "\nemployer: " + self.creator + "\nJob Title: " + self.job_title + "\nJob description: " + self.description + "\nJob Requirements: " + self.requirements + "\nJob Pay: " + self.pay
    
    def json_Format(self):
        return {
        "post_id": self.post_id,
        "job_title": self.job_title,
        "description": self.description,
        "requirements": self.requirements,
        "pay": self.pay,
        "employer": self.creator
    }