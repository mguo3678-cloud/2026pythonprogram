# 作者: 学不会
# 2026年10月13日19时20分23秒
# xxx@qq.com
# 具有默认值的参数就叫做缺省参数
def print_info(name, gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


# 必须保证带有默认值的缺省参数在参数列表末尾
# 所以，以下定义是错误的！
#    def print_info(name, gender=True, title)

# 如果有多个缺省参数，需要指定参数名，
def print_info(name, title="", gender=True):


    """
    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s%s 是 %s" % (title, name, gender_text))


if __name__ == '__main__':
    # print_info("小明")
    # print_info("小红", False)
    print_info("小明")
    print_info("老王", title="班长")
    print_info("小美", gender=False)