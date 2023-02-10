import time

def display_time(func):
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