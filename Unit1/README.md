PythonCookBook 1: 数据结构与算法
===

### 1.1: 将序列分解为单独的变量

    这一节的核心在于可迭代对象的分解

    a, b, .... n = (1, 2, 3, .... n)

### 1.2: 从任意长度的可迭代对象中分解元素

    对于长度不确定的分解可以采用"*表达式", 类似于正则表达式中的通配符

### 1.3: 保存最后N个元素

    这一节关键在于一个search函数，以及双端队列的使用

    from collections import deque
    """
    deque 的基本用法即特性:
    >> from collections import deque
    >> # 定长序列
    >> q = deque(maxlen=3)
    >> q.append(1)
    >> q.append(2)
    >> q.append(3)
    >> q
    [1, 2, 3]
    >> q.append(4)
    [2, 3, 4]
    >> # 不定长双端队列
    >> q = deque()
    >> q.append(2)
    >> q.appendleft(1)
    >> q
    [1, 2]
    >> q.popleft()
    1
    >> q
    [2]
    """

    def search(lines, pattern, history=5):
        """在lines查找pettern, 搜索历史为5条"""
        previous_lines = deque(maxlen=history)
        for line in lines:
            if pattern in line:
                yield line, previous_lines
            previous_lines.append(line)

    当编写搜索某项纪录的代码时，通常会用到含有yield关键字的生成器函数,这将处理搜索过程的代码和
    使用搜索结果的代码成功解耦开来。


### 1.4: 找到集合中最大或最小的N个元素

    使用heapq模块的nlargest和nsmallest函数

### 1.5: 实现优先级队列

    heappop 和 heappush 函数的使用

### 1.6: 将一个键映射到多个值上

    将键映射到多个值上，可以使用容器(ex:[])存放值
    collections模块的 defaultdict类可以简化创建这种字典的操作
        defaultdict(list)
    而且defaultdict会自动初始化第一个键值

## 1.7: 让字典保持有序

    collections 模块的 OrderedDict 类

## 1.8: 对字典进行相关计算

    默认的一些操作函数 min、max、sorted对字典的计算会对键进行计算
    但是使用zip函数可以将键值翻转，从而对值进行计算

## 1.9: 在字典中找寻相同的值

    pytho3中可以对list与list使用 &, -等操作符，方便我们比较字典

## 1.10: 删除序列中的重复对象且保持元素顺序不变

    关键在与集合(避免重复),与生成器(保持顺序不变)的结合使用

## 1.11: 对切片进行命名

    当大量使用切片这样的硬编码方式时，最好通过命名进行管理
    python 内置类slice类方便我们进行切片的命名创建

## 1.12: 找出序列中出现次数最多的元素

    collections模块的Counter函数的使用
    Counter对象可以接受任意可哈希的对象序列,
    在底层实现中，Counter是一个字典，在元素和元素出现的次数间做了映射

## 1.13: 通过公共键对字典列表排序

    通过公共键对字典列表排序的关键是sorted的key函数需要设置为
    我们希望设置的排序键

    operator 模块的 itemgetter函数是一个很好的工具
    key = itemgetter('key')
