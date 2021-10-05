import requests
import pandas as pd
from time import sleep
import argparse

parser = argparse.ArgumentParser(description = 'Species assessment automated search through IUCN Red List API')
parser.add_argument('-i', '--input', type = str, help = 'Path to the .csv file')
parser.add_argument('-r', '--region', type = str, help = 'Search species assessments within a specific region using the IUCN region identifier')
args = parser.parse_args()

dict = {'name_input':[], 'synonym':[], 'accepted_name':[],
'category':[], 'criteria':[], 'taxon_id':[], 'assessment_date':[]}

splist = pd.read_csv(args.input, header = None)
def getStatus(spname):
    url = 'https://apiv3.iucnredlist.org/api/v3/species/' + spname + '/region/' + args.region + '?token=' + splist[0][0]
    r = requests.get(url)
    while True:
        try:
            dict['category'].append(r.json()['result'][0]['category'])
            dict['name_input'].append(spname)
            dict['synonym'].append('FALSE')
            dict['accepted_name'].append(spname)
            dict['taxon_id'].append(r.json()['result'][0]['taxonid'])
            dict['assessment_date'].append(r.json()['result'][0]['assessment_date'])
            dict['criteria'].append(r.json()['result'][0]['criteria'])
            break
        except IndexError:
            dict['name_input'].append(r.json()['name'])
            dict['category'].append('NE')
            dict['synonym'].append('FALSE')
            dict['accepted_name'].append(r.json()['name'])
            dict['taxon_id'].append('NA')
            dict['assessment_date'].append('NA')
            dict['criteria'].append('NA')
            break
        except KeyError:
            url2 = 'https://apiv3.iucnredlist.org/api/v3/species/synonym/' + spname + '?token=' + splist[0][0]
            r2 = requests.get(url2)
            dict['name_input'].append(spname)
            dict['synonym'].append('TRUE')
            dict['accepted_name'].append(r2.json()['result'][0]['accepted_name'])
            url3 = 'https://apiv3.iucnredlist.org/api/v3/species/' + r2.json()['result'][0]['accepted_name'] + '?token=' + splist[0][0]
            r3 = requests.get(url3)
            dict['category'].append(r3.json()['result'][0]['category'])
            dict['taxon_id'].append(r3.json()['result'][0]['taxonid'])
            dict['assessment_date'].append(r3.json()['result'][0]['assessment_date'])
            dict['criteria'].append(r3.json()['result'][0]['criteria'])
            break

spp = splist.iloc[1: , :]
if __name__ == '__main__':
    for i in spp[0]:
        getStatus(i)
        print(f'Searching for {i} assessment in {args.region}...')
        if len(spp) > 50:
            sleep(5)
        else:
            sleep(2)
        while True:
            try:
                df = pd.DataFrame(dict)
                df.to_csv('status.csv')
                break
            except ValueError:
                print("ERROR: species names aren't correct")
                break
    print('done')
