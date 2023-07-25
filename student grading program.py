def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
        return "D"
    else:
        return "Fail"

def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter the marks obtained: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Student Grading Program!")
    while True:
        marks = get_valid_marks()
        grade = calculate_grade(marks)
        print(f"The grade for the student is: {grade}")

        another_student = input("Do you want to calculate the grade for another student? (yes/no): ")
        if another_student.lower() != "yes":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
