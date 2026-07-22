import logging
import Hospital_Module

logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def add_patient(h_id, p_id, name, age, disease):

    try:

        if h_id not in Hospital_Module.hospitals:
            print("Hospital not found.")

        elif p_id in Hospital_Module.hospitals[h_id]:
            print("Patient already exists.")

        else:
            Hospital_Module.hospitals[h_id][p_id] = [
                name,
                age,
                disease
            ]

            print("Patient added successfully.")

    except Exception as e:
        print(e)
        logging.error(str(e))

    else:
        logging.info(f"Patient {name} added successfully.")