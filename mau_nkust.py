class Compuse:
    def __init__(self,compuse_name):
        self.compuse_name=compuse_name

class College:
    def __init__(self,college_name):
        self.college_name=college_name

class Department:
    def __init__(self,department_name):
        self.department_name=department_name


class Faculty:
    def __init__(self,teacher_name):
        self.teacher_name=teacher_name

class Student:
    def __init__(self,student_name):
        self.student_name=student_name
       



class NKUST:
    def __init__(self,name,compuse_name,college_name,department_name,teacher_name,student_name):
        self.school_name=name
        self.compuse_name=Compuse(compuse_name)
        self.college_name=College(college_name)
        self.department_name=Department(department_name)
        self.teacher_name=Faculty(teacher_name)
        self.student_name=Student(student_name)

nkust=NKUST("NKUST","Jiangong","CE","ME","mausheng Chen","susie Su")
print(nkust.school_name)
print(nkust.compuse_name.compuse_name)
print(nkust.college_name.college_name)
print(nkust.department_name.department_name)
print(nkust.teacher_name.teacher_name)
print(nkust.student_name.student_name)








