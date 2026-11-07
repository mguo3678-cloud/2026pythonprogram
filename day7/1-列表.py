# 作者: 学不会
# 2026年10月11日16时31分25秒
# xxx@qq.com


def list_demo():
    name_list = ["zhangsan", "lisi", "wangwu"]
    # 1.取值
    print(name_list[0])
    # 知道数据的内容，想确定数据在列表中的位置
    print(name_list.index("lisi"))
    # 2.修改
    name_list[0] = "zhangsan1"
    print(name_list)
    # 3.添加
    name_list.append("zhaoliu")
    print(name_list)
    name_list.insert(1, "乐乐")
    print(name_list)
    # extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾
    temp_list = ["孙悟空", "猪二哥", "沙师弟"]
    name_list.extend(temp_list)
    print(name_list)
    # 4.删除
    name_list.remove("乐乐")
    print(name_list)
    name_list.pop(2)
    print(name_list)

    del name_list[0]
    print(name_list)
    # clear清空列表
    print(id(name_list))
    name_list.clear()
    print(name_list)
    print(id(name_list))


# 列表的统计
def list_demo2():
    name_list = ["张三", "李四", "王五", "王小二", "张三"]
    # len(length 长度) 函数可以统计列表中元素的总数
    list_len = len(name_list)
    print("列表中包含 %d 个元素" % list_len)
    # count 方法可以统计列表中某一个数据出现的次数
    count = name_list.count("张三")
    print("张三出现了 %d 次" % count)


def list_sort():
    name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
    num_list = [6, 8, 4, 1, 10]
    # 升序
    name_list.sort()
    num_list.sort()
    # 降序
    name_list.sort(reverse=True)
    num_list.sort(reverse=True)
    # 逆序（反转）
    name_list.reverse()
    num_list.reverse()
    print(name_list)
    print(num_list)

    # def list_iter():
    """
    遍历加删除时，用while不要用for
    :return:
    """
    # num_list = [5, 4, 3, 2, 5, 2]
    # num_list_len = len(num_list)
    # for i in range(num_list_len):
    #     if num_list[i] == 5:
    #         del num_list[i]
    #         num_list_len -= 1
    # print(num_list)


def list_while():
    num_list = [2, 5, 5, 4, 3, 2, 5, 2]
    num_list_len = len(num_list)
    i = 0
    while i < num_list_len:
        if (num_list[i] == 5):
            del num_list[i]
            num_list_len -= 1
        else:
            i += 1
    print(num_list)


if __name__ == "__main__":
    # 增删改查
    # list_demo()
    # 列表统计
    # list_demo2()
    # 列表排序
    # list_sort()
    # list_iter()
    list_while()
