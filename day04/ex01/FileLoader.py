import pandas as pd


class FileLoader:
    @staticmethod
    def load(path):
        df = pd.read_csv(path)
        print(f"{df.shape[0]} x {df.shape[1]}")
        return df

    @staticmethod
    def display(df, n=5):
        if (n > 0):
            print(df.head(n))
        else:
            print(df.tail(-n))
