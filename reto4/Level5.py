from helpers.helper import validate_value
from json import load, decoder, dump
from uuid import uuid4

data = {
    'students_created': [],
    'teachers_created': []
}

class Person:
    def __init__(self, name):
        self.name = name

 
    def interface(self):

        while True:
                print('''
                    Welcome to Student-Teacher system : 
                    ¿What do you do?
                    1) Manage Students
                    2) Manage Teachers
                    3) Quit\n
                ''')
                opcion_1 = input("> ")
                if opcion_1 == "1":
                    print('''
                                1) List students
                                2) Add a new student
                            ''')
                    
                    opcion_2 = input("> ")

                    if opcion_2 == "1":
                        self.show_students()
                    elif opcion_2 == "2":
                        scores = []
                        name = input(f"Enter student name\n")
                        while True:
                            score = input(f"[{name}]Enter score\n")
                            if validate_value(score) is True:
                                scores.append(int(score))

                            if input(f"Do yo want enter other note y/n?") == "y":
                                #print(scores)
                                pass
                            else:
                                break
            
                        student = Student(name, scores)
                        student.create_student(student)

                elif opcion_1 == "2": 
                     print('''
                                1) List teachers
                                2) Add a new teacher
                            ''')
                    
                     opcion_3 = input("> ")
                     if opcion_3 == "2":
                         name = input(f"Enter teacher name\n")
                         age = input(f"Enter teacher age \n")
                         dni = input(f"Enter teacher dni \n")

                         teacher = Teacher(name, age, dni)
                         teacher.create_teacher(teacher)

                     if opcion_3 == "1":
                        self.show_teachers()

                elif opcion_1 == "3":
                    print("\nThank you")
                    quit()
                else:
                    print("\nEnter a valid option")


class Student(Person):
    def __init__(self, name, scores):
        super().__init__(name)
        self.scores = scores

    def create_student(self, student):
        datos = {
            "id": str(uuid4()),
            "name": student.name,
            "scores": student.scores,
            "max_score": int(max(student.scores)),
            "min_score": int(min(student.scores)),
            "average_score": int(sum(student.scores)/len(student.scores))
        }
        self.save_student(datos)
        print(f"\nThe student {student.name} was successfully created")

    def save_student(self, datos):
        data['students_created'].append(datos)
        pjs = data['students_created']
        archivo = open("students.json", "w")
        dump(pjs, archivo, indent=4)
        archivo.close()
        
    def show_students(self):
        try:
            archivo = open("students.json", "r")
            data["students_created"] = load(archivo)
            archivo.close()
            for  student in data["students_created"]:
                print(f'''Name: {student["name"]}
                          Id: {student["id"]}
                          Scores: {student["scores"]}  
                          Min score: {student["min_score"]}  
                          Max score: {student["max_score"]}  
                          Average score: {student["average_score"]}  
                ''')
                 
                
        except FileNotFoundError:
            print("\n Creando registro de personajes...")
            archivo = open("students.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\nNo hay personajes creados, se puede crear desde ahora")


class Teacher(Person):
    def __init__(self, name, age, dni):
        super().__init__(name)
        self.dni = dni
        self.age = age

    def create_teacher(self, teacher):
        datos = {
            "id": str(uuid4()),
            "name": teacher.name,
            "age": teacher.age,
            "dni": teacher.dni
        }
        self.save_teacher(datos)
        print(f"\nThe teacher {teacher.name} was successfully created")

    def save_teacher(self, datos):
        data['teachers_created'].append(datos)
        pjs = data['teachers_created']
        archivo = open("teachers.json", "w")
        dump(pjs, archivo, indent=4)
        archivo.close()
        
    def show_teachers(self):
        try:
            archivo = open("teachers.json", "r")
            data["teachers_created"] = load(archivo)
            archivo.close()
            for  teacher in data["teachers_created"]:
                print(f'''Name: {teacher["name"]}
                          Id: {teacher["id"]}
                          age: {teacher["age"]}  
                          Identity card: {teacher["dni"]}   
                ''')
                 
                
        except FileNotFoundError:
            print("\n Creando registro de personajes...")
            archivo = open("teachers.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\nNo hay personajes creados, se puede crear desde ahora")


class Start(Teacher, Student):
    def __init__(self):
        try:
            #self.show_students()
            self.interface()
        except KeyboardInterrupt:
            print('\nAplicacion interrumpida')

Start()