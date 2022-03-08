import pandas as pd

def show_country_statistics(iso):
    url = f"https://api.worldbank.org/v2/en/country/{iso}?downloadformat=excel"
    data = pd.read_excel(url, 0, skiprows=[0,1,2])
    data = data.drop(['Country Name', 'Country Code'], axis=1)
    data = data.set_index('Indicator Name')
    data = data.loc[['Population, total', 'Urban population (% of total population)',\
                     'GDP (current US$)','GNI per capita (constant 2015 US$)',\
                     'Final consumption expenditure (constant 2015 US$)',\
                     'CPIA business regulatory environment rating (1=low to 6=high)',\
                     'Ease of doing business rank (1=most business-friendly regulations)'],\
                    ["2020"]]
    data = data.rename(index={'Population, total': 'Population (in Millions)',\
                             'Urban population (% of total population)': 'Urban population (in %)',\
                             'GDP (current US$)': 'GDP (in US$B)',\
                              'GNI per capita (constant 2015 US$)': 'GNI per capita (in US$)',\
                              'Final consumption expenditure (constant 2015 US$)': 'Final consumption expenditure (in US$B)',
                             })
    data = data.rename(columns={'2020': ''})
    data.index.name = "Country Feature"
    data.loc['Population (in Millions)',''] = '{0:.2f}'.format(data.loc['Population (in Millions)',''].astype(float)/1000000)
    data.loc['Urban population (in %)',''] = '{0:.2f}'.format(data.loc['Urban population (in %)',''])
    data.loc['GDP (in US$B)',''] = '{0:.2f}'.format(data.loc['GDP (in US$B)','']/1000000000)
    data.loc['GNI per capita (in US$)',''] = '{0:.2f}'.format(data.loc['GNI per capita (in US$)',''])
    data.loc['Final consumption expenditure (in US$B)',''] = '{0:.2f}'.format(data.loc['Final consumption expenditure (in US$B)','']/1000000000)
    data = data.dropna()
    data = data[data[''] != 'nan']
    return data
