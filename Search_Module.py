import logging
import Hospital_Module

logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def search_patient(p_id):

    try:

        found = False

        for h_id, patients in Hospital_Module.hospitals.items():

            if p_id in patients:

                print("\nHospital ID :", h_id)
                print("Patient ID  :", p_id)
                print("Name        :", patients[p_id][0])
                print("Age         :", patients[p_id][1])
                print("Disease     :", patients[p_id][2])

                found = True
                break

        if not found:
            print("Patient not found.")

    except Exception as e:
        print(e)
        logging.error(str(e))

    else:
        logging.info("Patient searched.")