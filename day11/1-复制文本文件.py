# 作者: 学不会
# 2026年10月16日15时19分39秒
# xxx@qq.com


file = open('file', 'r')
file1 = open('file1', 'w')
file1.write(file.read())
file1.close()
file.close()
