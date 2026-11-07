# 作者: 学不会
# 2026年10月16日16时22分10秒
# xxx@qq.com
import os


def seek_stat():
    file = open('file', 'r+', encoding='utf-8')
    # 相对于开始位置开始偏移
    # file.seek(0, os.SEEK_SET)
    #相对于结尾开始偏移
    # file.seek(0, os.SEEK_END)#只能是0或正数
    #相对于当前位置开始偏移
    text=file.read(3)
    file.seek(0, os.SEEK_CUR) #偏移量为5，从当前位置开始偏移
    text = file.read()

    print(text)

    file.close()


if __name__ == '__main__':
    seek_stat()
