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


if __name__ == "__main__":
    df = FileLoader.load("file")
    print("entire df")
    print(df)
    print("first 2 rows")
    FileLoader.display(df, 2)
    print("last 2 row")
    FileLoader.display(df, -2)
