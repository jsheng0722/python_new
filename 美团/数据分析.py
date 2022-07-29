import pandas as pd
import numpy as py
from matplotlib import pyplot as plt
import seaborn as sns
import re
import os


def xlsx_to_csv(filename):
    data_xlsx = pd.read_excel(filename + '.xlsx', index_col=0)
    data_xlsx.to_csv(filename + '.csv', encoding='utf-8')


if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    if not os.path.exists('医美.csv'):
        xlsx_to_csv('医美')
    df = pd.read_csv(r'医美.csv')
    print(df)
    df.info()
    data_cluster = df[['id', 'avgprice', 'latitude', 'longitude', 'avgscore', 'comments', 'historyCouponCount']]
    print(data_cluster)

    # 保存并覆盖
    data_cluster.to_csv(r'医美new.csv', index=False)
