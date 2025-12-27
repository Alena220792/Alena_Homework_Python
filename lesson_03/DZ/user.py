class User:
       def __init__(self, first_name, last_name):
        self.First_name = first_name
        self.Last_name = last_name

       def get_First_name(self):
        return self.First_name
    
       def get_Last_name(self):
        return self.Last_name
    
       def get_user_info (self):
        return f"{self.First_name} {self.Last_name}"