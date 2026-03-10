import logging

def initilize_logger():
    logging.basicConfig(    
        filename="log.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
