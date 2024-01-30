# School Management Backend

## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
$env:FLASK_APP = "core/server.py"
rm core/store.sqlite3
flask db upgrade -d core/migrations/

```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```
## Running the Application with Docker

### Prerequisites
- [Docker](https://www.docker.com/) installed on your machine

### Build the Docker image:
docker build -t your-image-name .
- Replace your-image-name with a suitable name for your Docker image.

### Run the Docker container:
docker run -p 7755:7755 your-image-name 

### Access the application:
Open your browser and navigate to http://localhost:7755

### Stopping the Application
docker stop $(docker ps -q --filter ancestor=your-image-name)




