
# action1 求2+4+6+8+...+100的求和，用Python该如何写
numbers= range(2,101,2)
sum=0
for number in numbers:
    sum+=number
print("\n\n计算2+4+6+8+...+100。结果等于：%d"%sum)