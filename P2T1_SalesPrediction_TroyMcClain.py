#program used to calculate total profit from sales
#April 9-2019
#CTI-110-P2T1-Sales Prediction
#TroyMcClain

TotalSales = float(input("Enter projected sales: "))

# calculate the profit as 23 percent of total sales.

profit = TotalSales * 0.23

#Display the profit.

print("The profit is $", format(profit, ",.2f"))
