# 作者: 学不会
# 2026年10月23日09时25分16秒
# xxx@qq.com
import  random
class Hash:
    def __init__(self,hash_table_size):
        self.hash_table_size = hash_table_size
        self.hash_table = [None] * hash_table_size#初始化哈希表

    def elf_hash(self,hash_str):
        h=0#初始化哈希值
        g=0#初始化g值,g是哈希值的高4位
        for i in hash_str:
            h = (h << 4) + ord(i)#左移4位,然后加上字符的ASCII码
        g = h & 0xf0000000
        if g:
            h ^= g >> 24
        h &= ~g
        return h % self.hash_table_size

if __name__ == '__main__':
    str_list=["xiongda","lele","hanmeimei","wangdao","fenghua"]
    stu_list=[]#创建学生列表
    temp_dict={}#创建字典,用于存储学生信息,避免引用问题
    for i in str_list:
        temp_dict['name']=i#创建字典
        temp_dict['age']=random.randint(18,30)#随机生成年龄
        stu_list.append(temp_dict.copy())#复制字典,避免引用问题,copy()方法返回一个新的字典副本，而不是引用原来的字典。
        temp_dict.clear()
    print(stu_list)
    h=Hash(10)#初始化哈希表
    for stu in stu_list:#遍历学生列表
        index=h.elf_hash(stu['name'])#计算哈希值
        if h.hash_table[index] is None:#哈希表为空
            h.hash_table[index]=[stu]#存储时，直接封装为列表
        else:
            print("哈希冲突")
            h.hash_table[index].append(stu)#哈希冲突时，将学生信息添加到列表中

    student_name=input("请输入学生姓名:")
    index=h.elf_hash(student_name)#计算哈希值

    #查询对应姓名的学生信息，针对有哈希冲突的如何进行哈希查找
    for stu in stu_list:
        if stu['name']==student_name:
            print(f'找到了{stu}')
            break

