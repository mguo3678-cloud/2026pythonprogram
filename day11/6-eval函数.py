# 作者: 学不会
# 2026年10月16日17时48分29秒
# xxx@qq.com

#绝对不可以把前端发过来的数据给eval

# eval("__import__('os').system('ls')")

my_dict=eval('{"name":"张三","age":20,"city":"北京"}')
print(my_dict)

content=open('file4.conf','r')
my_dict1=eval(content.read())
print(my_dict1)