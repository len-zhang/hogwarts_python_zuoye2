# -*- coding:utf-8 -*-

class Bicycle:
    # def __init__(self, km):
    #     self.km = km

    def run(self, km):
        print(f"用脚骑行里程为{km}公里")


class EBicycle(Bicycle):
    def __init__(self, quantity):
        # super().__init__(km)
        self.quantity = quantity

    def fill_charge(self, vol):
        self.quantity = self.quantity + vol
        print(f"充了{vol}度电，当前总电量为{self.quantity}度电")

    def e_run(self, km):
        limitkm_by_e = self.quantity * 10
        if limitkm_by_e >= km:
            print(f"我使用电力骑行了{limitkm_by_e}公里")
        else:
            print(f"我使用电力骑行了{limitkm_by_e}公里")
            super().run(km - limitkm_by_e)


if __name__ == "__main__":
    go = EBicycle(50)
    go.fill_charge(20)
    go.e_run(1000)
