# 作者: 学不会
# 2026年10月16日17时38分31秒
# xxx@qq.com

import sys

print(sys.argv)

file =open(sys.argv[1],'r')
content = file.read()
print(content)
file.close()



