# coding=utf-8
from confo.code_conf import *
import requests
from time import sleep

session=requests.session()
class Code_api(object):
    def __init__(self):
        pass
    def cod_ZX(self):
        rep=session.post(url=cod_url,data=cod_data)
        # print(rep.text)
        return rep.json()
    def cx_dlcx(self):
        rep=session.post(url=COD_url,data=COD_data)
        # print(rep.text)
        return rep.json()
    def cx_yzm(self):
        rep=session.post(url=CODE_url,data=CODE_data)
        # print(rep.text)
        return rep.json()
    def cx_png(self):
        rep=session.get(url=CoDe_url)
        # print(rep.text)
        return rep.json()
    def cx_hqpl(self):
        # headers = {
        #     "Cookie": "_ga=GA1.2.285131633.1593651977; _gid=GA1.2.2111788223.1593651977; csrftoken=vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX; scratchsessionsid=86n6if425ww6t4k194kkyyeqxxeiy01e"
        # }
        rep=session.get(url=cod_hqpl_url,data=cod_hqpl_data)
        print(rep.text)
        # return rep.json()
    def cx_scpl(self):
        headers = {
            "Cookie": "_ga=GA1.2.285131633.1593651977; _gid=GA1.2.2111788223.1593651977; csrftoken=vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX; scratchsessionsid=86n6if425ww6t4k194kkyyeqxxeiy01e",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken":"vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX"
        }
        rep=session.delete(url=code_scpl_url,headers=headers)
        # print(rep.text)
        return rep.json()
    def cx_hqallpl(self):
        rep=requests.get(url=code_hqallhf_url)
        # print(rep.text)
        return rep.json()
    def cx_kcplcxall(self):
        headers = {
            "Cookie": "_ga=GA1.2.285131633.1593651977; _gid=GA1.2.2111788223.1593651977; csrftoken=vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX; scratchsessionsid=86n6if425ww6t4k194kkyyeqxxeiy01e",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken": "vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX"
        }
        rep=requests.session().get(url=code_kcplcx_url,data=code_kcplcx_data,headers=headers)
        # print(rep.text)
        return rep.json()
    def cx_fbpl(self):
        headers={
            "Cookie": "_ga=GA1.2.285131633.1593651977; _gid=GA1.2.2111788223.1593651977; csrftoken=vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX; scratchsessionsid=86n6if425ww6t4k194kkyyeqxxeiy01e",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken": "vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX"
        }
        rep=requests.post(url=code_fbkcpl_url,data=code_fbkcpl_data,headers=headers)
        # print(rep.text)
        return rep.json()
    def cx_hqkcpl(self):
        headers = {
            "Cookie": "_ga=GA1.2.285131633.1593651977; _gid=GA1.2.2111788223.1593651977; csrftoken=vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX; scratchsessionsid=86n6if425ww6t4k194kkyyeqxxeiy01e",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken": "vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX"
        }
        rep=session.get(url=code_hqkcpl_url,headers=headers)
        # print(rep.text)
        return rep.json()
    def cx_PUTpl(self):
        headers = {
            "Cookie": "_ga=GA1.2.285131633.1593651977; _gid=GA1.2.2111788223.1593651977; csrftoken=vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX; scratchsessionsid=86n6if425ww6t4k194kkyyeqxxeiy01e",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken": "vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX"
        }
        rep=session.put(url=code_PUTpl_url,headers=headers,data=code_PUTpl_data)
        # print(rep.text)
        return rep.json()
    def cx_XGpl(self):
        headers = {
            "Cookie": "_ga=GA1.2.285131633.1593651977; _gid=GA1.2.2111788223.1593651977; csrftoken=vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX; scratchsessionsid=86n6if425ww6t4k194kkyyeqxxeiy01e",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken": "vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX"
        }
        rep=session.put(url=code_XGpl_url,data=code_XGpl_data,headers=headers)
        # print(rep.text)
        return rep.json()
    def cx_xgpl(self):
        headers={
            "Cookie": "_ga=GA1.2.285131633.1593651977; _gid=GA1.2.2111788223.1593651977; csrftoken=vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX; scratchsessionsid=86n6if425ww6t4k194kkyyeqxxeiy01e",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken": "vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX"
        }
        rep=session.patch(url=code_xgpl_url,data=code_xgpl_data,headers=headers)
        # print(rep.text)
        return rep.json()
    def cx_scPL(self):
        headers={
            "Cookie": "_ga=GA1.2.285131633.1593651977; _gid=GA1.2.2111788223.1593651977; csrftoken=vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX; scratchsessionsid=86n6if425ww6t4k194kkyyeqxxeiy01e",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken": "vl4782lbTljdvO8taPG0PSjEbOZo9DZuCyMWPaMRB67eKJbkFpBURIKBZrPtiCkX"
        }
        rep=session.delete(url=code_scPL_url,headers=headers)
        # print(rep.text)
        return rep.json()
    def cx_pldz(self):
        headers = {
            "Cookie": "_ga=GA1.2.1948998215.1594621522; _gid=GA1.2.1674838571.1594621522; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozNTUsInVzZXJuYW1lIjoiYWJjIiwicGhvbmUiOiIxNzY2NTM0MDI0OSIsInVzZXJfdHlwZSI6InRlYWNoZXIiLCJleHAiOjE1OTcyMjIwOTgsImVtYWlsIjoiIiwiaXNzIjoibG9uZ2FuLXVzZXJjZW50ZXIifQ.-YStSmwF2FdCwwjSdbMuv3uDRUZNzrhQPeeSijZ_PXg; messages=11651a192bbf34218e20f38905fb26832bf2ab84$[[\"__json_message\"\0540\05425\054\"Successfully signed in as abc.\"]]; csrftoken=iwS7LUHmqLyfr2JWmuyNpshv61QeQ92A3TboJPIPOXkNooD4fMPLh75NW53cWKwP; scratchsessionsid=imyoxb4oyqaqr2bphoitg54cu1iuc1ca",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken": "Rv2RghWLxpjURyX9rjfYuSyE2OVMKf5zCSl8ecXeVB5sOURhkBwWmxmWSS8KQQzO"
        }
        session.put(url=code_pldz_url,data=code_pldz_data,headers=headers)
        # rep=session.put(url=code_pldz_url,data=code_pldz_data,headers=headers)
        # print(rep.text)
    def cx_qxdz(self):
        headers = {
            "Cookie": "_ga=GA1.2.1948998215.1594621522; _gid=GA1.2.1674838571.1594621522; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozNTUsInVzZXJuYW1lIjoiYWJjIiwicGhvbmUiOiIxNzY2NTM0MDI0OSIsInVzZXJfdHlwZSI6InRlYWNoZXIiLCJleHAiOjE1OTcyMjIwOTgsImVtYWlsIjoiIiwiaXNzIjoibG9uZ2FuLXVzZXJjZW50ZXIifQ.-YStSmwF2FdCwwjSdbMuv3uDRUZNzrhQPeeSijZ_PXg; messages=11651a192bbf34218e20f38905fb26832bf2ab84$[[\"__json_message\"\0540\05425\054\"Successfully signed in as abc.\"]]; csrftoken=iwS7LUHmqLyfr2JWmuyNpshv61QeQ92A3TboJPIPOXkNooD4fMPLh75NW53cWKwP; scratchsessionsid=imyoxb4oyqaqr2bphoitg54cu1iuc1ca",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken": "Rv2RghWLxpjURyX9rjfYuSyE2OVMKf5zCSl8ecXeVB5sOURhkBwWmxmWSS8KQQzO"
        }
        session.delete(url=code_qudz_url,headers=headers)
        # rep = session.delete(url=code_qudz_url, headers=headers)
        # print(rep.text)
    def cx_xmcx(self):
        # headers = {
        #     "Cookie": "_ga=GA1.2.750634542.1594181894; _gid=GA1.2.807300913.1594181894; messages=11651a192bbf34218e20f38905fb26832bf2ab84$[[\"__json_message\"\0540\05425\054\"Successfully signed in as abc.\"]]; scratchsessionsid=hqqbvfdce3xba9qgcd9iwvah3azb6lrf; csrftoken=NmGzUHR5HWGBqtWYJDMgiddXpvouMwh4dXDqfPk2BdOShOwRmqFcMXAP9sSGk7XM; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozNTUsInVzZXJuYW1lIjoiYWJjIiwicGhvbmUiOiIxNzY2NTM0MDI0OSIsInVzZXJfdHlwZSI6InRlYWNoZXIiLCJleHAiOjE1OTY3ODQ4MDIsImVtYWlsIjoiIiwiaXNzIjoibG9uZ2FuLXVzZXJjZW50ZXIifQ.6BqAs6b1tY7fBUsOImXOOvqzLD0dAuOQ4f4ROfTIJ3E",
        #     "Referer": "https://api.test.longan.eliteu.xyz/",
        #     "X-CSRFToken": "O9J6uVKWmR7cbJpB2fsHN9bqB0BtJVJTb1U6JLPhtKlr7gCESy6rv7qDFYyWQXBO"
        # }
        rep=session.get(url=code_xmwz_url)
        # print(rep.text)
        return rep.json()
    def cx_cxxm(self):
        rep=session.get(url=code_cxxm_url,data=code_cxxm_data)
        # print(rep.text)
        return rep.json()
    def cx_xgxm(self):
        rep=session.put(url=code_xgxm_url,data=code_xgxm_data)
        # print(rep.text)
        return rep.json()
    def cx_tjxmnr(self):
        rep=session.patch(url=code_tjxmnr_url,data=code_tjxmnr_data)
        # print(rep.text)
        return rep.json()
    def cx_cj_scxm(self):
        rep = session.post(url=code_cjxm_url, data=code_cjxm_date)
        # print(ret.status_code)
        print(rep.text)
        re=rep.json()['id']
        sleep(1)
        code_scxm_url = 'https://api.test.longan.eliteu.xyz/api/v1/courseprojects/{0}/'.format(re)
        session.delete(url=code_scxm_url)
        # ret = session.delete(url=code_scxm_url)
        # print(ret.status_code)
        # print(ret.text)
    def cx_hqkc(self):
        code_hqkc_url='https://api.test.longan.eliteu.xyz/api/v1/courses/'
        # session.get(url=code_hqkc_url)
        a=session.get(url=code_hqkc_url)
        print(a.text)
        return a.json()
    def cx_cjkcwz(self):
        headers = {
            "Cookie": "_ga=GA1.2.750634542.1594181894; _gid=GA1.2.807300913.1594181894; messages=11651a192bbf34218e20f38905fb26832bf2ab84$[[\"__json_message\"\0540\05425\054\"Successfully signed in as abc.\"]]; scratchsessionsid=hqqbvfdce3xba9qgcd9iwvah3azb6lrf; csrftoken=NmGzUHR5HWGBqtWYJDMgiddXpvouMwh4dXDqfPk2BdOShOwRmqFcMXAP9sSGk7XM; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozNTUsInVzZXJuYW1lIjoiYWJjIiwicGhvbmUiOiIxNzY2NTM0MDI0OSIsInVzZXJfdHlwZSI6InRlYWNoZXIiLCJleHAiOjE1OTY3ODQ4MDIsImVtYWlsIjoiIiwiaXNzIjoibG9uZ2FuLXVzZXJjZW50ZXIifQ.6BqAs6b1tY7fBUsOImXOOvqzLD0dAuOQ4f4ROfTIJ3E",
            "Referer": "https://api.test.longan.eliteu.xyz/",
            "X-CSRFToken": "O9J6uVKWmR7cbJpB2fsHN9bqB0BtJVJTb1U6JLPhtKlr7gCESy6rv7qDFYyWQXBO"
        }
        rep = session.post(url=code_cjkcwz_url,data=code_cjkcwz_data,headers=headers)
        # print(rep.text)
        return rep.json()
    def cx_cxkc1(self):
        rep = session.get(url=code_cxkc_url)
        print(rep.text)
        return
if __name__=="__main__":
    b = headers = {
        "Cookie": "_ga=GA1.2.750634542.1594181894; _gid=GA1.2.807300913.1594181894; messages=11651a192bbf34218e20f38905fb26832bf2ab84$[[\"__json_message\"\0540\05425\054\"Successfully signed in as abc.\"]]; scratchsessionsid=hqqbvfdce3xba9qgcd9iwvah3azb6lrf; csrftoken=NmGzUHR5HWGBqtWYJDMgiddXpvouMwh4dXDqfPk2BdOShOwRmqFcMXAP9sSGk7XM; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozNTUsInVzZXJuYW1lIjoiYWJjIiwicGhvbmUiOiIxNzY2NTM0MDI0OSIsInVzZXJfdHlwZSI6InRlYWNoZXIiLCJleHAiOjE1OTY3ODQ4MDIsImVtYWlsIjoiIiwiaXNzIjoibG9uZ2FuLXVzZXJjZW50ZXIifQ.6BqAs6b1tY7fBUsOImXOOvqzLD0dAuOQ4f4ROfTIJ3E",
        "Referer": "https://api.test.longan.eliteu.xyz/",
        "X-CSRFToken": "O9J6uVKWmR7cbJpB2fsHN9bqB0BtJVJTb1U6JLPhtKlr7gCESy6rv7qDFYyWQXBO"
    }
    c=Code_api()
    # c.cod_ZX(),c.cx_dlcx(),c.cx_yzm(),c.cx_png(),c.cx_hqpl(),c.cx_scpl(),c.cx_hqallpl(),c.cx_kcplcxall(),c.cx_fbpl(),c.cx_hqkcpl(),c.cx_PUTpl(),c.cx_XGpl(),c.cx_xgpl(),c.cx_scPL(),c.cx_pldz(),c.cx_qxdz(),c.cx_xmcx(),c.cx_cxxm(),c.cx_xgxm(),c.cx_tjxmnr(),c.cx_cj_scxm(),c.cx_hqkc(),c.cx_cjkcwz()
    c.cx_cxkc1()