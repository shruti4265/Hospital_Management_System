import logging
import Hospital_Module
import Add_Patient
import View

logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Hospital")
    print("2. View Hospitals")
    print("3. Add Patient")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except Exception as e:
        print("Invalid input.")
        logging.error(str(e))
        continue

    if choice == 1:

        try:
            h_id = int(input("Enter Hospital ID: "))

            patient_id = int(input("Enter Patient ID: "))
            patient_name = input("Enter Patient Name: ")
            age = int(input("Enter Age: "))
            disease = input("Enter Disease: ")

            patient_list = {
                patient_id: [patient_name, age, disease]
            }

            Hospital_Module.add_hospital(h_id, patient_list)

        except Exception as e:
            print("Invalid input.")
            logging.error(str(e))

    elif choice == 2:

        View.view_all_hospitals()

    elif choice == 3:

        try:
            h_id = int(input("Enter Hospital ID: "))
            patient_id = int(input("Enter Patient ID: "))
            patient_name = input("Enter Patient Name: ")
            age = int(input("Enter Age: "))
            disease = input("Enter Disease: ")

            Add_Patient.add_patient_to_hospital(
                h_id,
                patient_id,
                patient_name,
                age,
                disease
            )

        except Exception as e:
            print("Invalid input.")
            logging.error(str(e))

    elif choice == 4:
        print("Thank You")
        logging.info("Program exited.")
        break

    else:
        print("Invalid Choice")