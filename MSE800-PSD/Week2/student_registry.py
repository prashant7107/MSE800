# Global variable
student_records = []

class StudentRegister:
    def input_student(self, count=3):
        #   Function to collect data
        global student_records

        print(f"Enter data for student {count}")
        for i in range(1, count+1):
            print(f"\nStudent #{i}")
            name = input("Name: ")
            print("Please enter a number for age.")
            age = int(input("Age: "))
            sid = input("Student ID: ")

            student_records.append({
                "name": name, 
                "age": age, 
                "id": sid
            })

    def print_student(self):
        sorted_data = sorted(student_records, key=lambda x: x['age'])
        print("\n--- Sorted Student List ---")
        for student in sorted_data:
            print(f"Name: {student['name']} | Age: {student['age']} | Id: {student['id']}")


# Entry Point
if __name__ == "__main__":  
    manager = StudentRegister()
    
    manager.input_student(3)
    
    manager.print_student()