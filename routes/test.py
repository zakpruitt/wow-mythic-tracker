from difflib import get_close_matches



dic = { }
dic["q1correct4"] = "0"
dic["q2correct3"] = "1"
dic["q3correct1"] = "2"
dic["q4correct2"] = "3"
dic["q5correct3"] = "4"

print(get_close_matches("q1correct", dic.keys()))
