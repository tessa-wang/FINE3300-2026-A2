# Inflation Calculator

import pandas as pd              

# Reading the file
file = open('STATIC_INFLATIONCALC.csv', 'r')    
lines = file.readlines()                        
file.close()                                    

#creating empty lists
dates = []          
cpis = []   
years = []         

# loop for var line to add dates and CPI into the lists
for line in lines[9:]:                         
    cpi_date, cpi = line.split(',')
    cpi_date = cpi_date.strip(' \n"')
    cpi = cpi.strip(' \n"')                                         
    dates.append(cpi_date)                  
    cpis.append(float(cpi)) 
    year = int(cpi_date[0:4])               # first 4 characters of the date = year
    month = int(cpi_date[5:7])              # characters 5-6 of the date = month
    years.append(year + (month - 1) / 12)             

cpi_data = pd.DataFrame({'date': dates, 'CPI': cpis})   

first_date = dates[0][0:7]
last_date = dates[-1][0:7]

# ask price 

price = float(input("Enter the price: "))
    
# Asking for the two dates
def get_date(date_speficier):
    while True:
        user_input_date = input("Enter the " + date_speficier + " date (YYYY-MM): ")
        if user_input_date + '-01' in dates:
            return user_input_date
        print("Invalid date. Use YYYY-MM between", first_date, "and", last_date)

cpi1_date = get_date("first")
cpi2_date = get_date("second")

# The Calculations
cpi1 = cpi_data[cpi_data['date'] == cpi1_date + '-01']['CPI'].iloc[0] #links date to date and CPI rate
cpi2 = cpi_data[cpi_data['date'] == cpi2_date + '-01']['CPI'].iloc[0]

new_price = price * cpi2 / cpi1
price_percent_change = (new_price - price) / price * 100

year1 = int(cpi1_date[0:4])
month1 = int(cpi1_date[5:7])
year2 = int(cpi2_date[0:4])
month2 = int(cpi2_date[5:7])
num_years = (year2 - year1) + (month2 - month1) / 12

if num_years == 0:  
    annual_rate = 0
else:
    annual_rate = ((cpi2 / cpi1) ** (1 / num_years) - 1) * 100   

if num_years < 0:
    num_years = -num_years

# Printing results
print(50 * '-')
print("${:,.2f} CAD in {} would cost ${:,.2f} CAD in {}".format(price, cpi1_date, new_price, cpi2_date))
print("Percent change: {:.2f}%".format(price_percent_change))
print("Number of years: {:.2f}".format(num_years))
print("Average annual rate of inflation: {:.2f}%".format(annual_rate))
print("CPI for {}: {:.1f}".format(cpi1_date, cpi1))
print("CPI for {}: {:.1f}".format(cpi2_date, cpi2))
print("2002 CPI = 100.0")
print(50 * '-')

# Generating CPI graph
change = []     
                            
for i in range(12, len(cpis)):                   # start at month 12, since the first 12 months have nothing to compare to
    change.append((cpis[i] / cpis[i - 12] - 1) * 100)   # % change vs. 12 months earlier

base = [100] * len(years)                       # a list of 100s for the dotted base line (2002 CPI = 100)

# Drawing the graph
import matplotlib.pyplot as plt 
fig, ax1 = plt.subplots(figsize=(12, 6))        # create the figure and the left axis

ax1.plot(years, cpis, color='blue', label='CPI')                                # CPI line
ax1.plot(years, base, color='black', linestyle=':', label='Base level (2002 = 100)')   # dotted base line
ax1.set_xlabel('Year')                          # x-axis label
ax1.set_ylabel('CPI (2002 = 100)')              # left y-axis label
ax1.set_title('Canada CPI and Annual Percentage Change')   # title
ax1.legend(loc='upper left')                    # legend for the left axis

ax2 = ax1.twinx()                               # second y-axis on the RIGHT (needed for the % change)
ax2.plot(years[12:], change, color='orange', label='Annual % change')   # skip the first 12 months to match the change list
ax2.set_ylabel('Annual % change')               # right y-axis label
ax2.legend(loc='upper center')                  # legend for the right axis

fig.savefig('CPI_Graph.png')               
plt.show()                