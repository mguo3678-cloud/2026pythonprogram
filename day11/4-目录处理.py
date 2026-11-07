# 作者: 学不会
# 2026年10月16日16时41分48秒
# xxx@qq.com

import os


def dir_use():
    # 列出当前目录下的所有文件和目录,不列出.和..目录
    print(os.listdir())

    # 创建目录
    # os.mkdir('test')
    # 删除目录
    # os.rmdir('test')
    # 获取当前目录的绝对路径
    print(os.getcwd())

    # 修改工作目录
    os.chdir('..')
    print(os.getcwd())

    # 判断是否为目录

    print(os.path.isdir('test'))


def file_use():
    # os.rename('file','file.txt')
    os.remove('text')

#目录的深度优先遍历
def dir_deep_traverse(path,width):
    files=os.listdir(path)
    for file in files:
        print(' '*width,file)
        out_path=os.path.join(path,file)
        if os.path.isdir(out_path):
            dir_deep_traverse(out_path,width+4)

#获取文件状态

def use_stat():
    file_info = os.stat('file.txt')
    print('size{},uid{},mode{:x},mtime{}'
          .format(file_info.st_size, file_info.st_uid,
                file_info.st_mode, file_info.st_mtime))
    from time import strftime
    from time import gmtime
    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime(file_info.st_mtime)))

if __name__ == '__main__':
    # dir_use()
    # file_use()
    # dir_deep_traverse('.',0)
    use_stat()