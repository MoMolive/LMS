# coding=utf-8
'''
接口自动化框架设计
此模块放所有的接口入参信息
'''
cod_url='https://scratch.codelab.club/rest-auth/registration/'
cod_data={
        "birth_month": "2",
        "birth_year": "2007",
        "captcha": "228233",
        "country": "中国",
        "email": "746390263@qq.com",
        "gender": "female",
        "password": "HSJ123",
        "phone": "18203075348",
        "subscribe": True,
        "username": "SJ",
}

CODE_url='https://api.test.longan.eliteu.xyz/api-token-auth/'
CODE_data={
        "content-type": "application/json ",
        "username": "abc",
        "password": "123456"
}

COD_url='https://api.test.longan.eliteu.xyz/api/v1/captcha/'
COD_data={
        "Content-Type": "application/json",
        "X-CSRFToken": "KAJdRLp7AelqXsWxMJaGpFtNL0MyWxthyhmWgVjOEdaXERt2GxwJMOqplvtdwNL6",
        "phone":"17665340249"
}

CoDe_url='https://api.test.longan.eliteu.xyz/api/v1/covers/'

cod_hqpl_url='https://api.test.longan.eliteu.xyz/api/v1/comments/30/'
cod_hqpl_data={
        "id":34
}

code_scpl_url='https://api.test.longan.eliteu.xyz/api/v1/comments/3/'

code_hqallhf_url='https://api.test.longan.eliteu.xyz/api/v1/comments/24/replies/'

code_kcplcx_url='https://api.test.longan.eliteu.xyz/api/v1/coursecomments/'
code_kcplcx_data={
        "content": "你是猪吗？",
        "course": 3
}

code_fbkcpl_url='https://api.test.longan.eliteu.xyz/api/v1/coursecomments/'
code_fbkcpl_data={
  "content": "你是猪么？",
  "course": 1
}

code_hqkcpl_url='https://api.test.longan.eliteu.xyz/api/v1/coursecomments/24/'

code_PUTpl_url='https://api.test.longan.eliteu.xyz/api/v1/coursecomments/24/'
code_PUTpl_data={
          "content": "你是猪？？",
          "course": 3
}

code_XGpl_url='https://api.test.longan.eliteu.xyz/api/v1/coursecomments/24/'
code_XGpl_data={
  "content": "你是猪姐姐吗？",
  "course": 3
}

code_xgpl_url='https://api.test.longan.eliteu.xyz/api/v1/coursecomments/24/'
code_xgpl_data={
  "content": "你是猪么？",
  "course": 1
}

code_scPL_url='https://api.test.longan.eliteu.xyz/api/v1/coursecomments/29/'

code_pldz_url='https://api.test.longan.eliteu.xyz/api/v1/coursecomments/69/like/'
code_pldz_data={
  "content": "",
  "course": 3
}

code_qudz_url='https://api.test.longan.eliteu.xyz/api/v1/coursecomments/69/like/'

code_xmwz_url='https://api.test.longan.eliteu.xyz/api/v1/courseprojects/'

code_cxxm_url='https://api.test.longan.eliteu.xyz/api/v1/courseprojects/2/'
code_cxxm_data={
        "accept": "application/json" ,
        "X-CSRFToken": "LSaNFGRYzI1F3dBGl50SiBeZcP2N2pLRMTqHBzkQAgI9syGAyHNCY709hChEJRYS"
}

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

code_xgxm_url='https://api.test.longan.eliteu.xyz/api/v1/courseprojects/63/'
code_xgxm_data={
    "accept": "application/json",
    "Content-Type": "application/json" ,
    "X-CSRFToken": "LSaNFGRYzI1F3dBGl50SiBeZcP2N2pLRMTqHBzkQAgI9syGAyHNCY709hChEJRYS",
    "title": "最后一个追赶游戏",
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

code_tjxmnr_url='https://api.test.longan.eliteu.xyz/api/v1/courseprojects/63/'
code_tjxmnr_data={
"accept": "application/json",
    "Content-Type": "application/json" ,
    "X-CSRFToken": "LSaNFGRYzI1F3dBGl50SiBeZcP2N2pLRMTqHBzkQAgI9syGAyHNCY709hChEJRYS",
    "title": "就是一个追赶游戏",
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

code_cjkcwz_url='https://api.test.longan.eliteu.xyz/api/v1/courses/'
code_cjkcwz_data={
     "title": "双课程",
     "cover": "/image/course.png",
     "description": "全面建立双课程学习的知识架构",
     "content": "儿童可以编程 -- 从 Python 开始/课程介绍.md",
     "is_series": True,
     "knowledge_tags": "",
     "level_tags": "",
     "hardware_tags": ""
}

code_cxkc_url='https://api.test.longan.eliteu.xyz/api/v1/courses/2/'