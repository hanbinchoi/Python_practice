price = float(input('Enter the actual product price: '))
sales = float(input('Enter the sales amount: '))

if price<sales:
    print('Total Profit = {}'.format(sales-price))

elif price>sales:
    print('Total Loss Amount = {}'.format(price-sales))

else:
    print('No Profit No Loss!!!')
