# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


def helper():
    df = pd.read_excel('C:/Users/Administrator/Desktop/statistic_v2_helper_view.xlsx')
    df = df[df['date'] >= '2020-02-01']
    print(df.head())
    plt.plot(df['date'], df['device_count'])
    plt.show()


if __name__ == '__main__':
    helper()
