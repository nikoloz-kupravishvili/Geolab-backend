class student:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = str(age)
        self.info = [self.name,self.surname,self.age]

    def get_info(self):
        return f'info : {self.name,self.surname,self.age}'
    
    def __repr__(self):

        return self.info
    
        
me = student('nick','anonymous',69)


class school(student):
    def __init__(self,school_name,school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.student_list = []


    def add_student(self,student):
        for i in student.info:
            self.student_list.append(i)
        return f'list: {self.student_list}'

    def remove_student(self,index =0,):
        return f'removed : {self.student_list[index]}'
        self.student_list.pop(index)
        
        
    def show_students(self):
        return me.get_info()
       

    

        
studenti = school('andrew tate' , 'chicago')

print(studenti.add_student(me))
print(me.get_info())
print(studenti.remove_student())
print(studenti.show_students())