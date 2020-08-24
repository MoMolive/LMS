# coding=utf-8
import unittest,json
from api.code_api import Code_api
import random
class CODE_test(unittest.TestCase):
    def setUp(self):
        return '开始执行'
    def tearDown(self):
        return '执行完毕'
    def test01_code(self):
        result=Code_api().cod_ZX()
        try:
            if result.get('username')=="已存在一位使用该名字的用户。" or result.get('email')=="该邮箱地址已被注册。" or result.get('invalid')=="验证码错误.":
                print("注册失败，请重新输入")
            else:
                print("注册成功")
        except Exception as e:
            print("exception", e)
            return
    def test02_code(self):
            result=Code_api().cx_dlcx()
            try:
                if result['phone']=="17665340249":
                    print('发送验证信息成功')
                else:
                    print('发送验证信息失败')
            except:
                return
    def test03_code(self):
        result=Code_api().cx_yzm()
        try:
            if result['token']==None:
                print('查询登录失败')
            else:
                print('查询登录成功')
        except:
            return
    def test04_code(self):
        result=Code_api().cx_png()
        try:
            if result['image']==None:
                print('图片调用失败')
            else:
                print('图片调用成功')
        except:
            return
    def test05_code(self):
        result=Code_api().cx_hqpl()
        try:
            if result['id']==30:
                print('查询评论成功')
            else:
                print('查询评论失败')
        except:
            return
    def test06_code(self):
        result = Code_api().cx_scpl()
        try:
            if result['detail'] == "You are not the author." or result['detail']=="未找到。":
                print('你不是作者或未找到该评论！删除失败')
            else:
                print ("评论删除成功")
        except:
            return
    def test07_code(self):
        result = Code_api().cx_hqallpl()
        try:
            if result == []:
                print('获取评论回复成功')
            else:
                print('获取回复评论失败')
        except:
            return
    def test08_code(self):
        result=Code_api().cx_kcplcxall()
        try:
            if result['count']==29:
                print('获取课程评论成功')
            else:
                print('获取评论失败')
        except:
            return
    def test09_code(self):
        result=Code_api().cx_fbpl()
        try:
            if result['username']=='abc':
                print('发表课程评论成功')
            else:
                print('发表课程评论失败')
        except:
            return
    def test10_code(self):
        result=Code_api().cx_hqkcpl()
        try:
            if result['name']=='BOBO':
                print('获取课程评论成功')
            else:
                print('获取评论失败')
        except:
            return
    def test11_code(self):
        result=Code_api().cx_PUTpl()
        try:
            if result['is_like']==False:
                print('评论课程成功')
            else:
                print('评论失败')
        except:
            return
    def test12_code(self):
        result=Code_api().cx_XGpl()
        try:
            if result['content']=="你是猪姐姐吗？":
                print('修改课程评论成功')
            else:
                print('修改课程评论失败')
        except:
            return
    def test13_code(self):
        result=Code_api().cx_xgpl()
        try:
            if result['is_like']==False:
                print('修改成功')
            else:
                print('修改失败')
        except:
            return
    # def test14_code(self):
    #     result=Code_api().cx_scPL()
    #     try:
    #         if result==None:
    #             print("删除成功")
    #         else:
    #             print('删除失败')
    #     except:
    #         return
    def test15_code(self):
        result=Code_api().cx_pldz()
        try:
            if result==None:
                print('点赞成功')
            else:
                print('点赞失败')
        except:
            return
    def test16_code(self):
        result=Code_api().cx_qxdz()
        try:
            if result==None:
                print('取消点赞成功')
            else:
                print('取消点赞失败')
        except:
            return
    def test17_code(self):
        result=Code_api().cx_xmcx()
        try:
            if result['count']==2:
                print('查询此账户下所有项目成功')
            else:
                print('查询所有项目失败')
        except:
            return
    def test18_code(self):
        result=Code_api().cx_cj_scxm()
        try:
            if result==None:
                print('创建并删除此项目成功')
            else:
                print('创建删除项目失败')
        except:
            return
    def test19_code(self):
        result=Code_api().cx_cxxm()
        try:
            if result['id']==2:
                print('查询 “害羞的熊猫” 项目成功')
            else:
                print('查询失败')
        except:
            return
    def test20_code(self):
        result=Code_api().cx_xgxm()
        try:
            if result['id']=='9':
                print('修改“追赶游戏”项目名称成功')
            else:
                print('修改项目失败')
        except:
            return
    def test21_code(self):
        result=Code_api().cx_tjxmnr()
        try:
            if result['id']=='9':
                print('添加/修改项目内容成功')
            else:
                print('添加/修改项目内容失败')
        except:
            return
    def test22_code(self):
        result=Code_api().cx_hqkc()
        try:
            if result['count']==0:
                print('获取tag课程失败')
            else:
                print('获取tag课程成功')
        except Exception as e:
            print("exception", e)
            return
    def test23_code(self):
        result=Code_api().cx_cxkc1()
        try:
            if "id" in result:
                print('查询单一课程成功')
            if "id" not in result:
                print("查询单一课程失败")
        except:
            return

    def test24_code(self):
        result=Code_api()
        try:
            if result['']=='':
                print('')
            else:
                print('')
        except:
            return
    def test25_code(self):
        result=Code_api()
        try:
            if result['']=='':
                print()
            else:
                print()
        except:
            return
    def test26_code(self):
        result=Code_api()
        try:
            if result['']=='':
                print()
            else:
                print()
        except:
            return
    def test27_code(self):
        result=Code_api()
        try:
            if result['']=='':
                print()
            else:
                print()
        except:
            return
    def test28_code(self):
        result=Code_api()
        try:
            if result['']=='':
                print()
            else:
                print()
        except:
            return
