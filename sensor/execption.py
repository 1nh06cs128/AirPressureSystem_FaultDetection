import sys, os

def error_message_detail(error, error_detail: sys):
    _, _, exe_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.
    
    error_message = " Error occured at python script name [0]"
    
    return error_message

class SensorException(Exception):
    
    def __init__(self, error_message, error_detail:sys):
        