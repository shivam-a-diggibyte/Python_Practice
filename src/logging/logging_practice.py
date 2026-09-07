import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("Starting the process")
logging.info("Process is running normally")
logging.warning("Disk space is getting low")
logging.error("Failed to connect to the database")
logging.critical("System is shutting down")


# Program with logging functionality
import logging
 
logging.basicConfig(level=logging.INFO)
 
logging.info("Program started")
 
try:
    marks = int(input("Enter your marks: "))       # Ask user for marks
 
    if marks < 0 or marks > 100:
        logging.warning("Invalid marks entered")
    else:
        logging.info("Valid marks entered")
        print("Marks:", marks)
 
except ValueError:
    logging.error("User entered a non-numeric value")
 
logging.info("Program finished")