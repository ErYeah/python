# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 10:44:21 2018

@author: hp
"""

'''
Q：编写一个程序统计一个C源文件中注释所占的百分比。
假设filein.c的内容为：
void main()
{
FILE * in;
/*Open the file*/
if((in=fopen("in.txt","r"))==NULL)
{
printf("Can&rsquo;t open in.txt!");
return;
}
/*Close the file,
and return.*/
fclose(in);
}

【样例输出】
22%

【样例说明】
filein.c文件的总字符数为179，
注释中的字符数为41，
则注释所占百分比为22%。
'''
import re

r=open("filein.c","r")
lines=r.readlines()
content=''
for i in lines:
    content+=i
contentLen=len(content)

#——————————————正则————————————————
#第二个*代表0次到任意多次,
#.号代表任意字符（不包括换行符)
#?号代表检索模式为非贪婪模式
#()号：在输出结果中除掉/*...*/
pattern='/\*(.*?)\*/'#正则本体
#re.DOTALL:全文检索，多行检索
#贪婪模式(默认)：最长的匹配结果
#非贪婪模式：最短的匹配结果
result=re.findall(pattern,content,re.DOTALL)
#——————————————————————————————————

r.close()
resultLen=0
for i in result:
    resultLen+=len(i)

print('%.f%%'%((resultLen/contentLen)*100))


