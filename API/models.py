

class WorkBook():
    def __init__(self, wb):
        self.wb = wb
    def get_names(self):
        ws = self.wb.active
        names_list = map(lambda x: x.value, ws["B"])
        response = list(names_list)
        return response[1:]
        
    def get_countries_data(self, name):
        index_Area = 0
        index_Demographics = 0
        index_Economy = 0
        ws_list = [self.wb["Area"], self.wb["Demographics"], self.wb["Economy"]]
        ws = self.wb.active
        names_list = [list(map(lambda x: x.value, ws_list[0]["B"])),list(map(lambda x: x.value, ws_list[1]["B"])),list(map(lambda x: x.value, ws_list[2]["B"]))]
        response = list(names_list)
        
        for x, n in enumerate(names_list[0]):
            if name == n:
                index_Area = x + 1
        for x, n in enumerate(names_list[1]):
            if name == n:
                index_Demographics = x + 1 
        for x, n in enumerate(names_list[2]):
            if name == n:
                index_Economy = x + 1          
        
        return {
            "Name" : ws_list[0][f"B{index_Area}"].value,
            "Area" : ws_list[0][f"C{index_Area}"].value,
            "Population" : ws_list[1][f"C{index_Demographics}"].value,
            "Median Age" : ws_list[1][f"E{index_Demographics}"].value,
            "Density" : ws_list[1][f"D{index_Demographics}"].value,
            "Urban Area" : ws_list[1][f"F{index_Demographics}"].value,
            "Area" : ws_list[2][f"C{index_Economy}"].value,
        }     

        
