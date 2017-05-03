# -*- coding: utf-8 -*-
# This program is coded by Watchara Deenuanpanao #
# email: watchara.deenuanpanao@gmail.com #
# The program is to scrape the restaurant information from https://offpeak.my/
# and insert into MySQL database.
# I use the Windows Task Scheduler to set time to run this python script.

import urllib2
import mysql.connector

wiki = "https://offpeak.my/"
page = urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)

W=[]
X=[]
Y=[]
Z=[]

cnx = mysql.connector.connect(user='python001', password='python001',
                              host='127.0.0.1',
                              database='classicmodels')

cursor = cnx.cursor()

i=0
for table_row in soup.find_all("div", class_="info"):

#    print 'i==> '+ str(i+1)
    col1 = table_row.find_all("div")
    temp_col1_0 = str(col1[0].string).strip()  #Restaurant Name
    temp_col1_1 = col1[1].find(string=True)    
    c = temp_col1_1.encode('ascii','ignore')   #Restaurant Location
    book_str = str(col1[3].find(text=True))    
    book_str1,book_str2 = book_str.split(' ')  #Book Number 
                
    sql = 'insert into classicmodels.restaurant(restaurant_name,restaurant_location,bookings,scrape_date) select "' + temp_col1_0 + '","' + c.strip() + '","' + book_str1 + '",current_timestamp()'

    cursor.execute(sql)
  
    cnx.commit()

        
    W.append(temp_col1_0)
    X.append(c.strip())
    Y.append(str(col1[2].find(text=True)))
    Z.append(book_str1)

    i=i+1

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(W,columns=['Restaurant_Name'])
df['Province']=X
df['Rating_Star']=Y
df['Booking_No']=Z
print df

cnx.close()
