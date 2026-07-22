import logging
import Hospital_Module
import Patient_Module
import Search_Module
import Delete_Module
import View_Module

logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Hospital")
    print("2. Add Patient")
    print("3. View All")
    print("4. Search Patient")
    print("5. Delete Patient")
    print("6. Exit")

    try:

        choice = int(input("Enter Choice : "))

    except Exception as e:
        print("Invalid Input")
        logging.error(str(e))
        continue

    if choice == 1:

        try:

            h_id = int(input("Hospital ID : "))

            p_id = int(input("Patient ID : "))
            name = input("Patient Name : ")
            age = int(input("Age : "))
            disease = input("Disease : ")

            patient = {
                p_id: [name, age, disease]
            }

            Hospital_Module.add_hospital(h_id, patient)

        except Exception as e:
            print(e)

    elif choice == 2:

        try:

            h_id = int(input("Hospital ID : "))
            p_id = int(input("Patient ID : "))
            name = input("Patient Name : ")
            age = int(input("Age : "))
            disease = input("Disease : ")

            Patient_Module.add_patient(
                h_id,
                p_id,
                name,
                age,
                disease
            )

        except Exception as e:
            print(e)

    elif choice == 3:

        View_Module.view_all()

    elif choice == 4:

        try:

            p_id = int(input("Enter Patient ID : "))
            Search_Module.search_patient(p_id)

        except Exception as e:
            print(e)

    elif choice == 5:

        try:

            h_id = int(input("Hospital ID : "))
            p_id = int(input("Patient ID : "))

            Delete_Module.delete_patient(
                h_id,
                p_id
            )

        except Exception as e:
            print(e)

    elif choice == 6:

        print("Thank You")
        break

    else:
        print("Invalid Choice")