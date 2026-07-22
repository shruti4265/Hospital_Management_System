import logging
import Hospital_Module

logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def delete_patient(h_id, p_id):

    try:

        if h_id not in Hospital_Module.hospitals:
            print("Hospital not found.")

        elif p_id not in Hospital_Module.hospitals[h_id]:
            print("Patient not found.")

        else:

            del Hospital_Module.hospitals[h_id][p_id]

            print("Patient deleted successfully.")

    except Exception as e:
        print(e)
        logging.error(str(e))

    else:
        logging.info("Patient deleted.")