import logging

def main():
    logging.basicConfig(filrname='C:\Users\student\Desktop\Zajecia10\app.log', level=logging.INFO)
    logging.info("Start")
    logging.warning("Warn")
    logging.debug("A problem occurred")

if __name__ =="__main__":
    main()
