# PO REST Services

## Installing

```bash
cd fl-exam
virtualenv venv
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
