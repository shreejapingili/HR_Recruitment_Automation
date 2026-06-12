import logging
import os

# Create the logs folder automatically if it doesn't exist
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/process_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Automation Started")

print("Log Created")
