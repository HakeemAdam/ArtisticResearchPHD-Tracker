"""
Artistic Research PhD
==================================================================================

A Program to search Google for artistic research phd calls and save results to csv file.
----------------------------------------------------------------------------------------

"""


from googlesearch import search
import pandas as pd

query = "artistic research phd 2020"

my_results_list = []


def searchGoogle(query):
    """
    Using the google search API for search and pandas to save the output as csv
    :param query: search query
    :type query: str
    ...
    :return: none
    """
    for i in search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0, ):
        my_results_list.append(i)
        df = pd.DataFrame(my_results_list, columns=['link'])
        df.to_csv(r'/Users/hakeem/PycharmProjects/ArtisticResearchPhD/app/resources/results.csv', index=False, header=True)


if __name__ == '__main__':
    searchGoogle(query)
