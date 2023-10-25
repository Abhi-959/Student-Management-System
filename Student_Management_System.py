class StudentInfo:

    def __init__(self,n,r,m):
        self.name = n
        self.rollno = r
        self.marks = m

    def __str__(self):
        return f"NAME:{self.name},ROLL NO:{self.rollno}, MARKS:{self.marks}"

students_list = []

def return_student():
    roll = int (input ('Enter roll number of student'))
    for stu in students_list:
        if stu.rollno == r:
            return stu
while True:

    ch = int(input("Enter Choice:\n1.Add Student\t\t2.Show Students\n3.Update Student\t4.Delete Student\n5.Exit"))

    match ch:
        
        case 1:
            n = input("Enter Student Name")
            r = int(input("Enter Roll No"))
            m = float(input("Enter Marks"))
            s = StudentInfo(n,r,m)
            students_list.append(s)
            print("Student Added")

        case 2:
            print("Showing Students")
            for stu in students_list:
                print(stu)

        case 3:
            result = return_student()
            if result:
                ch = int (input ('What do you wants to update\n''1.Name \n' '2. Marks\n'))
                match ch:
                    case 1:
                        newname = input ('Enter new name')
                        result. name = newname
                    case 2:
                        newmarks = int (input ('Enter new marks'))
                        result.marks = newmarks
                        print("Student Updated")
            else:
                print ('No such student')
                    
                    
        case 4:
            r = int(input("Enter Roll No to Delete:"))
            found = False
            for stu in students_list:
                if stu.rollno == r:
                    found = True
                    student_to_be_removed = stu
                    break
                print ("found=", found)
            if found:
                students_list. remove (student_to_be_removed)
                print (student_to_be_removed, "REMOVED!")
            else:
                print ("NO SUCH NOT FOUND!")
                print("\nAfter Deletion:")
            for stu in students_list:
                print(stu)
                
        case 5:
            print("Exit")
            break
        case _:
            print("invalid Choice")
        

    
    
               
