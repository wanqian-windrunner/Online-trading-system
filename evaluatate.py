import json
import utils_else

# 在用户选择退出系统时执行此程序
class Evaluate_system:
    def __init__(self,username):  
        self.username = username
   
    def score(self):
        #让用户输入对本系统的评星
        self.score=input('''   评星系统
                    你可以选择输入数字 1/2/3/4/5.
                  数字越大说明你对本系统的评价越高''')
        #判断输入是否符合要求
        if  self.score == 1 or  self.score == 2 or  self.score == 3 or  \
            self.score == 4 or  self.score == 5:
            pass
        #如果不符合要求就让用户重新输入
        else:
            print('''你输入的不是1/2/3/4/5(纯数字),
                  请重新输入''')
            return score()
        
    def comment(self): 
        #让用户输入对本系统的评价
        self.comment=input('''         评价系统
                      如果你有其他的建议，请在这里输入：
                      (如果你需要跳过，请输入"#")''')
        # 判断用户是否需要跳过。如果跳过将评价改为空字符串
        if self.comment == "#" 
                self.comment == ""
                print("已成功跳过评价")
    def submmit(self,username):
         # 读取系统原有数据
        dict = utils_else.Data_porcess.read()
         # 在程序中更改
        dict["score"]["count"] += 1
        dict["score"]["sum"] += self.score
        dict["score"]["average value"] = (dict["score"]["sum"] += \
                                          self.score)/(dict["score"]["count"])
        dict["comment"][username] = self.comment
        # 将数据保存在系统中
        utils_else.Data_porcess.write(dict)
        # 程序结束
    




        



    









        


    