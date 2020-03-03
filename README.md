## Setup

### Local development

Setup and activate virtual environment:
```shell script
virtualenv --python=/usr/bin/python3.7 .env
source .env/bin/activate
```

Install python requirements:

```shell script
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Testing

```shell script
tox
```
