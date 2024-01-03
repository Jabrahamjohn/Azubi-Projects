# tip calculator for hotel Asanka
#!/usr/bin/python3
Charge_of_food = float(input("please input the amount charged for food\n :$"))
Tip = Charge_of_food * (18/100)
Sales_tax = Charge_of_food * (7/100)
Grand_total = Charge_of_food + Tip + Sales_tax
print("Your bill is as follows:\n")
print("Tip = ",Tip)
print(f"\nSales tax = ${Sales_tax: .2f}")
print("\nYour Grand Total is:\n", Grand_total)
