import logging

loger = logging.getLogger('my-logger')
loger.setLevel(logging.DEBUG)

log_format = '%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s'
log_formatter = logging.Formatter(log_format, style='%')

file_handler = logging.FileHandler('logger.log')
file_handler.setFormatter(log_formatter)

loger.addHandler(file_handler)


class log_class():
    def load_data():
        loger.info('Dataset downloaded')
    
    def add_done():
        loger.debug('add completed')
    
if __name__ == '__main__':
    log_class.load_data()
    log_class.add_done()
    