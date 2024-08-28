import time
import logging

# Configure logging
logging.basicConfig(filename='/tmp/live-translation.log', level=logging.INFO)

def run():
    while True:
        logging.info("Daemon is running")
        time.sleep(10)

if __name__ == "__main__":
        run()
