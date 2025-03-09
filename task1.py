student_name={
    "Bali":"90",
    "Kansa":"89",
    "Bakasura":"87",
    "Mahishasura":"50",
    "Ravan":"100"
}
user_input=input("enter studennt name: ")

if user_input in student_name:
    print(f"{user_input} score is : {student_name[user_input]}")

else:
    print("student not found")