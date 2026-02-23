# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 130
}

total_investment = 0

print("Stock Portfolio Tracker")

while True:
    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()
    
    if stock_name == "DONE":
        break
    
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"Added {stock_name} investment: {investment}")
    else:
        print("Stock not available.")

print("Total Investment Value:", total_investment)

# Optional: Save to file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value: " + str(total_investment))

print("Result saved to portfolio.txt")
