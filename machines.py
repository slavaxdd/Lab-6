class Machine:
    def __init__(self, efficiency, cost, detail_price):
        self.efficiency = efficiency # производительность
        self.cost = cost # стоимость станка
        self.avg_det_price = detail_price # средняя цена детали
    
    def recoup_det_amount(self): # кол-во деталей для окупаемости станка
        if self.avg_det_price == 0:
            return float('inf')
        return self.cost/self.avg_det_price
    
    def recoup_time(self): # время окупаемости станка
        if self.efficiency == 0:
            return float('inf')
        return self.recoup_det_amount()/self.efficiency
    
    def __str__(self):
        return (f"(Machine: "
                f"efficiency={self.efficiency}, "
                f"cost={self.cost}, "
                f"detail_price={self.avg_det_price})")
    



class Milling_Machine(Machine):
    def __init__(self, efficiency, cost, detail_price, num_axes, cutter_size):
        super().__init__(efficiency, cost, detail_price)

        self.axes = num_axes # количество осей
        self.cutter = cutter_size

    def detail_complexity(self):
        return (self.axes / self.cutter) 

    def recoup_det_amount(self):
        if self.avg_det_price == 0:
            return float('inf') 
        return self.cost/self.avg_det_price 

    def recoup_time(self): 
        if self.efficiency == 0:
            return float('inf')
        return self.recoup_det_amount()/self.efficiency   
    
    def __str__(self):
        return (f"Milling Machine (efficiency={self.efficiency}, "
                f"cost={self.cost}, "
                f"detail_price={self.avg_det_price}, "
                f"num_axes={self.axes}, "
                f"cutter_size={self.cutter})")
    





class CNC_Machine(Machine):
    def __init__(self, efficiency, cost, detail_price, program_complexity):
        super().__init__(efficiency, cost, detail_price)

        self.complexity = program_complexity # сложность чпу
        
        self.cost_coefficient = {'low': 1.05, 'medium': 1.15, 'high': 1.25}.get(program_complexity, 1.15) # коэф стоимости станка + обслуживания в зависимости от сложности

    def recoup_det_amount(self):
        adjust_cost = self.cost * self.cost_coefficient

        if self.avg_det_price == 0:
            return float('inf') 
        return adjust_cost/self.avg_det_price 

    def recoup_time(self): 
        if self.efficiency == 0:
            return float('inf')
        return self.recoup_det_amount()/self.efficiency   
    
    def __str__(self):
        return (f"CNC Machine (efficiency={self.efficiency}, "
                f"price={self.cost}, "
                f"detail_price={self.avg_det_price}, "
                f"program_complexity={self.complexity})")


if __name__ == '__main__':
    CNC_mach = CNC_Machine(400, 4500000, 1000, 'medium')
    MILL_mach = Milling_Machine(200, 1500000, 700, 5, 50)
    print(CNC_mach)
    print(CNC_mach.recoup_det_amount())
    print(MILL_mach)
    print(MILL_mach.recoup_det_amount())