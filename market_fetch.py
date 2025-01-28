import yfinance as yf
import schedule
import time

def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        return stock.fast_info['last_price']  # Faster than fetching history
    except Exception as e:
        print(f"Error fetching stock price for {ticker}: {e}")
        return None

def check_price_alert(ticker, threshold):
    current_price = get_stock_price(ticker)
    if current_price is not None:  # Ensure we got a valid price
        if current_price >= threshold:
            print(f"{ticker} has reached ${current_price}!")
        else:
            print(f"{ticker} is at ${current_price}, below the threshold.")
    else:
        print(f"Could not retrieve price for {ticker}.")

def monitor_stock():
    check_price_alert("AAPL", 150)  

schedule.every(1).minutes.do(monitor_stock)

print("Starting stock monitoring...")
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
        break
