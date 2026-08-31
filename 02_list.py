# 创建一个数字列表
numbers=[121,22,31,64,15,24,20]
# 给列表numbers插入添加一个数据20,在列表的末尾
print(numbers)
# 给列表numbers插入添加一个数据10,索引为3
numbers.insert(3,10)
print(numbers)
# 输出从小到大排序的列表numbers
print(sorted(numbers))
# 输出从大到小排序的列表numbers
print(sorted(numbers,reverse=True))
# 给列表numbers删除数据22
numbers.remove(22)
print(numbers)
# 查找列表中最大的数字
print(max(numbers))
# 查找列表中最小的数字
print(min(numbers))
numbers.sort(reverse=False)
