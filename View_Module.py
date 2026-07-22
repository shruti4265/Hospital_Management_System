import logging
import Hospital_Module

logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def view_all():

    try:

        if not Hospital_Module.hospitals:
            print("No hospitals available.")

        else:

            for h_id, patients in Hospital_Module.hospitals.items():

                print("\nHospital ID :", h_id)

                for p_id, details in patients.items():

                    print("----------------------")
                    print("Patient ID :", p_id)
                    print("Name       :", details[0])
                    print("Age        :", details[1])
                    print("Disease    :", details[2])

    except Exception as e:
        print(e)
        logging.error(str(e))

    else:
        logging.info("Displayed all records.")