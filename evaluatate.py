import json
import utils_else   #这是独立的一个json文件，用来存储用户评分和评价

# 在用户选择退出系统时执行此程序
class Evaluate_system:
    
    def __init__(self,username):  
        self.username = username
   
    def score(self):
        # 如果用户输入不符合要求，重新执行此模块
        while True:
            #让用户输入对本系统的评星
            self.score=input('''   评星系统
                    你可以选择输入数字 1/2/3/4/5.
                  数字越大说明你对本系统的评价越高''')
            #判断输入是否符合要求
            if  self.score == 1 or  self.score == 2 or  self.score == 3 or  \
                self.score == 4 or  self.score == 5:
                break
            #如果不符合要求就让用户重新输入
            else:
                print('''你输入的不是1/2/3/4/5(纯数字),
                    请重新输入''')
        
    def comment(self): 
        #让用户输入对本系统的评价
        self.comment=input('''         评价系统
                      如果你有其他的建议，请在这里输入：
                      (如果你需要跳过，请输入"#")''')
        # 判断用户是否需要跳过。如果跳过将评价改为空字符串
        if self.comment == "#":
                self.comment == ""
                print("已成功跳过评价")

    def submit(self,username):
         # 读取系统原有数据
        self.dict = utils_else.Data_process.read()
         # 在程序中更改
        self.dict["score"]["count"] += 1
        self.dict["score"]["sum"] += self.score
        self.dict["score"]["average value"] = (self.dict["score"]["sum"])/(self.dict["score"]["count"])
        self.dict["comment"][username] = self.comment
        # 将数据保存在系统中
        utils_else.Data_process.write(self.dict)

    def show_stars(self):
        self.average_data = self.dict["score"]["average value"]
        #返回平均分的值
        return self.average_data
    




        



    









        


    