import sys
import logging
from src.logger import logging
#This imports the sys module, which allows access to sys.exc_info() — a function that returns info about the most recent exception.

import traceback


def error_message_detail(error, error_detail: sys):
    '''A function to generate a detailed error message.'''
    
    exc_type, exc_value, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script [{0}] at line [{1}] with error: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message




