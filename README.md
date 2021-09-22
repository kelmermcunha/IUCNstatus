# IUCNstatus
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](./LICENSE)

Species assessment automated search through IUCN Red List API

## Pre-requisites

You'll need [Python 3](https://www.python.org/downloads/) installed in order to run this script.

### Python libraries

```sh
  $ sudo apt install -y python3.pip
  $ sudo pip3 install --upgrade pip
```

```sh
  $ sudo pip3 install requests
  $ sudo pip3 install pandas
  $ sudo pip3 install argparse
```

## Installation

### Clone

You'll need [Git](https://git-scm.com) installed to sucessfully clone and run this script. In your command line:

```bash
  # First, clone this repository
  $ git clone https://github.com/kelmermcunha/IUCNstatus
  
  # Change your directory to this repository
  $ cd IUCNstatus
  
  # Run the script
  $ python3 IUCNstatus.py --help
```

### Download

Alternatively, you can download the script directly in the "Code" buttom. Then, run in your command line:

```bash
  # Change to the directory where you downloaded the script
  $ cd path/to/the/folder
  
  # Run the script
  $ python3 IUCNstatus.py --help
```

## How to use

You'll first need to [generate](https://apiv3.iucnredlist.org/api/v3/token) a personal API token to connect with IUCN Red List API.

Then, create a .csv file following the [example](https://github.com/kelmermcunha/IUCNstatus/blob/main/input-example.csv). 
Note that the API token is in the first line, followed by the species names in the same column.

```bash
  $ python3 IUCNstatus.py --help
usage: IUCNstatus.py [-h] [-d DIRECTORY] [-r REGION]

Species assessment automated search through IUCN Red List API

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Path to the .csv file
  -r REGION, --region REGION
                        Search species assessments for a specific region using
                        the IUCN region identifier
```

To perform a search within a specific region, use the [region identifiers](https://apiv3.iucnredlist.org/api/v3/region/list?token=9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee) defined by IUCN.

## Author

* [Kelmer Martins-Cunha](https://github.com/kelmermcunha)

## Organization

* [Monitoring and Inventorying the Neotropical Diversity of Funga](https://mindfunga.ufsc.br) (MIND.Funga, MICOLAB/UFSC, Santa Catarina, Brazil)

## License

This project is licensed under the GNU General Public License v3.0 License - see the [LICENSE](./LICENSE) file for details.
