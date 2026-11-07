# 作者: 学不会
# 2026年10月14日12时24分04秒
# xxx@qq.com

class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具名称:{self.name},占地面积:{self.area}'


class House:
    def __init__(self, house_type, area, free_area, item_list):
        self.house_type = house_type
        self.area = area
        self.free_area = free_area
        self.item_list = []

    def __str__(self):
        return (f'户型:{self.house_type},面积:{self.area},'
                f'剩余面积:{self.free_area},家具列表:{self.item_list}')

    def add_item(self, item: HouseItem):#添加注解
        if item.area > self.free_area:
            print('家具占地面积超出剩余面积')
            return
        self.free_area += item.area
        self.item_list.append(item)
        print(f'添加家具:{item.name},剩余面积:{self.free_area}')

bed = HouseItem('床', 4)
table = HouseItem('桌子', 2)

print(bed)

house = House('别墅', 100, 80, [])
house.add_item(bed)
print(house)