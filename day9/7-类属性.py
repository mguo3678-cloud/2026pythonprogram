# 作者: 学不会
# 2026年10月15日14时24分31秒
# xxx@qq.com
class Tool:
    count = 0  # 通过类属性来记录工具的数量，用类名直接访问

    def __init__(self, name):
        print(self)
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print(cls)
        print(cls.count)


if __name__ == '__main__':
    tool1 = Tool('斧头')
    tool2 = Tool('锤子')
    tool3 = Tool('剪刀')
    print(Tool.count)
    Tool.show_tool_count()