# PO REST Services

## Installing

$ cd fl-exam
$ virtualenv venv
$ venv/bin/pip install -r requirements.txt

## Get All PO's

curl -i http://localhost:5000/

## Get Specific PO

curl -i http://localhost:5000/{po}

## Get Lines from PO

curl -i http://localhost:5000/{po}/{line}
