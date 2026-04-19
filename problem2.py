def maxprofit(prices):
    min_price=float('inf')
    max_profit=0
    for price in prices:
        if price<min_price:
            min_price=price
        elif price-min_price>max_profit:
             max_profit=price-min_price
    return max_profit      
         

prices =[7,6,8,8,10,7,20,55,2,5] 
result = maxprofit(prices)
print('big profit', result)
