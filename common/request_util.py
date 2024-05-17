import json
import requests
class Request:
    def __init__(self):
        self.session = requests.Session()
    def send_request(self,url,method,header=None,data=None,files=None,verify=False,**kwargs):
        method= method.lower()

        if method =='get':
            rep = Request().session.request(url=url,method=method,headers=header,params=data,verify=verify,**kwargs)
            return rep.json()
        elif method =='put':
            rep = Request().session.request(url=url, method=method, headers=header, json=data, verify=verify,
                                            **kwargs)
            return rep.json()
        else:
            if "application/x-www-form-urlencoded" in str(header.get("Content-Type")):
                rep = Request().session.request(url=url, method=method, headers=header, data=data, files=files,verify=verify,
                                                **kwargs)
            else:
                rep = Request().session.request(url=url, method=method, headers=header, json=data, files=files,verify=verify,
                                                **kwargs)
            return rep.json()


if __name__=="__main__":
    Request()
    method = 'post'
    url = 'http://42.193.175.165:18888/qitan-user/user/login'
    header = {"Content-Type": "application/json"}
    data = {"userPhone": 13652883290,
            "password": "Aa123456",
            "userAgent": "PC",
            "userType": "pwd-login"}
    re = Request().send_request(url, method, header, data)
    print(re)
