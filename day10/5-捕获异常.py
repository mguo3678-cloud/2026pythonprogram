# 作者: 学不会
# 2026年10月15日16时47分07秒
# xxx@qq.com

def except_base():
    try:
        print(1 / 0)
    except Exception as e:
        print(e)


def except_dif_type():
    try:
        num = int(input('请输入一个数字: '))
        ret = 10 / num
        print(ret)
    except ValueError:
        print('输入的不是数字')
    except ZeroDivisionError:
        print('除数不能为0')
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
        print(e.__traceback__.tb_lineno)
        # 发生异常所在的行数
    else:
        print("没有异常")
    finally:
        print("执行完毕")


if __name__ == '__main__':
    # except_base()
    except_dif_type()

