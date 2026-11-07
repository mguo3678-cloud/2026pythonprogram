# 作者: 学不会
# 2026年10月11日20时05分07秒
# xxx@qq.com
xiaoming_dict = {"name": "小明"}

print(xiaoming_dict)
print(xiaoming_dict['name'])
print(xiaoming_dict.get('name'))  # get没有找到对应键，返回None
print('-' * 50)
# 2. 增加/修改
# 如果key不存在，会新增键值对
xiaoming_dict["age"] = 18
# 如果key存在，会修改已经存在的键值对
xiaoming_dict["name"] = "小小明"
print(xiaoming_dict)
print('-' * 50)
# 3. 删除
xiaoming_dict.pop("name")
# 在删除指定键值对的时候，如果指定的key不存在，程序会报错！
# xiaoming_dict.pop("name123")
# 2. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}
# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)
print('-' * 50)
# 3. 清空字典
print(id(xiaoming_dict))
xiaoming_dict.clear()
print(id(xiaoming_dict))

xiaoming_dict = {"name": "小明",
                 "qq": "123456",
                 "phone": "10086"}
# 迭代遍历字典
# 变量k是每一次循环中，获取到的键值对的key
for k in xiaoming_dict:
    print(f'{k}: {xiaoming_dict[k]}')
# 会以元组的形式输出
for k in xiaoming_dict.items():
    print(k)
for k, v in xiaoming_dict.items():
    print(k, v)
print('-' * 50)
# 将 多个字典 放在 一个列表 中，再进行遍历
# 会以字典的形式输出
card_list = [
    {"name": "张三",
     "qq": "12345",
     "phone": "110"},
    {"name": "李四",
     "qq": "54321",
     "phone": "10086"}
]

for card_info in card_list:
    print(card_info)
