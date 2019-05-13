# coding:utf8

from inter.httpkeyword import HTTP

if __name__ == "__main__":
    http = HTTP()
    http.seturl("http://112.74.191.10:8081/inter/HTTP")

    print("-----------------无token-------------------")
    http.removeheader("token")
    http.post("login","username=Will&password=123456")
    http.assertequals("status","405")

    print("-----------------token值为空-------------------")
    http.addheader("token")
    http.post("login","username=Will&password=123456")
    http.assertequals("status","405")

    print("-----------------token值过长-------------------")
    http.addheader("token","rghstrfdhsrhgerashaerherherrgerghergergergergergergergergr")
    http.post("login", "username=Will&password=123456")
    http.assertequals("status", "405")

    print("-----------------token未授权-------------------")
    http.addheader("token","0d862fe621ae4bca86489a554945b202")
    http.post("login", "username=Will&password=123456")
    http.assertequals("status", "405")

    print("-----------------token已经授权-------------------")
    http.addheader("token")
    http.post("auth")
    http.savejson("token","token")
    http.addheader("token","{token}")
    http.post("login", "username=Will&password=123456")
    http.assertequals("status", "200")

    print("-----------------token已经登录-------------------")
    http.addheader("token","{token}")
    http.post("login", "username=Will&password=123456")
    http.assertequals("status", "406")
    http.post("logout")

    print("-----------------无用户名-------------------")
    http.addheader("token")
    http.post("auth")
    http.savejson("token","token")
    http.addheader("token","{token}")
    http.post("login", "password=123456")
    http.assertequals("status", "402")

    print("-----------------用户名为空-------------------")
    http.post("login", "username=&password=123456")
    http.assertequals("status", "402")

    print("-----------------用户名为特殊字符：@$%^vfcs32-------------------")
    http.post("login", "username=@$%^vfcs32&password=123456")
    http.assertequals("status", "401")

    print("-----------------用户名为特殊字符：큐〓㊚32fdc-------------------")
    http.post("login", "username=큐〓㊚32fdc&password=123456")
    http.assertequals("status", "401")

    print("-----------------用户名为特殊字符：3r🚣l-------------------")
    http.post("login", "username=3r🚣l&password=123456")
    http.assertequals("status", "401")

    print("-----------------用户名边界值：用户名2位-------------------")
    http.post("login", "username=wi&password=123456")
    http.assertequals("status", "402")

    print("-----------------用户名边界值：用户名3位-------------------")
    http.post("login", "username=wil&password=123456")
    http.assertequals("status", "401")

    print("-----------------用户名边界值：用户名16位-------------------")
    http.post("login", "username=willwillwillwill&password=123456")
    http.assertequals("status", "401")

    print("-----------------用户名边界值：用户名17位-------------------")
    http.post("login", "username=willwillwillwillw&password=123456")
    http.assertequals("status", "402")

    print("-----------------用户名边界值：用户名过长-------------------")
    http.post("login", "username=willwillwillwillwillwillwillwillwillwillwillwillwillwillwillwill&password=123456")
    http.assertequals("status", "402")

    print("-----------------无密码-------------------")
    http.post("login", "username=Will")
    http.assertequals("status", "402")

    print("-----------------密码为空-------------------")
    http.post("login", "username=Will&password=")
    http.assertequals("status", "402")

    print("-----------------密码为特殊字符：@$%^vfcs32-------------------")
    http.post("login", "username=Will&password=@$%^vfcs32")
    http.assertequals("status", "401")

    print("-----------------密码为特殊字符：큐〓㊚32fdc-------------------")
    http.post("login", "username=Will&password=큐〓㊚32fdc")
    http.assertequals("status", "401")

    print("-----------------密码为特殊字符：3r🚣l-------------------")
    http.post("login", "username=Will&password=3r🚣l")
    http.assertequals("status", "401")

    print("-----------------密码边界值：密码2位-------------------")
    http.post("login", "username=Will&password=65")
    http.assertequals("status", "402")

    print("-----------------密码边界值：密码3位-------------------")
    http.post("login", "username=Will&password=456")
    http.assertequals("status", "401")

    print("-----------------密码边界值：密码16位-------------------")
    http.post("login", "username=Will&password=1234561234561234")
    http.assertequals("status", "401")

    print("-----------------密码边界值：密码17位-------------------")
    http.post("login", "username=Will&password=12345612345612345")
    http.assertequals("status", "402")

    print("-----------------用户名边界值：用户名过长-------------------")
    http.post("login", "username=Will&password=12345612345612345123456123456123451234561234561234512345612345612345")
    http.assertequals("status", "402")

    print("-----------------字段测试：无用户名密码-------------------")
    http.post("login")
    http.assertequals("status", "402")

    print("-----------------字段测试：3个字段-------------------")
    http.post("login", "username=Will&password=123456&aaa=bbb")
    http.assertequals("status", "200")
    http.post("logout")
    http.addheader("token")
    http.post("auth")
    http.savejson("token","token")
    http.addheader("token","{token}")

    print("-----------------等价类测试：用户名密码错误-------------------")
    http.post("login", "username=Will&password=654321")
    http.assertequals("status", "401")

    print("-----------------等价类测试：用户名不存在-------------------")
    http.post("login", "username=lliW&password=123456")
    http.assertequals("status", "401")

    print("-----------------等价类测试：用户名密码不匹配-------------------")
    http.post("login", "username=Will&password=tufei")
    http.assertequals("status", "401")

    print("-----------------等价类测试：用户名密码正确-------------------")
    http.post("login", "username=Will&password=123456")
    http.assertequals("status", "200")

    print("-----------------SQL注入测试1-------------------")
    http.post("logout")
    http.addheader("token")
    http.post("auth")
    http.savejson("token", "token")
    http.addheader("token", "{token}")
    http.post("login", "username=Will' or 1=1 #&password=123456")
    http.assertequals("status", "401")

    print("-----------------SQL注入测试2-------------------")
    http.post("logout")
    http.addheader("token")
    http.post("auth")
    http.savejson("token", "token")
    http.addheader("token", "{token}")
    http.post("login", "username=Will&password=1' or 1=1 #")
    http.assertequals("status", "401")