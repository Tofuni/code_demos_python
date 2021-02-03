# -*- coding: utf-8 -*-
"""
MODULES:
    F - 
        fileArray(fn) 
        fileAction(filename, act, body)
    A - 
        arrPrint(arr)
        arrToString(arr)
        arrStrSearch(arr, string)
        arrIterFn(arr, fn)
        arrFilter(arr, fnFilter)
        arrFilterGreaterThanFive(num)
        arrSurvey(arr)
        arrToText(arr)
        arrSurveyToFile(arr)
"""

try:
    import modules.files as F
    import modules.arrays as A
    import modules.custdates as D
except:
    print(Exception)

F.fileAction('spanish_vocal.csv','read','')