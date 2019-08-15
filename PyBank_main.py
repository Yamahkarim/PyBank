#!/usr/bin/env python
# coding: utf-8

# # <h1> PyBank: Python Challenge

# In this assignment, I have been tasked with analyzing the budget data set and perfroming analysis to calculate the following:
#     
#     1.) The total number of months included in the dataset
# 
#     2.) The net total amount of "Profit/Losses" over the entire period
# 
#     3.) The average of the changes in "Profit/Losses" over the entire period
# 
#     4.) The greatest increase in profits (date and amount) over the entire period
# 
#     5.) The greatest decrease in losses (date and amount) over the entire period

# In[1]:


#dependencies
import os 
import csv 


# In[2]:


#import file
csvpath = "Data/budget_data.csv" 

#read csv
with open(csvpath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    # skip header
    csv_header = next(reader) 
    
    #create empty lists to store and iterate calculations 
    dates = []
    money = []
    change = [] 
    change_alt = [] 
    previous = 0 
    
    #Populate lists with corresponding information for date and profit with a for-loop 
    for row in reader:
        #populates dates 
        dates.append(row[0])
    
        #populate profit list
        money.append(row[1])
        
        #populate change in profit
        diff = int(row[1]) - int(previous)
        previous = row[1]
        change.append(diff)
    


# In[3]:


#Combine information from dates and money into paired tuples by using zip function
zipped = zip(dates, change)
zipped_lst = list(zipped)

change.remove(change[0])
zipped_lst.remove(zipped_lst[0])


# In[4]:


#perform calculations 
total_months = len(dates)
total_profit = sum(map(int, money))
average_change = sum(change) / len(change)
increase = max(change)
decrease = min(change)


# In[5]:


#Calculate Monthinly increase and decrease with an if, then for-loop 
month_dec = 0
month_inc = 0

for row in zipped_lst:
    if row[1] == increase:
        month_inc = row[0]
    if row[1] == decrease:
        month_dec = row[0]


# In[6]:


print(f'Financial Analysis')
print(f'___________________________')
print(f'Total Months: {total_months}')
print(f'Total Profit: ${total_profit}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {month_inc} ({increase})')
print(f'Greatest Decrease in Profits: {month_dec} ({decrease})')


# In[7]:


#write analysis to a .txt file 
with open('PyBank.txt', 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'___________________________', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total Profit: ${total_profit}', file=text_file)
    print(f'Average Change: ${average_change:.2f}', file=text_file)
    print(f'Greatest Increase in Profits: {month_inc} ({increase})', file=text_file)
    print(f'Greatest Decrease in Profits: {month_dec} ({decrease})', file=text_file)


# In[ ]:





# In[ ]:




