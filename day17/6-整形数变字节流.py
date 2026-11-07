# 作者: 学不会
# 2026年10月30日18时41分14秒
# xxx@qq.com


import struct

temp_bytes = struct.pack('I', 12345)
print(temp_bytes)
temp_int = struct.unpack('I', temp_bytes)
print(temp_int)


