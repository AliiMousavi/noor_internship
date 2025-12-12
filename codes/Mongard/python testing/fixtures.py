class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def email(self):
        return f"{self.fname}{self.lname}@gmail.com"
    
# p = Person("amir", "mohamadi")
# print(p.full_name())
# print(p.email())
