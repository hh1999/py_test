#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib.request as request
import urllib.error as error
import json


# 天气预报查询示例
def Life():
    api_url = 'http://apis.juhe.cn/simpleWeather/life'
    params_dict = {
        "city": "北京",  # 查询天气的城市名称，如：北京、苏州、上海
        "key": "cbdb91f07db2908ea07987faa53762d7",  # 您申请的接口API接口请求Key
    }
    params = urllib.parse.urlencode(params_dict)
    try:
        req = request.Request(api_url, params.encode())
        response = request.urlopen(req)
        content = response.read()
        if content:
            try:
                result = json.loads(content)
                error_code = result['error_code']
                if (error_code == 0):
                    kongtiao = result['result']['life']['kongtiao']
                    guomin = result['result']['life']['guomin']
                    shushidu = result['result']['life']['shushidu']
                    chuanyi = result['result']['life']['chuanyi']
                    diaoyu = result['result']['life']['diaoyu']
                    ganmao = result['result']['life']['ganmao']
                    xiche = result['result']['life']['xiche']
                    ziwaixian = result['result']['life']['ziwaixian']
                    yundong = result['result']['life']['yundong']
                    daisan = result['result']['life']['daisan']
                    print("空调开启：%s\n过敏：%s\n舒适度：%s\n穿衣：%s\n钓鱼：%s\n感冒：%s\n紫外线：%s\n洗车：%s\n运动：%s\n带伞：%s" % (
                        kongtiao, guomin, shushidu, chuanyi, diaoyu, ganmao, ziwaixian,xiche,yundong,daisan))
                else:
                    print("请求失败:%s %s" % (result['error_code'], result['reason']))
            except Exception as e:
                print("解析结果异常：%s" % e)
        else:
            # 可能网络异常等问题，无法获取返回内容，请求异常
            print("请求异常")
    except error.HTTPError as err:
        print(err)
    except error.URLError as err:
        # 其他异常
        print(err)


if __name__ == '__main__':
    Life()

