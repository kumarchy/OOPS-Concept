class phone:
    def set_color(self,color):
       self.color=color 
    def set_cost(self,cost):
       self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
        
p1=phone()
p1.set_color("red")
p1.set_cost(1200)
print(p1.show_color())
print(p1.show_cost())

class Phone:
    
    def set_color(self,color):
       
        self.color=color
        
    def set_cost(self,cost):
        self.cost=cost
        
    def show_color(self):
        return self.color
    
    def show_cost(self):
        return self.cost
    
    def make_call(self):
        print("Making phone call")
    
    def play_game(self):
        print("Playing Game")
p2=Phone()
p2.set_color("blue")
p2.set_cost(100)
print("the color is ",p2.show_color())
print("the cost is ",p2.show_cost())

class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def employee_details(self):
        print("name of employee is ",self.name)
        print("age of employee is",self.age)
        print("salary of employee is",self.salary)
        print("gender of employee is",self.gender)
e1=Employee("kumar",20,2000,"male")
e1.employee_details()

class vehicle():
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost

    def show_details(self):
        print("i am a vehicle")
        print("mileage of vehicle is :",self.mileage)
        print("cost of vehicle is :",self.cost)


class car(vehicle):
    def __init__(self, mileage, cost):
        super().__init__(mileage, cost)
        
    def show_car_details(self):
        print("i am a car")
        

c1=car(1200,15000)
c1.show_details()
c1.show_car_details()




class parent1():
    def assign_string_one(self,str1):
        self.str1=str1
    def show_string_one(self):
        return self.str1
class parent2():
    def assign_string_two(self,str2):
        self.str2=str2
    def show_string_two(self):
        return self.str2
class derived(parent1,parent2):
    def assign_string_three(self, str3):
        self.str3=str3
    def show_string_three(self):
        return self.str3
d1=derived()
d1.assign_string_one("one")
d1.assign_string_two("two")
d1.assign_string_three("three")
print(d1.show_string_one())
print(d1.show_string_two())
print(d1.show_string_three())


class parent():
    def assign_name(self,name):
        self.name=name
    def show_name(self):
        return self.name

class child(parent):
    def assign_age(self,age):
        self.age=age
    def show_age(self):
        return self.age

class grandchild(child):
    def assign_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        return self.gender

g1=grandchild()
g1.assign_name("kumar")
g1.assign_age(20)
g1.assign_gender("male")
print("your name is:",g1.show_name())
print("your age is:",g1.show_age())
print("your gender is:",g1.show_gender())


class details():
    def enter_name(self,name):
        self.name=name
    def show_name(self):
        return self.name
class organization(details):
    def enter_organization(self,organization):
        self.organization=organization
    def show_organization(self):
        return self.organization
class qualification(organization):
    def enter_qualification(self,qualification):
        self.qualification=qualification
    def show_qualification(self):
        return self.qualification
class job(qualification):
    def enter_job(self,job):
        self.job=job
    def show_job(self):
        return self.job

p1=job()
p1.enter_name("kumar")
p1.enter_organization("kpr institute of engineering and technology")
p1.enter_qualification("12th pass")
p1.enter_job("student")
print("your name is:",p1.show_name())
print("your organization is:",p1.show_organization())
print("your qualification is:",p1.show_qualification())
print("your job is :",p1.show_job())

      
