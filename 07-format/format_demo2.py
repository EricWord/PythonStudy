name = "zhangsan"
age = 18
# {}根据后面的内容对应填充
x = "大家好，我是{},我今年{}岁了".format(name, age)
print(x)
# {数字} 根据数字的顺序进行填充
x = "大家好，我是{1},我今年{0}岁了".format(age, name)
print(x)
# {变量名}
x = "大家好，我是{name},我今年{age}岁了,我来自{addr}".format(age=22, name="tom", addr="海南")
print(x)
# 混合使用 {数字} {变量} 不推荐这么混合使用
x = "大家好，我是{name},我今年{1}岁了,我来自{0}".format("越南", 39, name="lily")
print(x)
# 使用列表的自动拆包功能
d = ["zhangsan", 19, "上海", 180]
x = "大家好，我是{},我今年{}岁了,我来自{},身高{}cm".format(*d)
print(x)
# 字典
info = {"name": "lisi", "age": 24, "addr": "北京", "height": 180}
x = "大家好，我是{name},我今年{age}岁了,我来自{addr},身高{height}cm".format(**info)
print(x)
