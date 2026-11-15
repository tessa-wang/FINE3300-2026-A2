# Inflation Calculator

import pandas as pd  
import matplotlib.pyplot as plt             

# Reading the file
file = open('STATIC_INFLATIONCALC.csv', 'r') # open file  
lines = file.readlines()                        
file.close() # close file                                   

#creating empty lists
dates = []          
cpis = []   
years = []         

# loop to add date CPI to the lists (skipping the first 9 lines)
for line in lines[9:]:                         
    cpi_date, cpi = line.split(',') #split line at comma into date and CPI
    cpi_date = cpi_date.strip(' \n"') # removes spaces, qoutes, and the new line from date
    cpi = cpi.strip(' \n"') # same for CPI^                             
    dates.append(cpi_date)  # add date to the list  
    cpis.append(float(cpi)) #add CPI to list as a float
    year = int(cpi_date[0:4]) # first 4 characters of the date = year
    month = int(cpi_date[5:7]) # characters 5-6 of the date = month
    years.append(year + (month - 1) / 12) # date as a number for the graph      

cpi_data = pd.DataFrame({'date': dates, 'CPI': cpis})   # put the date and CPI lists into pandas data frame

first_date = dates[0][0:7] # earliest date in the data
last_date = dates[-1][0:7] # latest date in the data

# Asking for price. Validates for 0 and letters 
while True:    # loop asking until the price is valid
    try:
        price = float(input("Enter the price: "))  # asking user for price
        if price != 0: # any number (except 0)
            break  # valid, so stop asking
    except: # if it wasn't a number, float fails
        pass
    print("Invalid price. Enter a number, e.g. 100 or 100.50")    

# Asking for the two dates
def get_date(date_specifier):
    while True:
        user_input_date = input("Enter the " + date_specifier + " date (YYYY-MM): ") # asking for dates
        if user_input_date + '-01' in dates:
            return user_input_date
        print("Invalid date. Use YYYY-MM between", first_date, "and", last_date)

# ask the user for the first and second date
cpi1_date = get_date("first")
cpi2_date = get_date("second")

# The Calculations
cpi1 = cpi_data[cpi_data['date'] == cpi1_date + '-01']['CPI'].iloc[0] # find the CPI for the first date
cpi2 = cpi_data[cpi_data['date'] == cpi2_date + '-01']['CPI'].iloc[0] # find the CPI for the second date


new_price = price * cpi2 / cpi1 # BoC's formula
price_percent_change = (new_price - price) / price * 100 # % change in price

year1 = int(cpi1_date[0:4]) # year from first date
month1 = int(cpi1_date[5:7]) # month from first date
year2 = int(cpi2_date[0:4]) # year from second date
month2 = int(cpi2_date[5:7]) # month from second date
num_years = (year2 - year1) + (month2 - month1) / 12 # years between the two dates

if num_years == 0:  # same month entered twice
    annual_rate = 0 # no time passed, so no inflation
else:
    annual_rate = ((cpi2 / cpi1) ** (1 / num_years) - 1) * 100 # compound annual inflation rate  

# If second date is earlier than first make the number positive
if num_years < 0:
    num_years = -num_years

# Printing results
print(50 * '-') 
print("${:,.2f} CAD in {} would cost ${:,.2f} CAD in {}".format(price, cpi1_date, new_price, cpi2_date)) # original price and what it would cost on the second date
print("Percent change: {:.2f}%".format(price_percent_change)) # change in price
print("Number of years: {:.2f}".format(num_years)) # years between two dates
print("Average annual rate of inflation: {:.2f}%".format(annual_rate)) # compound inflation rate per year
print("CPI for {}: {:.1f}".format(cpi1_date, cpi1)) # CPI on the first date
print("CPI for {}: {:.1f}".format(cpi2_date, cpi2)) # CPI on the second date
print("2002 CPI = 100.0") # base year note (on BoC's website)
print(50 * '-')

# Generating CPI graph
change = []     
                            
for i in range(12, len(cpis)): # start at month 12, since the first 12 months have nothing to compare to
    change.append((cpis[i] / cpis[i - 12] - 1) * 100)   # % change vs. 12 months earlier

base = [100] * len(years) # a list of 100s for the dotted base line (2002 CPI = 100)

# Drawing the graph
fig, ax1 = plt.subplots(figsize=(12, 6)) # create the figure and the left axis

ax1.plot(years, cpis, color='blue', label='CPI') # CPI line
ax1.plot(years, base, color='black', linestyle=':', label='Base level (2002 = 100)') # dotted base line
ax1.set_xlabel('Year')  # x-axis label
ax1.set_ylabel('CPI (2002 = 100)')  # left y-axis label
ax1.set_title('Canada CPI and Annual Percentage Change')  # title
ax1.set_ylim(0, 230) # making left axis a bit taller (to make sure lines stay below legend)
ax1.legend(loc='upper left')  # legend for the left axis

ax2 = ax1.twinx()  # second y-axis on the RIGHT (needed for the % change)
ax2.plot(years[12:], change, color='orange', label='Annual % change')   # skip the first 12 months to match the change list
ax2.set_ylabel('Annual % change') # right y-axis label
ax2.set_ylim(-20, 32) # making right axis a bit taller
ax2.legend(loc='upper center')  # legend for the right axis

fig.savefig('CPI_Graph.png')  #save the graph as a png file             
plt.show() # shows the graph                