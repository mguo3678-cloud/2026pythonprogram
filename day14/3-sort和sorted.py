# 作者: 学不会
# 2026年10月23日18时43分25秒
# xxx@qq.com
from operator import itemgetter, attrgetter

print(sorted({1: 'D', 2: 'B', 3: 'B', 5: 'E', 4: 'A'}))

str_list = "This is a test string from Andrew".split()
print(str_list)
print(sorted(str_list, key=str.lower))  # str.lower()将字符串转换为小写，key=str.lower表示按照小写排序

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# lambda表达式 匿名函数
print(sorted(student_tuples, key=lambda student: student[2]))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    # 重写 __repr__ 方法，以便在打印时显示对象的详细信息，而不是对象的内存地址
    # repr()方法用于返回对象的字符串表示形式，通常用于调试和日志记录
    def __repr__(self):
        return repr((self.name, self.grade, self.age))


print(f'使用repr----------------------')
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda student: student.age))

# operator 库函数自定义排序
print(f'使用operator库函数--------------------------------')
print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('age')))

# 多层排序
print(f'多层排序--------------------------------')
print(sorted(student_tuples, key=itemgetter(1, 2)))

print(sorted(student_objects, key=attrgetter('grade', 'age')))

# 字典中混合list排序
mydict = {'Li': ['M', 7],
          'Zhang': ['E', 2],
          'Wang': ['P', 3],
          'Du': ['C', 2],
          'Ma': ['C', 9],
          'Zhe': ['H', 7]}
# 针对字典 mydict 的 value 结构 [n,m] 中的 m 按照从小到大的顺序排列。
print(sorted(mydict.items(), key=lambda x: x[1][1]))
gameresult = [{"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
              {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
              {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
              {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]

print(sorted(gameresult, key=itemgetter("rating", "wins")))

# 第一个升序，第二个降序怎么搞
tup1es = [(3, 5), (1, 2), (2, 4), (3, 1), (1, 3)]
print(sorted(tup1es, key=lambda x: (x[0], -x[1])))
