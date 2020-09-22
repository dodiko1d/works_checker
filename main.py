import importlib
import students


for student in students.STUDENTS:
    student_work = importlib.import_module(f'students_works.{student}.solution')
    solution = student_work.func
    if solution() == True:
        print(f'{student} ok')
    else:
        print(f'{student} error')