## Setting up Project (MAC)

### Deactivate any existing virtual environment

```sh
deactivate
```

### Remove the virtual environment directory

```sh
rm -rf venv
```

### Create a new virtual environment (install python 10.15)

```sh
python3.10 -m venv venv
```

### Activate the virtual environment

```sh
source venv/bin/activate
```

### Install dependencies

```sh
pip install -e .
```

### Start the qdrant and kafka server

```sh
docker-compose up -d
```

### Stop the qdrant and kafka server

```sh
docker-compose down
```