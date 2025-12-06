from logger import logger

def main():
    logger.info("Hello")
    logger.debug("Hello!", extra={'user':5555})

if __name__ == "__main__":
    main()