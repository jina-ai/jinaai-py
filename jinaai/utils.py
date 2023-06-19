import base64
import mimetypes
import os
import re

def is_url(string):
    url_pattern = r'^(?:\w+:)?\/\/([^\s.]+\.\S{2}|localhost[:?\d]*)\S*$'
    return bool(re.match(url_pattern, string))

def is_base64(string):
    base64_pattern = r'^data:[A-Za-z0-9+/]+;base64,'
    return bool(re.match(base64_pattern, string))

def image_to_base64(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            base64_data = base64.b64encode(file_data).decode('utf-8')
            mime_type = get_mime_type(file_path)
            base64_string = f"data:{mime_type};base64,{base64_data}"
            return base64_string
    except Exception as error:
        raise Exception(f"Image to base64 error: {str(error)}")

def get_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type or 'application/octet-stream'

