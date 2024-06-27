import utils_else   

# 在用户选择退出系统时执行此程序
class Evaluate_system:
    
    def __init__(self,username):  
        self.username = username
        # 读取系统原有数据
        self.dict = utils_else.Data_process.read()
   
    def score(self):
        # 如果用户输入不符合要求，重新执行此模块
        while True:
            #让用户输入对本系统的评星
            self.score=int(input('''
                               评星系统
                    你可以选择输入数字 1/2/3/4/5.
                  数字越大说明你对本系统的评价越高\n'''))
            #判断输入是否符合要求
            if  self.score == 1 or  self.score == 2 or  self.score == 3 or  \
                self.score == 4 or  self.score == 5:
                break
            #如果不符合要求就让用户重新输入
            else:
                print('''你输入的不是1/2/3/4/5,请重新输入''')
        
    def comment(self): 
        #让用户输入对本系统的评价
        self.comment=input('''
                                评价系统
                      如果你有其他的建议，请在这里输入：
                      (如果你需要跳过，请直接按回车键)\n''')


    def submit(self):
         # 在程序中更改
        self.dict["score"]["count"] += 1
        self.dict["score"]["sum"] += self.score
        self.dict["score"]["average value"] = (self.dict["score"]["sum"])/(self.dict["score"]["count"])
        self.dict["comment"][self.username] = self.comment
        # 将数据保存在系统中
        utils_else.Data_process.write(self.dict)

    def show_stars(self):
        self.average_data = self.dict["score"]["average value"]
        #返回平均分的值
        print(f'该系统目前总分数为：{self.average_data}，感谢您的评价！')
    
    def show_comment(self):
        #返回用户的评价
        for i in self.dict["comment"]:
            print(i,":",self.dict["comment"][i])
    

if __name__ == '__main__':
    a = Evaluate_system("user3")
    a.score()
    a.comment()
    a.submit()
    a.show_stars()
    a.show_comment()




        



    









        


    