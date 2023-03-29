#转义字符
print('Hello \nworld')  #加上转义字符的首字符   ----n =newline 表示换行
print('Hello\tworld')  #表示两段字符串需要间隔一个空间或者空格（实际上是一个四组空格的位置）
print('Hello\rworld') #原先输出hello字符串，但是由于\r后面输出world，因此world返回到原先hello的位置上代替了hello
print("Hello\bworld") #终端输出 Hellworld  原因就是\b就是退一个格，将o退除了


#\n就是一个将之后的东西进行换行的操作（换行）
#\t就是一个空四个制表符的位置（水平制表符）
#\r 就是之后的字符串将占据\r前面的位置（回的）
#\b就是将前一个格间的消除（退格）

print('http:\\\\www.baidu.com')
print()