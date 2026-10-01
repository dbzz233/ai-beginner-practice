"""add.py —— 输入两个数字，输出它们的和。"""

number1 = float(input("请输入第一个数字："))
number2 = float(input("请输入第二个数字："))

total = number1 + number2

# 结果是整数时不显示多余的 .0，例如 3 + 5 输出 8 而不是 8.0
if total == int(total):
    total = int(total)

print("它们的和是：", total)
print("计算完成")
