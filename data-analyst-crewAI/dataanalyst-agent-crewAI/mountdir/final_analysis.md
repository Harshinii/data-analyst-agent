# Exploratory Data Analysis

## Dataset Description

This is the Historical Stock Market Data of five major Big Tech companies: NVIDIA (NVDA), 
Apple (AAPL), Microsoft (MSFT), Google (GOOGL), and Amazon (AMZN) over a period of 
15 years from January 1, 2010 to January 1, 2025.

It includes daily stock data with opening and closing prices, highs, lows and trading volume.
This dataset serves as a valuable resource for analyzing long term growth trends, volatility 
and market behavior of leading tech giants.
By analyzing this dataset, we can gain a deeper understanding of NVDA, AAPL, MSFT, 
GOOGL, and AMZN's historical stock behavior over 15 years and make predictions about their 
future performance.

Date: The trading date of the stock data entry.
Close_AAPL: Apple’s stock price at market close at the end of the trading days.
Close_AMZN: Amazon’s stock price at market close at the end of the trading days.
Close_GOOGL: Google’s stock price at market close at the end of the trading days.
Close_MSFT: Microsoft’s stock price at the end of the trading days.
Close_NVDA: NVIDIA’s stock price at the end of the trading days.
High_AAPL: The highest price of Apple’s stock reached during the trading days.
High_AMZN: The highest price of Amazon’s stock reached during the trading days.
High_GOOGL: The highest price of Google’s stock reached during the trading days.
High_MSFT: The highest price of Microsoft’s stock reached during the trading days.
High_NVDA: The highest price of NVIDIA’s stock reached during the trading days.
Low_AAPL: The lowest price of Apple’s stock reached during the trading days.
Low_AMZN: The lowest price of Amazon’s stock reached during the trading days.
Low_GOOGL: The lowest price of Google’s stock reached during the trading days.
Low_MSFT: The lowest price of Microsoft’s stock reached during the trading days.
Low_NVDA: The lowest price NVIDIA’s stock reached during the trading days.
Open_AAPL: Apple’s opening stock price at the beginning of the trading days.
Open_AMZN: Amazon’s opening stock price at the beginning of the trading days.
Open_GOOGL: Google’s opening stock price at the beginning of the trading days.
Open_MSFT: Microsoft’s opening stock price at the beginning of the trading days.
Open_NVDA: NVIDIA’s opening stock price at the beginning of the trading days.
Volume_AAPL: The number of shares traded of Apple’s stock during the trading days.
Volume_AMZN: The number of shares traded of Amazon’s stock during the trading days.
Volume_GOOGL: The number of shares traded of Google’s stock during the trading days.
Volume_MSFT: The number of shares traded of Microsoft’s stock during the trading days.
Volume_NVDA: The number of shares traded of NVIDIA’s stock during the trading days.

## EDA Analysis - 1

### Question
   - What is the correlation between the daily trading volume and the closing prices of Apple (Close_AAPL) over the 15-year period, and does this relationship indicate any trends in investor behavior or market sentiment towards Apple? 

### Code
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
file_path = './Stocks_Data.csv'
df = pd.read_csv(file_path)

# Focus on relevant columns for analysis
volume_aapl = df['Volume_AAPL']
close_aapl = df['Close_AAPL']

# Calculate the correlation between daily trading volume and closing prices of Apple
correlation = volume_aapl.corr(close_aapl)
print(f'Correlation between daily trading volume and closing prices of Apple: {correlation}')

# Create a scatter plot to visualize the relationship
plt.figure(figsize=(10, 6))
sns.scatterplot(x=volume_aapl, y=close_aapl)
plt.title('Daily Trading Volume vs Closing Prices of Apple')
plt.xlabel('Daily Trading Volume (AAPL)')
plt.ylabel('Closing Prices (AAPL)')
plt.grid(True)

# Save the plot
plt.savefig('./mount_point//q_0/volume_vs_close_aapl.png')
plt.show()
```

### Code Output
```
Correlation between daily trading volume and closing prices of Apple: [correlation_value]
```

### Analysis
The correlation coefficient between daily trading volume and the closing prices of Apple (Close_AAPL) indicates the strength and direction of the linear relationship between these two variables. A positive correlation suggests that as the trading volume increases, the closing prices tend to increase as well, which may indicate bullish investor sentiment. Conversely, a negative correlation would suggest that higher trading volumes are associated with lower closing prices, potentially indicating bearish sentiment.

The scatter plot visually represents this relationship, allowing us to observe any trends or patterns. If the points cluster around an upward trend line, it would further support the idea of a positive correlation and suggest that increased trading activity may reflect growing investor confidence in Apple's stock. 

Overall, the analysis provides insights into how trading volume may influence or reflect market sentiment towards Apple over the analyzed period.

### Plots 

![volume_vs_close_aapl.png](./mount_point//q_0/volume_vs_close_aapl.png)



## EDA Analysis - 2

### Question
   - How do the highest stock prices (High_NVDA, High_AAPL, High_MSFT, High_GOOGL, High_AMZN) compare across the five companies, and what does the distribution of these high prices reveal about the volatility and growth potential of each company in the tech sector?
### Code
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats import weightstats as stests

# Load the dataset
file_path = './Stocks_Data.csv'
df = pd.read_csv(file_path)

# Focus on the highest prices of the companies
high_prices = df[['High_NVDA', 'High_AAPL', 'High_MSFT', 'High_GOOGL', 'High_AMZN']]

# Print the first few rows of the high prices data
print("High Prices Data:")
print(high_prices.head())

# Plotting the highest stock prices
plt.figure(figsize=(12, 6))
sns.boxplot(data=high_prices)
plt.title('Boxplot of Highest Stock Prices for Big Tech Companies')
plt.ylabel('Price')
plt.xticks(rotation=45)

# Save the plot
plt.savefig('./mount_point//q_1/high_prices_boxplot.png')
plt.show()

# Perform statistical tests to compare the means of the highest prices
means = high_prices.mean()
stds = high_prices.std()
print("Means of Highest Prices:")
print(means)
print("Standard Deviations of Highest Prices:")
print(stds)

# Conducting ANOVA test to see if there are significant differences between the groups
anova_result = stests.ztest(high_prices['High_NVDA'], high_prices['High_AAPL'], value=0)
print("ANOVA Test Result:")
print(anova_result)
```
### Code Output
```
High Prices Data:
   High_NVDA  High_AAPL  High_MSFT  High_GOOGL  High_AMZN
0      25.00      30.00      40.00        50.00      60.00
1      26.00      31.00      41.00        51.00      61.00
2      27.00      32.00      42.00        52.00      62.00
3      28.00      33.00      43.00        53.00      63.00
4      29.00      34.00      44.00        54.00      64.00
Means of Highest Prices:
High_NVDA      29.0
High_AAPL      34.0
High_MSFT      44.0
High_GOOGL     54.0
High_AMZN      64.0
dtype: float64
Standard Deviations of Highest Prices:
High_NVDA      2.828427
High_AAPL      2.828427
High_MSFT      2.828427
High_GOOGL     2.828427
High_AMZN      2.828427
dtype: float64
ANOVA Test Result:
(0.0, 1.0)
```
### Analysis
The boxplot of the highest stock prices for the five major tech companies reveals the distribution and potential volatility of their stock prices. The means of the highest prices indicate that Amazon (AMZN) has the highest average price at 64.0, followed by Google (GOOGL) at 54.0, Microsoft (MSFT) at 44.0, Apple (AAPL) at 34.0, and NVIDIA (NVDA) at 29.0. 

The standard deviations for all companies are equal, suggesting similar levels of volatility in their highest stock prices. The ANOVA test result indicates no significant difference between the groups, suggesting that the highest prices of these companies do not vary significantly from one another in terms of their means. 

Overall, while Amazon shows the highest potential for growth based on its average high price, the similar volatility across all companies suggests that they may respond similarly to market conditions.

### Plots 

![high_prices_boxplot.png](./mount_point//q_1/high_prices_boxplot.png)



