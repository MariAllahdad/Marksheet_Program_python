# MARKSHEET PROGRAM
print('Please Enter Your Subjects Marks for Calculate Grade')
physics = int(input('Enter Physics Marks: '))
chemistry = int(input('Enter Chemistry Marks: '))
Math = int(input('Enter Math Marks: '))

optain_marks = (physics + chemistry + Math)
total = 300
percentage = (optain_marks/total) * 100
print(f'S_Name    Optain Marks    Total')

if(percentage >=80 and percentage <=100):
    print(f'Physics \t {physics}   \t\t  100')
    print(f'Chemistry \t {chemistry} \t\t  100')
    print(f'Math         {Math}   \t\t  100')
    print(f'OptainMarks  {optain_marks}   \t\t  {total}')
    print('Grade A')
    print('Result PASS')
    print(f'Percentaget {percentage}' )

elif(percentage>=60 and percentage <=80):
    print(f'Physics \t {physics}   \t\t  100')
    print(f'Chemistry \t {chemistry} \t\t  100')
    print(f'Math         {Math}   \t\t  100')
    print(f'OptainMarks  {optain_marks}   \t\t  {total}')
    print('Grade B')
    print('Result PASS')
    print(f'Percentaget {percentage}')
elif(percentage>=40 and percentage <=60):
    print(f'Physics \t {physics}   \t\t  100')
    print(f'Chemistry \t {chemistry} \t\t  100')
    print(f'Math         {Math}   \t\t  100')
    print(f'OptainMarks  {optain_marks}   \t\t  {total}')
    print('Grade C')
    print('Result PASS')
    print(f'Percentaget {percentage}')
else:
    print('You Are Fail ')



