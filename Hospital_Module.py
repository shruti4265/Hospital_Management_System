import logging

logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

hospitals = {}

def add_hospital(h_id, patient_list):
    try:
        if h_id in hospitals:
            print("Hospital already exists.")
            logging.warning("Hospital already exists.")
        else:
            hospitals[h_id] = patient_list
            print("Hospital added successfully.")
    except Exception as e:
        print(e)
        logging.error(str(e))
    else:
        logging.info(f"Hospital {h_id} added successfully.")