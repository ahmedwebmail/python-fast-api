from pygments.lexers import data

import logging

# Configure Logging
logging.basicConfig(
    filename = "error.log",
    level = logging.INFO,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def login(username):
    logging.info(f"Logging in: {username}")

def process_data(data):
    try:
        if data == "bad_data":
            raise ValueError("Invalid data")
        logging.info(f"Data processed: {data}")
    except ValueError as e:
        logging.error(f"Error processing data: {e}", exc_info=True)

def logout(username):
    logging.info(f"Logging out: {username}")

if __name__ == "__main__":
    user_name = "ahmed"
    login(user_name)
    process_data("bad_data")
    logout(user_name)