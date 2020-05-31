from FileLoader import FileLoader


def youngestFellah(df, year):
    df = df[df['Year'] == year]
    m = df[df['Sex'] == 'M'].nsmallest(1, 'Age')
    f = df[df['Sex'] == 'F'].nsmallest(1, 'Age')
    return {'m': m.iloc[0]['Age'], 'f': f.iloc[0]['Age']}


if __name__ == "__main__":
    df = FileLoader.load("../data/athlete_events.csv")
    FileLoader.display(df)
    dic = youngestFellah(df, 2004)
    print(dic)
