"""subtract.py —— 输入两个数字，输出它们的差。"""

number1 = float(input("请输入第一个数字："))
number2 = float(input("请输入第二个数字："))

difference = number1 - number2

# 结果是整数时不显示多余的 .0，例如 8 - 5 输出 3 而不是 3.0
if difference == int(difference):
    difference = int(difference)

print("它们的差是：", difference)
print("计算完成")
