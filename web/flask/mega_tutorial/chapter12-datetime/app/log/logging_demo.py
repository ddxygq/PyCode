import logging_module as log

if __name__ == '__main__':
    logger = log.getLogger('log.log', 'mylog')
    logger.error('test')