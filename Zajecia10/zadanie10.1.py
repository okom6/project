import logging

def main():
    logger = logging.getLogger('spam_application')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('spam.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.info('creating an instance of auxiliary_module.Auxiliary')
    logger.info('created an instance of auxiliary_module.Auxiliary')
    logger.info('calling auxiliary_module.Auxiliary.do_something')
    logger.info('finished auxiliary_module.Auxiliary.do_something')
    logger.info('calling auxiliary_module.some_function()')
    logger.info('done with auxiliary_module.some_function()')

    logger.info("Start")
    logger.warning("Warn")
    logger.debug("A problem occurred")

if __name__ =="__main__":
    main()