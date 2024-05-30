#!/usr/bin/env python3
"""importing the necessary modules"""
import re


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """function that returns the log message obfuscated:"""
    pattern = '|'.join([f'{field}=.*?(?={separator}|$)' for field in fields])
    return re.sub(pattern, lambda m:
                  f"{m.group(0).split('=')[0]}={redaction}", message)
