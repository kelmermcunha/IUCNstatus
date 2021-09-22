import requests
import pandas as pd
from time import sleep
import argparse

parser = argparse.ArgumentParser(description = 'Species assessment automated search through IUCN Red List API')
parser.add_argument('-d', '--directory', type = str, help = 'Path to the .csv file')
parser.add_argument('-r', '--region', type = str, help = 'Search species assessments for a specific region using the IUCN region identifier')
args = parser.parse_args()

name_input = []
syn = []
acceptedname = []
status = []
id = []
assess = []
crit = []
reg = []

if args.region:
    splist = pd.read_csv(args.directory, header = None)
    def getStatus(spname):
        url = 'https://apiv3.iucnredlist.org/api/v3/species/' + spname + '/region/' + args.region + '?token=' + splist[0][0]
        r = requests.get(url)
        while True:
            try:
                status.append(r.json()['result'][0]['category'])
                name_input.append(spname)
                syn.append('FALSE')
                acceptedname.append(spname)
                id.append(r.json()['result'][0]['taxonid'])
                assess.append(r.json()['result'][0]['assessment_date'])
                crit.append(r.json()['result'][0]['criteria'])
                reg.append(r.json()['region_identifier'])
                break
            except IndexError:
                name_input.append(r.json()['name'])
                status.append('NE')
                syn.append('FALSE')
                acceptedname.append(r.json()['name'])
                id.append('NA')
                assess.append('NA')
                crit.append('NA')
                reg.append(r.json()['region_identifier'])
                break
            except KeyError:
                url2 = 'https://apiv3.iucnredlist.org/api/v3/species/synonym/' + spname + '?token=' + splist[0][0]
                r2 = requests.get(url2)
                name_input.append(spname)
                syn.append('TRUE')
                acceptedname.append(r2.json()['result'][0]['accepted_name'])
                url3 = 'https://apiv3.iucnredlist.org/api/v3/species/' + r2.json()['result'][0]['accepted_name'] + '?token=' + splist[0][0]
                r3 = requests.get(url3)
                status.append(r3.json()['result'][0]['category'])
                id.append(r3.json()['result'][0]['taxonid'])
                assess.append(r3.json()['result'][0]['assessment_date'])
                crit.append(r3.json()['result'][0]['criteria'])
                reg.append(r.json()['region_identifier'])
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

            dict = {'name_input':name_input, 'synonym':syn, 'accepted_name':acceptedname,
            'region':reg ,'category':status, 'criteria':crit, 'taxon_id':id, 'assessment_date':assess}
            while True:
                try:
                    df = pd.DataFrame(dict)
                    df.to_csv('status.csv')
                    break
                except ValueError:
                    print("ERROR: species names aren't correct")
                    break
        print('done')
else:
    splist = pd.read_csv(args.directory, header = None)
    def getStatus(spname):
        url = 'https://apiv3.iucnredlist.org/api/v3/species/' + spname + '?token=' + splist[0][0]
        r = requests.get(url)
        while True:
            try:
                status.append(r.json()['result'][0]['category'])
                name_input.append(spname)
                syn.append('FALSE')
                acceptedname.append(spname)
                id.append(r.json()['result'][0]['taxonid'])
                assess.append(r.json()['result'][0]['assessment_date'])
                crit.append(r.json()['result'][0]['criteria'])
                break
            except IndexError:
                name_input.append(r.json()['name'])
                status.append('NE')
                syn.append('FALSE')
                acceptedname.append(r.json()['name'])
                id.append('NA')
                assess.append('NA')
                crit.append('NA')
                break
            except KeyError:
                url2 = 'https://apiv3.iucnredlist.org/api/v3/species/synonym/' + spname + '?token=' + splist[0][0]
                r2 = requests.get(url2)
                name_input.append(spname)
                syn.append('TRUE')
                acceptedname.append(r2.json()['result'][0]['accepted_name'])
                url3 = 'https://apiv3.iucnredlist.org/api/v3/species/' + r2.json()['result'][0]['accepted_name'] + '?token=' + splist[0][0]
                r3 = requests.get(url3)
                status.append(r3.json()['result'][0]['category'])
                id.append(r3.json()['result'][0]['taxonid'])
                assess.append(r3.json()['result'][0]['assessment_date'])
                crit.append(r3.json()['result'][0]['criteria'])
                break

    spp = splist.iloc[1: , :]
    if __name__ == '__main__':
        for i in spp[0]:
            getStatus(i)
            print(f'Searching for {i} global assessment...')
            if len(spp) > 50:
                sleep(5)
            else:
                sleep(2)

            dict = {'name_input':name_input, 'synonym':syn, 'accepted_name':acceptedname,
            'category':status, 'criteria':crit, 'taxon_id':id, 'assessment_date':assess}
            while True:
                try:
                    df = pd.DataFrame(dict)
                    df.to_csv('status.csv')
                    break
                except ValueError:
                    print("ERROR: species names aren't correct")
                    break
        print('done')
