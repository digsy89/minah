# -*- coding:utf-8 -*-

from datetime import datetime, timedelta
import nl_time

TODAY = datetime.today

RELATIVE_DAY = [
    ["오늘", timedelta(days=0)],
    ["내일 모레", timedelta(days=2)],
    ["내일", timedelta(days=1)],
    ["모레", timedelta(days=2)],
    ["글피", timedelta(days=3)],
    ["어제", timedelta(days=-1)],
    ["그저께", timedelta(days=-2)]
]

DAYOFWEEK = {
    "월요일":0,
    "화요일":1,
    "수요일":2,
    "목요일":3,
    "금요일":4,
    "토요일":5,
    "일요일":6
}

WEEK = [
    ["이번주",timedelta(days=0)],
    ["지난주",timedelta(days=-7)],
    ["저번주",timedelta(days=-7)],
    ["다다음주",timedelta(days=14)],
    ["다음주",timedelta(days=7)]
]

DATE_FORMAT = "%m{0}%d"

def parseWeekDay(text):
    dayofweek = DAYOFWEEK[text[-9:]]
    time_txt = text[-9:]
    txt = text[:-9]

    _dt = TODAY()

    if txt.strip() != '' and txt[-1] == ' ': time_txt = ' ' + time_txt; txt = txt[:-1]

    for week, delta in WEEK:
        if txt.endswith(week):
            _dt += delta
            time_txt = week + time_txt
            break

    _dt += timedelta(days=dayofweek - _dt.weekday())

    return _dt, time_txt

def parse(sentence):
    result = []
    _dt = None
    remaining_sentence = sentence
    time_txt = ""

    for k, delta in RELATIVE_DAY:
        idx = sentence.find(k)
        if idx >= 0:
            remaining_sentence = sentence[idx+len(k):]
            _dt = TODAY()+delta
            time_txt = k
            break
    if _dt is None:
        for week in DAYOFWEEK.keys():
            idx = sentence.find(week)
            if idx >= 0:
                remaining_sentence = sentence[idx+len(week):]
                _dt, time_txt = parseWeekDay(sentence[:idx+len(week)])
                break

    _time, h, m = nl_time.parseTime(remaining_sentence)
    if _dt is None:
        if _time=='':
            return result
        else:
            _dt = TODAY()        

    _dt = _dt.replace(hour=h, minute=m, second=0, microsecond=0)
    time_txt += _time
    result += [[time_txt, _dt]]

    return result
