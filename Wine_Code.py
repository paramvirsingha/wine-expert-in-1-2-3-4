import pandas as pd
import matplotlib.pyplot as plt
wine_reviews=pd.read_csv('wine.csv', index_col=0)
fig = plt.figure(figsize=(12,10))
fig.suptitle('Wine Expert in 1-2-3-4', fontsize=20)
plt.subplots_adjust(left=None, bottom=.8, right=None, top=2, wspace=.75, hspace=.7)
ax1 = fig.add_subplot(2, 2, 1)
wine_reviews.groupby("country").points.mean().sort_values(ascending=False)[:5].plot.pie()
plt.title('Highest Rated Wines') 
plt.ylabel('')
ax2 = fig.add_subplot(2, 2, 2)
wine_reviews['points'].plot.hist()
plt.title('Distributions of Points') 
plt.xlabel('Points')
ax3 = fig.add_subplot(2, 2, 3)
wine_reviews.groupby("country").price.mean().sort_values(ascending=False)[1:12].plot()
plt.title('Decending by Mean Price') 
plt.ylabel('Avg Price in Dollars')
plt.xlabel('Countries')
ax4 = fig.add_subplot(2, 2, 4)
wine_reviews.groupby("country").price.mean().sort_values(ascending=True)[:5].plot.barh()
plt.title('Ascending By Mean Price') 
plt.xlabel('Avg Price in Dollars')
plt.ylabel('Countries')
fig.tight_layout()
fig.subplots_adjust(top=0.88)
plt.savefig('My_Sample_Plot', format='png', bbox_inches='tight')
