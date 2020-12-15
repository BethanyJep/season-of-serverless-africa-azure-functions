# Season-of-serverless-Africa (-azure-functions-)

## About the code sample

Using Azure functions to fetch json files for meals in Africa

## Prerequisites

* Python 3.6, 3.7 or 3.8 (if you have 3.9 you will need to use a virtual environment)
* npm to install azure-functions core tools
* anaconda to install virtual environment

P.S. I'm using windows

### Installation

Check the python version you have.

```bash
python --version
```

If it is not 3.6, 3.7 or 3.8 create a virual environment using anaconda.

```bash
conda create -n [environment name] python=[version]
```

Activate your environment

```bash
conda activate [environment name]
```
Install azure-functions core tools (v3) using npm

```bash
npm i -g azure-functions-core-tools@3
```
Initialize the function

```bash
func init
```

Run the function
```bash
func start
```
