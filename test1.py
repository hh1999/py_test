import pytest

from CityList import CityList
from Life import Life
from Weather import Weather
from Wids import Wids


def test_1():
    try:
        Weather()
    except Exception as e:
        print("运行失败：%s" % e)

def test_2():
    try:
        Life()
    except Exception as e:
        print("运行失败：%s" % e)

def test_3():
    try:
        Wids()
    except Exception as e:
        print("运行失败：%s" % e)

def test_4():
    try:
        CityList()
    except Exception as e:
        print("运行失败：%s" % e)