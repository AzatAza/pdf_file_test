import logging

logger = logging.getLogger("api")

def custom_logger(response):
    url = response.url
    method = response.request.method
    status = response.status_code
    logger.info(f'Url is {url}, method is {method}, status is {status}')
