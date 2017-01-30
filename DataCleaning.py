#pass the dataframe having all the movies from csv file
def getEnglishMovies(df,savefile):
    return df.loc[df['Language'].str.contains('English')]

def cleanConsensus(df,savefile):
    
    df_english_consensus = df.loc[df['tomatoConsensus'] != 'N/A'] 
    df_english_consensus = df_english_consensus.loc[pd.notnull(df_english_consensus['tomatoConsensus'])]
    if (savefile):
        df_english_consensus.to_csv('../Data/EnglishMoviesWithTomato.csv',encoding = 'utf-8',errors='replace')
    return df_english_consensus
def calculateConsensusPolarity(df,savefile):
    Consensus_List = df['tomatoConsensus'].tolist()
    polarity_value = np.empty(len(Consensus_List),dtype=float)
    for i in range(0,len(Consensus_List)):
        sentiment_val = TextBlob(Consensus_List[i]).sentiment
        polarity_value[i] = sentiment_val.polarity
        #print Consensus_List[i] , sentiment_val.polarity
    df['sentiment_polarity'] = pd.Series(polarity_value, index=df.index)
    return df
def getNonNullBoxOfficeRevenue(df):
    return df.loc[pd.notnull(df['BoxOffice'])]