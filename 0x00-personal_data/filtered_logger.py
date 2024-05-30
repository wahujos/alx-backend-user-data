#!/usr/bin/env python3
"""importing the necessary modules"""
import re
from typing import List


import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        # NotImplementedError
        message = super().format(record)
        redacted_message = filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR)
        return redacted_message


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """function that returns the log message obfuscated:"""
    pattern = '|'.join([f'{field}=.*?(?={separator}|$)' for field in fields])
    return re.sub(pattern, lambda m:
                  f"{m.group(0).split('=')[0]}={redaction}", message)
