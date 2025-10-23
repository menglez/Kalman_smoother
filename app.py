
import download_stock
import kalman_func



stock_input = input('ENTER stock TICKER and press ENTER >> ')
stock = stock_input.upper()

df = download_stock.download(stock)
#print(df)


#Apply custom Kalman filter
kf_ts    = kalman_func.kalman_filter( df[stock].values )
df['kf']           =  kf_ts
