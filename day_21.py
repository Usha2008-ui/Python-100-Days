def create_student_report(name,rollno,grade="A"):
    print("Name:", name)
    print("Roll Number:", rollno)
    print("Grade:", grade)
def avg(*marks):
    total = 0
    for i in marks:
        total += i
    avg = total / len(marks)
    print("Average marks:", avg)
def city_info(**kwargs):
    print("from ", kwargs["city_info"])
Name = "karan"
rollno = 12
total = [90, 80, 70, 60]
city = {"city_info": "Delhi"}
create_student_report(Name, rollno)
avg(*total)
city_info(**city)