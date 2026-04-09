import json

FILE_NAME = "students.json"

# Utility Functions

def calculate_results(scores):
    avg = sum(scores) / len(scores)

    if avg >= 70:
        grade = "A"
        risk = "Low"
    elif avg >= 60:
        grade = "B"
        risk = "Low"
    elif avg >= 50:
        grade = "C"
        risk = "Moderate"
    elif avg >= 40:
        grade = "D"
        risk = "High"
    else:
        grade = "F"
        risk = "High"

    return avg, grade, risk


def save_to_file(student):
    try:
        data = load_from_file()
        data.append(student)

        with open(FILE_NAME, "w") as file:
            json.dump(data, file)
    except Exception as e:
        print("Error saving data:", e)


def load_from_file():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


# Core Functions

def register_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Invalid name.")
        return

    student_id = input("Enter student ID: ").strip()

    try:
        units = int(input("Enter number of units: "))
        if units <= 0:
            print("Units must be greater than 0.")
            return
    except:
        print("Invalid input.")
        return

    scores = []
    for i in range(units):
        try:
            score = float(input(f"Enter score for unit {i+1}: "))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")
                return
            scores.append(score)
        except:
            print("Invalid score input.")
            return

    avg, grade, risk = calculate_results(scores)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores,
        "average": avg,
        "grade": grade,
        "risk": risk
    }

    save_to_file(student)
    print("Student registered successfully!")


def display_students():
    data = load_from_file()

    if not data:
        print("No records found.")
        return

    for s in data:
        print("\n--------------------")
        print(f"Name: {s['name']}")
        print(f"ID: {s['id']}")
        print(f"Average: {s['average']:.2f}")
        print(f"Grade: {s['grade']}")
        print(f"Risk Level: {s['risk']}")


def main_menu():
    while True:
        print("\n--- SAMSS MENU ---")
        print("1. Register Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")


# Run program
main_menu()