import logging
import os


class LogGen:
    @staticmethod
    def loggen(log_level=logging.INFO):
        log_file = r"D:\Algoscale wiki automation\src\logs\automation_log.log"

        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger("wiki automation")
        logger.setLevel(log_level)

        logger.handlers.clear()

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger
