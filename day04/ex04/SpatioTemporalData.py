from FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        df = self.df[self.df['City'] == location]
        df = df.drop_duplicates(['Year', 'City'])
        return list(df['Year'])

    def where(self, year):
        df = self.df[self.df['Year'] == year]
        df = df.drop_duplicates(['Year', 'City'])
        return list(df['City'])


if __name__ == "__main__":
    df = FileLoader.load("../data/athlete_events.csv")
    sp = SpatioTemporalData(df)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
