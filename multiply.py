"""multiply.py —— 输入两个数字，输出它们的积。"""

number1 = float(input("请输入第一个数字："))
number2 = float(input("请输入第二个数字："))

product = number1 * number2

# 结果是整数时不显示多余的 .0，例如 3 * 5 输出 15 而不是 15.0
if product == int(product):
    product = int(product)

print("它们的积是：", product)
print("计算完成")
