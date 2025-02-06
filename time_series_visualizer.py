import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Filter out the top and bottom 2.5% of the data
low_percentile = df['page_views'].quantile(0.025)
high_percentile = df['page_views'].quantile(0.975)

df_cleaned = df[(df['page_views'] >= low_percentile) & (df['page_views'] <= high_percentile)]

def draw_line_plot():
    df_cleaned_copy = df_cleaned.copy()

    plt.figure(figsize=(12, 6))
    plt.plot(df_cleaned_copy.index, df_cleaned_copy['page_views'], color='blue', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    plt.tight_layout()
    plt.savefig('line_plot.png')
    plt.show()

def draw_bar_plot():
    df_cleaned_copy = df_cleaned.copy()

    # Add columns for year and month
    df_cleaned_copy['year'] = df_cleaned_copy.index.year
    df_cleaned_copy['month'] = df_cleaned_copy.index.month

    monthly_avg = df_cleaned_copy.groupby(['year', 'month']).mean()['page_views'].unstack()

    monthly_avg.plot(kind='bar', figsize=(12, 6), width=0.8)
    
    plt.title('Average Daily Page Views by Year and Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    plt.show()

def draw_box_plot():
    df_cleaned_copy = df_cleaned.copy()

    # Extract year and month for the box plots
    df_cleaned_copy['year'] = df_cleaned_copy.index.year
    df_cleaned_copy['month'] = df_cleaned_copy.index.month

    # Year-wise box plot (Trend)
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='year', y='page_views', data=df_cleaned_copy)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.tight_layout()
    plt.savefig('year_box_plot.png')
    plt.show()

    # Month-wise box plot (Seasonality)
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='month', y='page_views', data=df_cleaned_copy)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.tight_layout()
    plt.savefig('month_box_plot.png')
    plt.show()
