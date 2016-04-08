from datetime import datetime
import re

__formatted_date_regex__ = "(\d{2,4}[\/|.|\-])?\d{1,2}(\/|\.|-)\d{1,2}( \d{1,2}:\d{1,2}(:\d{1,2})?)?"
__formatted_date_pattern__ = re.compile(__formatted_date_regex__)

__DATETIME__  = 0
__YEAR__      = 1
__DELIMITER__ = 2
__TIME__      = 3
__SECOND__    = 4

def parse(sentence):
    result = []
    for m in __formatted_date_pattern__.finditer(sentence):
        df = ""
        if m.group(__YEAR__) is not None:
            df += "%Y{0}" if len(m.group(__YEAR__))>3 else "%y{0}"
        df += "%m{0}%d"
        if m.group(__TIME__) is not None:
             df += " %H:%M"
             if m.group(__SECOND__) is not None:
                 df += ":%S"
        df = df.format(m.group(__DELIMITER__))
        result += [[m.group(0), datetime.strptime(m.group(0), df)]]
    return result
