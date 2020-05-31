from FileLoader import FileLoader


def howManyMedals(df, name):
    # drop dublicates
    df = df[(df['Name'] == name)]
    df = df[['Year', 'Medal']]
    years = set(list(df['Year']))
    d = {}
    for year in years:
        gold = df[(df['Year'] == year) & (df['Medal'] == 'Gold')].shape[0]
        silver = df[(df['Year'] == year) & (df['Medal'] == 'Silver')].shape[0]
        bronze = df[(df['Year'] == year) & (df['Medal'] == 'Bronze')].shape[0]
        d[year] = {'G': gold, 'S': silver, 'B': bronze}
    return d


if __name__ == "__main__":
    df = FileLoader.load("../data/athlete_events.csv")
    dic = howManyMedals(df, 'Kjetil Andr Aamodt')
    print(dic)
