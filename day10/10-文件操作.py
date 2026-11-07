# 作者: 学不会
# 2026年10月16日10时53分11秒
# xxx@qq.com
import os


def open_r():
    # read()只读方式打开文件。文件的指针将会放在文件的开头，这是默认模式。
    # 如果文件不存在，抛出异常
    # r+默认写在文件结尾 文件的指针将会放在文件的开头
    file = open('file', encoding='utf-8', mode='r+')
    text = file.read(5)
    print(text)
    file.write('Downloadanarchiveontaining')
    file.close()


def open_w():
    # w有创建文件的功能，如果文件存在，会清空文件内容
    file = open('file1', encoding='utf-8', mode='w+')
    file.write('helloworldhahaha1')
    text = file.read()
    print(text)
    file.close()


def open_a():
    # a+可以创建文件，打开文件时，a+的光标在文件末尾
    file = open('file2', encoding='utf-8', mode='a+')  # a模式默认光标在最后，读取不到内容
    file.seek(0, os.SEEK_SET)
    text = file.read()
    print(text)

    file.close()


def read_line():
    file = open('file')
    while True:
        text = file.readline()
        if not text:
            break
        # 每读取一行的末尾已经有了一个 `\n`
        print(text, end='')  # readline()读取一行，读取完后光标会停留在下一行的开头

    file.close()


def open_rb():
    file = open('file', mode='rb')
    text = file.read(5)
    print(text)
    file.write(b'Downloadanarchiveontaining')
    file.close()


if __name__ == '__main__':
    # open_r()
    # open_w()
    # open_a()
    # read_line()
    open_rb()
