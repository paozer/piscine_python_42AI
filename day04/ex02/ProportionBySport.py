from FileLoader import FileLoader


def proportionBySport(df, year, sport, gender):
    population = df[(df['Year'] == year) & (df['Sex'] == gender)]
    population = population.drop_duplicates(['Name'])
    subset = population[population['Sport'] == sport]
    print(subset.shape[0] / population.shape[0])


if __name__ == "__main__":
    df = FileLoader.load("../data/athlete_events.csv")
    proportionBySport(df, 2004, 'Tennis', 'F')
