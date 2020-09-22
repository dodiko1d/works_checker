import os
import random
import students


os.mkdir('students_works')


for student in students.STUDENTS:
    os.mkdir(f'students_works/{student}')
    with open(f'students_works/__init__.py', 'w') as file:
        pass

    with open(f'students_works/{student}/solution.py', 'w') as solution:
        solution.write(f'def func():\n\treturn {random.choice([True, False])}')

    with open(f'students_works/{student}/__init__.py', 'w') as file:
        pass