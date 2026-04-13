class Employee:
    company_name="Google"

    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks

    def welcome(self):
        print("Welcome students,",self.name)

    

emp_id =Employee("Mehul Sharma",22)  

emp_id.welcome()