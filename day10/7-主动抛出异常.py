# 作者: 学不会
# 2026年10月15日19时11分05秒
# xxx@qq.com
def psw_check():
    psw = input("请输入密码：")
    if len(psw) >= 8:
        return psw

    print("主动抛出异常")
    ex = Exception("密码长度不足8位")
    raise ex


def use_assert():

    try:
        assert 1 == 0, "密码长度不足8位"
    except Exception as e:
        print(e)


def use_raise():
    try:
        print(psw_check())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # use_raise()
    use_assert()
