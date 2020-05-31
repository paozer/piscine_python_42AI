import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
from FileLoader import FileLoader


class MyPlotLib:
    @staticmethod
    def histogram(data, features):
        df[features].hist()
        plt.show()

    @staticmethod
    def density(data, features):
        sns.distplot(df[features])
        plt.show()

    @staticmethod
    def pair_plot(data, features):
        pass

    @staticmethod
    def box_plot(data, features):
        pass


if __name__ == "__main__":
    df = FileLoader.load("../data/athlete_events.csv")
    MyPlotLib.histogram(df.drop_duplicates(['ID']), ['Height', 'Weight'])
    MyPlotLib.density(df.drop_duplicates(['ID']), ['Height', 'Weight'])
