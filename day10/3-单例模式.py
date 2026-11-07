# 作者: 学不会
# 2026年10月15日15时55分14秒
# xxx@qq.com

class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    def __init__(self):
        print("初始化音乐播放器")

if __name__ == '__main__':
    music = MusicPlayer()
    music1 = MusicPlayer()
    print(id(music))
    print(id(music1))
