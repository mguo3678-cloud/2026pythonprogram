# 作者: 学不会
# 2026年10月14日12时31分29秒
# xxx@qq.com

class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            print("%s 发射了 %d 颗子弹..." % (self.model, self.bullet_count))
        else:
            print("没有子弹了")


class Soldier:
    def __init__(self, name):
        # 1. 姓名
        self.name = name
        # 2. 枪- 新兵没有枪
        self.gun = None

    def fire(self):
        # 1. 判断士兵是否有枪
        # if self.gun == None:
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)
            return
        # 2. 高喊口号
        print("冲啊...[%s]" % self.name)
        # 3. 让枪装填子弹
        self.gun.add_bullet(50)
        # 4. 让枪发射子弹
        self.gun.shoot()


# 1. 创建枪对象
ak47 = Gun("AK47")
# 2. 创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
# print(xusanduo.gun)

# 创建枪对象
# ak47 = Gun("ak47")
# ak47.add_bullet(50)
# ak47.shoot()
