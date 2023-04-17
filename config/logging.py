import logging


logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] [%(message)s]',
                    filemode='a')

error_handler = logging.FileHandler('error.log')
error_handler.setLevel(logging.WARNING)
error_format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(message)s] tab')
error_handler.setFormatter(error_format)
logging.getLogger().addHandler(error_handler)

info_handler = logging.FileHandler('info.log')
info_handler.setLevel(logging.DEBUG)
info_format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(message)s] tab')
info_handler.setFormatter(info_format)
logging.getLogger().addHandler(info_handler)
