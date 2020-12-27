d= {}
student_name = {"Bahar", "bahar", "BAHAR"}
student_surname = {"Demir", "demir", "DEMİR"}
xy = [student_name, student_surname]
print(xy)
for i in range(3):
    i=i+1
    name = str(input("Please input Name  : "))
    surname = str(input("Please input Surname: "))
    if name not in student_name and surname not in student_surname:
        print(f"Last your {3 - i} chance")
    else:
        print(f"Welcome '{name}''{surname}'")
    Checklist = ["COURSE LIST"]
    x = int(input("How many lesson do you take? :"))
    while True:
        if 3 > x or x > 5:
            print("You failed in class")
            print(f"{x}  please write a number that between 3 and 5!")
            x = int(input("How many lesson do you take? :"))
            continue
        else:
            for k in range(x):
                k += 1
                c = str(input(f"Enter {k}. lesson:"))
                keys = [f"{k}. Lesson {c}"]
                Checklist.append(keys)
        for k in Checklist:
            print(*k)
        Course = int(input("Please write lesson number that you want to choose :"))
        while True:
            if 1 > Course or Course > x:
                print(f"Enter a Lesson number from 1 to {x}")
                Course = int(input("Please write lesson number : "))
            else:
                print(f"{Checklist[Course]}")
                Midterm_result = int(input("Please enter Midterm Exam result  : "))
                Final_result = int(input("Please enter Final Exam result : "))
                Project_result = int(input("PLease enter Project result   : "))
                while True:
                    if not 0 <= Midterm_result <= 100:
                        print("Please enter Midterm note is between 0 and 100")
                        Midterm_result = int(input("Please enter Midterm Exam result   : "))
                    break
                while True:
                    if not 0 <= Final_result <= 100:
                        print("Please enter  Final note is between 0 and 100")
                        Final_result = int(input("Please enter Final Exam result : "))
                    break
                while True:
                    if not 0 <= Project_result <= 100:
                        print("Please enter a Project note is between 0 and 100")
                        Project_result = int(input("PLease enter Project result : "))
                    break
                Graduate_grade = Midterm_result * 0.3 + Final_result * 0.5 + Project_result * 0.2
                if 90 <= Graduate_grade < 100:
                    s = str("AA")
                elif 70 <= Graduate_grade < 90:
                    s = str("BB")
                elif 50 <= Graduate_grade < 70:
                    s = str("CC")
                elif 30 <= Graduate_grade < 50:
                    s = str("DD")
                else:
                    Graduate_grade < 30
                    s = str("FF, you failed!")
                d["Course"] = Course
                d["Midterm"] = Midterm_result
                d["Final"] = Final_result
                d["Project"] = Project_result
                d["Graduate grade"] = Graduate_grade
                d["Letter Grade"] = s
                print(d)
            break
        break
    break
