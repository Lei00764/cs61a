## 使用函数构建抽象

Pure function纯函数：调用它们时除了返回一个值之外没有其它效果。

Sided function带副作用的函数：除了返回一个值之外，调用非纯函数会产生副作用，这会改变解释器或计算机的一些状态。例如print，会在屏幕上打印指定内容。



Lab 00 and Lab 01 已完成

HW 01 已完成



- 函数名称应该小写，以下划线分隔。提倡描述性的名称。
- 函数名称通常反映解释器向参数应用的操作（例如`print`、`add`、`square`），或者结果（例如`max`、`abs`、`sum`）。
- 参数名称应小写，以下划线分隔。提倡单个词的名称。
- 参数名称应该反映参数在函数中的作用，并不仅仅是满足的值的类型。
- 当作用非常明确时，单个字母的参数名称可以接受，但是永远不要使用`l`（小写的`L`）和`O`（大写的`o`），或者`I`（大写的`i`）来避免和数字混淆。

### 如何编写良好的函数

- 每个函数都应该只做一个任务。这个任务可以使用短小的名称来定义，使用一行文本来标识。顺序执行多个任务的函数应该拆分在多个函数中。
- 不要重复劳动（DRY）是软件工程的中心法则。所谓的DRY原则规定多个代码段不应该描述重复的逻辑。反之，逻辑应该只实现一次，指定一个名称，并且多次使用。如果你发现自己在复制粘贴一段代码，你可能发现了一个使用函数抽象的机会。
- 函数应该定义得通常一些，准确来说，平方并不是在 Python 库中，因为它是`pow`函数的一个特例，这个函数计算任何数的任何次方。

Python 包含了多种假值，包括 0、`None`和布尔值`False`。所有其他数值都是真值。

### and or not

为了求出表达式`<left> and <right>`：

1. 求出子表达式`<left>`。
2. 如果结果`v`是假值，那么表达式求值为`v`。
3. 否则表达式的值为子表达式`<right>`。

为了求出表达式`<left> or <right>`：

1. 求出子表达式`<left>`。
2. 如果结果`v`是真值，那么表达式求值为`v`。
3. 否则表达式的值为子表达式`<right>`。

为了求出表达式`not <exp>`：

1. 求出`<exp>`，如果值是`True`那么返回值是假值，如果为`False`则反之。

### 测试

断言：程序员使用`assert`语句来验证预期，例如测试函数的输出。`assert`语句在布尔上下文中只有一个表达式，后面是带引号的一行文本（单引号或双引号都可以，但是要一致）如果表达式求值为假，它就会显示。

```python
assert fib(8) == 13, 'The 8th Fibonacci number should be 13'
```

在文件中而不是直接在解释器中编写 Python 时，测试可以写在同一个文件，或者后缀为`_test.py`的相邻文件中。



Doctest：Python 提供了一个便利的方法，将简单的测试直接写到函数的文档字符串内。文档字符串的第一行应该包含单行的函数描述，后面是一个空行。参数和行为的详细描述可以跟随在后面。此外，文档字符串可以包含调用该函数的简单交互式会话：

```python3
def fib(n):
    """
    Fibonacci number

    >>> fib(1)
    0
    >>> fib(8)
    13
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

```bash
python3 -m doctest <python_source_file>
```

若测试结果正确，不会有任何显示。

### 高阶函数

高阶函数的重要性是，它允许我们更加明显地将这些抽象表达为编程语言中的元素，使它们能够处理其它的计算元素。

通常，编程语言会限制操作计算元素的途径。带有最少限制的元素被称为具有一等地位。一些一等元素的“权利和特权”是：

1. 它们可以绑定到名称。
2. 它们可以作为参数向函数传递。
3. 它们可以作为函数的返回值返回。
4. 它们可以包含在数据结构中。

Python 总是给予函数一等地位，所产生的表现力的收益是巨大的。另一方面，控制结构不能做到：你不能像使用`sum`那样将`if`传给一个函数。

### 装饰器

一般而言，装饰器是一个 输入和输出均为函数 的函数。

经验：在运行函数前，会先运行这个函数前的装饰器。装饰器一般用于代码重复量较大的时候，就比如系统登陆的校验，在装饰器中检验一下token值，以后呢代码就可以直接调用。

```python
import time

def display_time(func):  # 这里display_time接受一个函数作为参数
    def wrapper(*args):  # 默认名称
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print("Total time: ", t2 - t1)
        return result
    
    return wrapper


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if (num % i == 0):
                return False
        return True

@display_time  # 装饰器
def count_prime_nums(n):
    count = 0
    for i in range(2, n):
        if is_prime(i) == True:
            count += 1
    return count

print(count_prime_nums(10000))
```

https://www.bilibili.com/video/BV11s411V7Dt/

- 若count_prime_nums有返回值该怎么做？ 在wrapper函数返回
- 若count_prime_nums有参数该怎么做？ 在wrapper函数中传递参数，使用*args，表示任意数量的参数

```python
def make_adder(x):
    def adder(y):
        return x + y
    return adder  # 函数
  	# return adder(x) # 值 错误！！！ 

print(make_adder(1)(3))

# 或者这样看：
f = make_adder(1)
print(f(3))
```



### lambda 函数

节省代码

```python
def compose(f, g):
    def fun(x):
        return f(g(x))
    return fun
    # return lambda x : f(g(x))

# def square(x):
#     return x * x

# def add_one(x):
#     return x + 1

h = compose(lambda x : x * x, lambda x : x + 1)
# h = compose(square, add_one)
print(h(12))
```



0个骰子 对手80分 -> 80 20 2 得4分 75



4个骰子 80 + 28 
