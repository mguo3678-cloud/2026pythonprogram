# 作者: 学不会
# 2026年10月23日09时26分45秒
# xxx@qq.com


def binary_search(arr, target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>target:
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
        else:
            return mid
    return -1

if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9]
    target=0
    pos=binary_search(arr,target)
    if pos!=-1:
        print(f"元素{target}在数组中的索引为{pos}")
    else:
        print(f"元素{target}不在数组中")