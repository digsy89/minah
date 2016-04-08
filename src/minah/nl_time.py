# -*- coding: utf-8 -*-

__HOUR__ = {
    "1"  : 1,  "한"   : 1,
    "2"  : 2,  "두"   : 2,
    "3"  : 3,  "세"   : 3,
    "4"  : 4,  "네"   : 4,
    "5"  : 5,  "다섯" : 5,
    "6"  : 6,  "여섯" : 6,
    "7"  : 7,  "일곱" : 7,
    "8"  : 8,  "여덟" : 8,
    "9"  : 9,  "아홉" : 9,
    "10" : 10, "열"   : 10,
    "11" : 11, "열한" : 11,
    "12" : 12, "열두" : 12
}

__NUMBER__ = {"": 0, "일":1, "이":2, "삼":3, "사":4, "오":5, "육":6, "칠":7, "팔":8, "구":9}

def parseNumber(text):
    """
        Parse number in natural language which of range is 1~60
    """
    ten = one = ""
    try:
        ten, one = text.split('십')
    except:
        one = text
    try:
        return __NUMBER__[ten]*10 + __NUMBER__[one]
    except KeyError:
        try:
            return int(text)
        except ValueError:
            return None

__TIMEZONE__ = {
    "오전" : 10,
    "아침" : 9,
    "새벽" : 5,
    "낮"   : 3,
    "오후" : 3,
    "저녁" : 6,
    "밤"   : 9
}

def parseTime(text):
    """
        Parse clock time in natural language
        return >> original_text, hour, minute
    """
    time_txt = ""
    pm = True
    hour = None
    minute = 0
    timezone = None
    txt = text

    if text == "":
        return "", 12, 0

    if txt[0] == ' ': txt = text[1:]; time_txt += ' '

    # Parse timezone
    for am in ['오전', '아침', '새벽']:
        if txt.startswith(am):
            pm = False
            txt = txt[len(am):]
            time_txt += am
            timezone = am
    for tz in __TIMEZONE__.keys():
        if txt.startswith(tz):
            txt = txt[len(tz):]
            time_txt += tz
            timezone = tz

    if txt[0] == ' ': txt = txt[1:]; time_txt += ' '

    # Parse hour
    si = txt.find('시')
    if si >= 0:
        try:
            hour = __HOUR__[txt[:si]]
            time_txt += txt[:si+len('시')]
            txt = txt[si+len('시'):]
        except KeyError:
            pass

    if txt[0] == ' ': txt = txt[1:]; time_txt += ' '

    # Parse minute
    bun = txt.find('분')
    if bun >= 0:
        minute = parseNumber(txt[:bun])
        if minute is not None:
            time_txt += txt[:bun+len('분')]
    elif txt.startswith('반'):
        minute = 30
        time_txt += '반'

    # Set default time, in case of no hour, minute
    if hour is None:
        if timezone is None:
            hour = 12
        else:
            hour = __TIMEZONE__[timezone]
    else:
        if timezone is not None and pm:
           hour += 12
        elif timezone is None:
           if hour < 8:
               hour += 12

    if time_txt==' ':
        time_txt=''

    return time_txt, hour, minute
