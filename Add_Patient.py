import logging
import Hospital_Module

logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def add_patient_to_hospital(h_id, patient_id, patient_name, age, disease):
    try:
        if h_id not in Hospital_Module.hospitals:
            print("Hospital not found.")
            logging.warning("Hospital not found.")

        else:
            if patient_id in Hospital_Module.hospitals[h_id]:
                print("Patient already exists.")
                logging.warning("Patient already exists.")

            else:
                Hospital_Module.hospitals[h_id][patient_id] = [
                    patient_name,
                    age,
                    disease
                ]

                print("Patient added successfully.")

    except Exception as e:
        print(e)
        logging.error(str(e))

    else:
        logging.info(f"Patient {patient_name} added successfully.")