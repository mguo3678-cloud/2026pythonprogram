# 作者: 学不会
# 2026年10月16日15时27分06秒
# xxx@qq.com

def use_wb():
    file1=open('img.png','rb')
    file2=open('img_copy.png','wb')
    while True:
        data=file1.read(10)
        if data:
            file2.write(data)
        else:
            break
    file1.close()
    file2.close()
if __name__ == '__main__':
    use_wb()