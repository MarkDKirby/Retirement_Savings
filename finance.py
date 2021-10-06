import numpy as np
import matplotlib.pyplot as plt

'''Creates a class for retirement financial vehicles. These include the 401k and the IRA. It takes into
account the fluctuating inflation and interest rates as well as the fluctuating rates of raises you might get.
The retirement program prints the results, but this class contains methods to plot the data in different ways.
It also takes into account the age of the person as those who are after 50 get to contribute a much higher 
maximum than those who are under 50.'''


class Finance:
    def __init__(self, name, salary, savings_percent, savings_amount,
                 interest_rate, tax_rate, inflation_rate, year, total, raise_rate, age):
        
        self.name = name
        self.salary = salary
        self.savings_percent = savings_percent
        self.savings_amount = savings_amount
        self.year = year
        self.interest_rate = interest_rate 
        self.tax_rate = tax_rate    
        self.inflation_rate = inflation_rate
        self.total = total
        self.raise_rate = []
        self.interest = []
        self.inf = []
        self.years_list = []
        self.age = age

    # This code produces the same interest and inflation rate for both IRA and 401k 
    #because people are investing in both their IRA and 401k in the same years
    #It is assumed that they are making the same returns and that the inflation
    #will be the same.      
    def rates(self,years):
        self.interest = []
        self.years_list = []
        self.inf = []
        for i in range(0,years):
            self.interest.append(np.random.normal(0.1,0.1)) #fluctuate interest normally around 10% with a 10% Standard deviation.
            self.inf.append(np.random.normal(0.03,0.005)) #fluctuate inflation normally around 3% with only 0.5% standard deviation.
            self.years_list.append(i) #keep list of years to plot
            self.raise_rate.append(np.random.normal(0.04,0.01))
         
    
    #401k calculations 
    def four01k(self,salary,savings_percent,years,total,age):
        total_list = []
        savings_amount = 0
        savings_max = 19000
        discount_list = []
        discount = 0
        savings_max_inflated = 0
        
        for i in range(0,years):
            savings_amount = salary * savings_percent
            if age+i == 50:
                savings_max = savings_max + 6500
                
            #to index the maximum savings allowed to inflation
            savings_max_inflated = savings_max * (1+self.inf[i])
            if savings_max_inflated >= (savings_max+500):
                savings_max = savings_max + 500
            
            #you cannot save more than the max
            if savings_amount > savings_max:
                savings_amount = savings_max
                
            salary = salary * (1 + self.raise_rate[i])
            total = (savings_amount + total) * (1+self.interest[i])
            total_list.append(total)
            discount = total
                
            #discount for inflation
            for j in range(0,len(total_list)):
                discount = discount/(self.inf[j]+1)
            discount_list.append(discount)   

        return total_list, discount_list
    
    #IRA Calculations
    def IRA(self,savings_amount,total,years,age):
        total_list = []
        a = savings_amount
        T = total
        discount_list=[]
        
        #This will calculate the amount one can save in the IRA given the parameters
        for i in range(0,years):
            T = (T + savings_amount) * (1+ self.interest[i])
            a = a*(1+self.inf[i])
            
            #To contribute an extra $1000 it he/she is over 50
            if age == 50:
                savings_amount = savings_amount + 1000
                
            #To index the contributions to inflation
            if a >= (savings_amount+500):
                savings_amount = savings_amount + 500
            total_list.append(T)
            discount = T
            
            for j in range(0,len(total_list)):
                discount = discount/(self.inf[j]+1)
            discount_list.append(discount)
            age += 1 

  
        return total_list, discount_list
    
    # Four different plot methods
    # Plot one line for savings IRA / 401k
    def plot_of_savings(self,plot_data,title):
        plt.plot(self.years_list,plot_data)
        plt.xlabel("Years")
        plt.ylabel("Amount")
        plt.title(("Potential Growth of", title, " over Years"))
        plt.show()
        
    # plot many lines for savings IRA / 401k  
    def plot_more_runs(self,plotdata,iters,title):
        for i in range(0,iters):
            plt.plot(self.years_list,plotdata[i])
        plt.xlabel("Years")
        plt.ylabel("Amount")
        plt.title(("Potential Growth of", title, "over Years"))
        plt.show()
    
    #Plot with shading between maximum and minimum line    
    def plot_more_runs_with_range(self, plotdata, max_list, min_list, iters, title):
        for i in range(0,iters):
            plt.plot(self.years_list,plotdata[i])
        plt.fill_between(self.years_list,min_list,max_list, alpha = 0.3)
        plt.xlabel("Years")
        plt.ylabel("Amount")
        plt.title(("Potential Growth of", title, "over Years"))
        plt.show()
        
    #Plot with shading between maximum and minimum like with the average line  
    def plot_avg_max_min(self, max_list,min_list, avg_list, title):
        plt.plot(self.years_list,max_list)
        plt.plot(self.years_list,min_list)
        plt.plot(self.years_list,avg_list)
        plt.fill_between(self.years_list,max_list, min_list, alpha =0.3)
        plt.xlabel("Years")
        plt.ylabel("Amount")
        plt.title(("Potential Growth of", title, "over Years"))
        plt.show()
        
