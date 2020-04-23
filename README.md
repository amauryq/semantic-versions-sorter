# PO REST Services

## Installing

```bash
cd semantic-version-sorter
pip install virtualenv
virtualenv venv
# windows
## cmd
venv\\Scripts\\activate.bat
## ps
set-executionpolicy remotesigned # optional if needed
.\\venv\\Scripts\\activate.ps1
pip install -r requirements.txt
# linux
venv/bin/pip install -r requirements.txt
```
## Get All PO's

```bash
curl -i http://localhost:5000/
```

## Get Specific PO

```bash
curl -i http://localhost:5000/{po}
```

## Get Lines from PO

```bash
curl -i http://localhost:5000/{po}/{line}
```
