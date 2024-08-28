import time
import logging
from translator import execute, languages, voices

# Configure logging
logging.basicConfig(filename='/tmp/live-translation.log', level=logging.INFO)

def run():
    while True:
        logging.info("Daemon is running")
        language = "es"
        execute(language=languages[language], voice=voices[language], debug=False)

if __name__ == "__main__":
        run()
