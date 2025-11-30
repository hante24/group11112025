from logger import logger

def main():
    logger.info("Hello")
    logger.warning("Hello", extra={"user": 123})
    logger.error("Hello", extra={"user": 123})
    logger.critical("Hello", extra={"user": 123})

if __name__ == "__main__":
    main()
