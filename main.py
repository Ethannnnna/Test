# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

#可以输出一个数字
print(520)
print(98.5)
#输出数字不需要添加单引号或者双引号

#可以输出字符串
print('Hello world')
print('It will be nice day!')
print("That is good day today")
#直接照搬输出字符串是需要双引号或者单引号


#还可以输出含有运算符的表达式，但是会计算表达式的结果
print(3+1)
#表达式和数字都不需要在括号内添加‘’和“”
#如果括号内有数字和运算符一起，那么最终输出的将是数字运算的结果


#将数据输出到文件当中，注意点，1.所指定的盘符存在。2.使用file=fp这种来使得输出的内容存在输入的文件中
fp=open('D:/text.txt','a+')#’a+‘ 这里指的意思是在当前路径中，如果有该文件，则在该路径中的文件中继续追加；如果没有该文件，就该盘下添加文件并且执行下一行的命令
print("hello world",file=fp)
fp.close()



#不进行换行输出
print('hello','world','python')
