import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class ActivityPlot():
    def __init__(self, csv):
        self.csv = csv
    def read_csv(self):
        df = pd.read_csv(self.csv)

        #Create array of the week day and also value change.
        week_day = (np.asarray(df['date']).reshape(2,4))
        value_change = (np.asarray(df['value_change']).reshape(2,4))

        for num in value_change:
            if num == 'NaN':
                num = 0
        print(value_change)

        result = df.pivot(columns='date', values='value_change') #creates new table derived from data frame(df)
        #print(result)
        return result

    def create_plot(self):
        result = self.read_csv()
        fig, ax = plt.subplots(figsize=(12,7))

        title = "Activity HeatMap"
        plt.title(title, fontsize=18)

        ttl = ax.title
        ttl.set_position([0.5,1.05])

        ax.set_xticks([])
        ax.set_yticks([])

        ax.axis('off')

        sns.heatmap(result, fmt='', cmap='RdYlGn', linewidths=0.3,ax=ax)
        plt.show()
        
    

test = ActivityPlot("example.csv")
test.create_plot()