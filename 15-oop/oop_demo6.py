class House(object):
    def __init__(self, house_type, total_area, fru_list=None):
        if fru_list is None:
            fru_list = []
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list

    def add_fru(self, x):
        if self.free_area < x.area:
            print("剩余面积不足，放不进去了")
        else:
            # print("需要将家具添加到房子里")
            self.fru_list.append(x.name)
            self.free_area -= x.area

    def __str__(self):
        return "户型={},总面积={},剩余面积={},家具列表={}".format(self.house_type, self.total_area, self.free_area, self.fru_list)


house1 = House("两室一厅", 20)


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


bed = Furniture("席梦思", 4)
chest = Furniture("衣柜", 2)
table = Furniture("餐桌", 1.5)
sofa = Furniture("沙发", 10)

# 把家具添加到房间里
house1.add_fru(sofa)
house1.add_fru(bed)
house1.add_fru(chest)
house1.add_fru(table)

print(house1)  # 打印一个对象的时候，会调用这个对象的__repr__或者__str__方法，获取它们的返回值
