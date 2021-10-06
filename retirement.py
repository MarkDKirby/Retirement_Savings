import finance
import numpy as np

'''It can be difficult to plan for retirement. This program helps to make it easier by taking variable amounts
and converting them into projections about how much money you will have as a result of that savings plan. This
program then plots the results. We make use the Finance class from the finance program in Object Oriented Python
to accomplish this'''

years = 30
IRA_Start = 0
Four01k_Start = 0
Salary = 90000
IRA_Contribution = 5000
raise_rate = 0.03
contribution401k = 0.20
iters = 20
age = 25
s = finance.Finance(0,0,0,0,0,0,0,0,0,0,0)

# Get rates for inflation, interest and raises for every year until retirement
finance.Finance.rates(s,years)  

#run IRA and 401k     
Ira_Total, Disc_IRA_Total= finance.Finance.IRA(s,IRA_Contribution,IRA_Start,years,age)
Four01k_Total, Disc_Four01k_Total = finance.Finance.four01k(s,Salary,contribution401k,years,Four01k_Start,age)

print()
print("TOTALS:")
print('IRA = $','{:7,.2f}'.format(Ira_Total[-1]))
print('401k = $','{:7,.2f}'.format(Four01k_Total[-1]))
print('Total = $','{:7,.2f}'.format(Four01k_Total[-1] + Ira_Total[-1]))
print()
print("DISCOUNTED FOR INFLATION:")
print('IRA = $','{:7,.2f}'.format(Disc_IRA_Total[-1]))
print('401k = $','{:7,.2f}'.format(Disc_Four01k_Total[-1]))
print('TOTAL = $','{:7,.2f}'.format(Disc_Four01k_Total[-1] + Disc_IRA_Total[-1]))
print()

finance.Finance.plot_of_savings(s,Ira_Total,"IRA")
finance.Finance.plot_of_savings(s,Disc_IRA_Total,"Discounted IRA")

# Monte-Carlo Simulation - creates lists for returns in each year until retirement.
plot_IRA_list = []
plot_401k_list = []

for j in range(0, iters):
    finance.Finance.rates(s,years)
    plot_IRA, decreased_IRA = finance.Finance.IRA(s,IRA_Contribution,IRA_Start,years,age)
    plot_401k, decreased_401k = finance.Finance.four01k(s,Salary,contribution401k,years,Four01k_Start,age)
    plot_IRA_list.append(plot_IRA)
    plot_401k_list.append(plot_401k)
    
#plot the monte-carlo runs
finance.Finance.plot_more_runs(s,plot_IRA_list,iters, "IRA")
finance.Finance.plot_of_savings(s,Four01k_Total,"401k")
finance.Finance.plot_more_runs(s,plot_401k_list,iters,"401k")
finance.Finance.plot_of_savings(s,Disc_Four01k_Total, "Discounted 401k")

# To get the maximum, minimum and average values for each year in the
# years of savings for retirement.
year_max_list = []
year_min_list = []
year_max_list1 = []
year_min_list1 = []
year_avg_list = []
year_avg_list1 = []
for j in range(0, years):
    year_list = []
    year_list1 = []
    for i in range(0,iters):
        year_list.append(plot_IRA_list[i][j])
        year_list1.append(plot_401k_list[i][j])
    year_max_list.append(max(year_list))
    year_min_list.append(min(year_list))
    year_avg_list.append(np.mean(year_list))
    year_max_list1.append(max(year_list1))
    year_min_list1.append(min(year_list1))
    year_avg_list1.append(np.mean(year_list1))

# Plot minimum, maximum and average
finance.Finance.plot_more_runs_with_range(s,plot_IRA_list,year_max_list, year_min_list, iters,"IRA")
finance.Finance.plot_more_runs_with_range(s, plot_401k_list, year_max_list1, year_min_list1, iters,"401k")
finance.Finance.plot_avg_max_min(s, year_max_list, year_min_list, year_avg_list, "IRA")
finance.Finance.plot_avg_max_min(s, year_max_list1, year_min_list1, year_avg_list1, "401k")

