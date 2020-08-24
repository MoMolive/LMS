from operator import pos #导入包 定义要使用那个类
import requests,json
from time import sleep
session=requests.session()
code_cjxm_url = 'https://api.test.longan.eliteu.xyz/api/v1/courseprojects/'
code_cjxm_date={
  "accept": "application/json",
  "Content-Type": "application/json" ,
  "X-CSRFToken": "LSaNFGRYzI1F3dBGl50SiBeZcP2N2pLRMTqHBzkQAgI9syGAyHNCY709hChEJRYS",
  "title": "追赶游戏",
  "difficult_tags": "初级",
  "description": "玩儿过大鱼吃小鱼的游戏后，你想创作一个特别的追赶游戏，当抓住游戏中的角色时能得分。使用 Scratch，创作一个可以通过鼠标控制一个角色，去追逐另外一个角色的游戏。追到之后，你可以获取得分。",
  "cover": "https://course.longan.link/Scratch/%E5%B0%81%E9%9D%A2%E5%9B%BE%E7%89%87/%E8%BF%BD%E8%B5%B6%E6%B8%B8%E6%88%8F.png",
  "content": "https://course.longan.link/Scratch/%E5%AD%A6%E7%94%9F%E6%89%8B%E5%86%8C/%E6%B5%8B%E8%AF%95/%E6%B5%8B%E8%AF%95-%E8%BF%BD%E8%B5%B6%E6%B8%B8%E6%88%8F.md",
  "previewvideo": "",
  "category": "space",
  "knowledge_tags": "Scratch",
  "key_tags": "对象控制,重复循环,逻辑判断,指令属性模块",
  "result_tags": "动画",
  "hardware_tags": ""
}
ret=session.post(url=code_cjxm_url,data=code_cjxm_date)
print(ret.status_code)
print(ret.text)
re=ret.json()['id']
print(ret)
code_scxm_url = 'https://api.test.longan.eliteu.xyz/api/v1/courseprojects/{0}/'.format(ret)
ret = session.delete(url=code_scxm_url)
print(ret.status_code)
print(ret.text)
