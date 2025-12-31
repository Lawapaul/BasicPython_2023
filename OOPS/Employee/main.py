class Employee:
    def __init__ (self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print(f"Role: {self.role}\nDepartment: {self.department}\nSalary: {self.salary}")


class Engineer(Employee):
    def __init__(self,role,department,salary,name,age):
        super().__init__(role,department,salary)
        self.name = name
        self.age = age
    
    def details(self):
        super().showDetails()
        print(f"Name: {self.name}\nAge: {self.age}")


def main():
    obj_1 = Engineer("SDE","AIML",100010,"Harshit Singh",21)
    obj_1.details()

main()