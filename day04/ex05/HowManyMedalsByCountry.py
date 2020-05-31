from FileLoader import FileLoader


def howManyMedalsByCountry(df, country):
    df = df[df['City'] == country]
    d = {}
    years = set(list(df['Year']))
    for year in years:
        gold = df[(df['Year'] == year) & (df['Medal'] == 'Gold')].shape[0]
        silver = df[(df['Year'] == year) & (df['Medal'] == 'Silver')].shape[0]
        bronze = df[(df['Year'] == year) & (df['Medal'] == 'Bronze')].shape[0]
        d[year] = {'G': gold, 'S': silver, 'B': bronze}
    return d


if __name__ == "__main__":
    df = FileLoader.load("../data/athlete_events.csv")
    d = howManyMedalsByCountry(df, 'Athina')
    print(d)
