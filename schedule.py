import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display


x=raw_input('Please Enter a Valid TV Channel Name:')
x=x.strip()
temp=x.split()

url="https://tvscheduleindia.com/channel/"

for channel_name_words in temp:
	url+=channel_name_words.lower()
	url+="-"

url=url[:-1]


page=requests.get(url)
soup=BeautifulSoup( page.content,'html.parser')
table_rows=soup.select('tr td')

programme_name=[]
start_time=[]
end_time=[]
short_desc=[]

for i in range(0,len(table_rows),4):
	programme_name.append(table_rows[i].get_text())
# print(programme_name)


for i in range(1,len(table_rows),4):
	start_time.append(table_rows[i].get_text().strip("PM").strip("AM"))
# print(start_time)

for i in range(2,len(table_rows),4):
	end_time.append(table_rows[i].get_text().strip("AM").strip("PM"))
# print(end_time)

for i in range(3,len(table_rows),4):
	short_desc.append(table_rows[i].select('span')[0].get_text())
# print(short_desc)

dict={
	"END-TIME":end_time,
	"NAME":programme_name,
	"START-TIME":start_time,
	"DESCRIPTION":short_desc
	}
df=pd.DataFrame(dict)

display(df)
