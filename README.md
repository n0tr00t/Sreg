### Sreg V1.0

- AppName: Sreg [Search Registration]
- Create:  2015-03-03
- Author:  Dave, Evi1m0, Hel
- Website: [http://n0tr00t.github.io/Sreg/](http://n0tr00t.github.io/Sreg/)


Sreg可对使用者通过输入```email```、```phone```、```username```的返回用户注册的所有互联网护照信息，例如：

    ➜  Sreg git:(master) python reg_test.py -h
    usage: reg_test.py [-h] [-u USER] [-e EMAIL] [-c CELLPHONE]

    Check how many Platforms the User registered.

    optional arguments:
      -h, --help    show this help message and exit
      -u USER
      -e EMAIL
      -c CELLPHONE

    ➜  Sreg git:(master) ✗ python reg_test.py -e test@test.com

         .d8888b.
        d88P  Y88b
        Y88b.
         "Y888b.  888d888 .d88b.  .d88b.
            "Y88b.888P"  d8P  Y8bd88P"88b
              "888888    88888888888  888
        Y88b  d88P888    Y8b.    Y88b 888
         "Y8888P" 888     "Y8888  "Y88888
                                      888
                                 Y8b d88P
                                  "Y88P"

    [*] App: Search Registration
    [*] Version: V1.0(20150303)
    [*] Website: buzz.beebeeto.com

    [+] Email Checking: test@test.com

    [购物] 淘男网 (http://www.51taonan.com/)
    [IT] 51cto (http://www.51cto.com)
    [娱乐] 一听音乐网 (http://www.1ting.com/)
    [工具] 金山词霸 (http://www.iciba.com/)
    [生活] 58同城 (http://www.58.com/)
    [名站] 优酷 (http://www.youku.com)
    [IT] 果壳网 (http://www.guokr.com/)
    [购物] 好乐买 (http://www.okbuy.com/)
    [旅行] 艺龙 (http://www.elong.com/)
    [旅游] 凯撒旅游网 (http://www.caissa.com.cn/)
    [旅游] 酷讯旅游网 (http://www.kuxun.cn)
    [娱乐] 乐视网 (http://www.youku.com)
    [IT] CSDN (http://www.csdn.net/)
    [生活] 百合网 (http://www.baihe.com/)
    [购物] 当当网 (http://www.dangdang.com/)

    [+] Results the save path: ./reports/email_test@test.com.html
    
Sreg一共有三种查询方式：
 
  - 用户名
  - 手机
  - 邮箱

查询完成后，Sreg会返回给使用者一个精致的html页面供以查看。
    
### Plugin (SDK)

编写网站注册查询插件非常简单，首先将想要进行编写的网站在```/plugins/```建立对应```website.json```文件。

    {
        "information":{
            "author" : "evi1m0",
            "date" : "2015/03/10",
            "name" : "PPTV",
            "website" : "http://www.pptv.com/",
            "category" : "娱乐",
            "icon" : "http://static9.pplive.cn/pub/flagment/v_20150309153320/modules/g-1408-hd/images/logo.png",
            "desc" : "PPTV聚力-始终和你同一频道,汇聚最清晰,最流畅的网络各类最新热门直播、点播视频。"
        },

        "request" :{
            "cellphone_url" : "http://api.passport.pptv.com/v3/query/loginname_exist.do?logintype=username&username={}",
            "email_url" : "http://api.passport.pptv.com/v3/query/loginname_exist.do?logintype=username&username={}",
            "user_url" : "http://api.passport.pptv.com/v3/query/loginname_exist.do?logintype=username&username={}",
            "method" : "GET",
            "post_fields":{

            }
        },

        "status":{
            "judge_yes_keyword" : "<errorCode>5</errorCode>",
            "judge_no_keyword" : "<errorCode>0</errorCode>",
            "profile_url" : ""
        }
    }

  - information: 插件编写者及网站所需信息；
  - request: 核心接口定义，其中cellphone, email, user分别位手机注册、邮箱注册、用户名注册查询接口，如果仅有手机注册查询接口，其他则均为相同API即可；
  - status: 返回结果判断，judge_yes_keyword为用户已经注册此网站，相反为未注册此网站，profile_url为预留字段；
  
如果接口为POST方法，则修改method为POST后，定义post_fields为参数字段，例renren：

    "request" :{
        "cellphone_url" : "http://reg.renren.com/AjaxRegisterAuth.do",
        "email_url" : "http://reg.renren.com/AjaxRegisterAuth.do",
        "user_url" : "http://reg.renren.com/AjaxRegisterAuth.do",
        "method" : "POST",
        "post_fields":{
            "authType":"email",
            "value":"",
            "stage":"3"
        }
    },



### Category

 - IT
 - 名站
 - 娱乐
 - 工具
 - 教育
 - 旅行
 - 游戏
 - 生活
 - 社交
 - 社区
 - 购物
 - 资讯
 - 其它
 - 求职招聘
