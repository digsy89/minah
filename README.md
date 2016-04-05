# MINAH

Korean natural language date parser

Minah will recognize date in your sentence 

![Minah](http://file.thisisgame.com/upload/tboard/user/2013/06/21/20130621123440_8744.jpg)


## HOW TO WORK

heuristic..

## CAUTION

very dirty code

## USAGE
```
>>> import minah

>>> for original_text, date in minah.parse("다음주 금요일 저녁에 보자"):
...   print original_text, date
... 
다음주 금요일 저녁 2016-04-15 06:00:00
>>> print date.weekday()
4
```