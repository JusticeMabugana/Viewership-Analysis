# create bar graph to show the number of unique customers who watched content on each platform
plt.bar(df['Platform'].unique(), df['Platform'].value_counts())
plt.title('Number of Unique Customers by Platform')
plt.xlabel('Platform')
plt.ylabel('Number of Unique Customers')
plt.show()

# create pie chart showing the percentage of total time watched by each platform
plt.pie(df['Platform'].value_counts(), labels=df['Platform'].unique(), autopct='%1.1f%%')
plt.title('Percentage of Total Time Watched by Platform')
plt.show()
