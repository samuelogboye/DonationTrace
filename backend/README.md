# HealthSync

## Backend

Final Portfolio Project for Software Engineering at ALX

# Run the Application

## create a virtual environment (linux/macOS)

```bash
python3 -m venv venv
```

## Activate the virtual environment (linux/macOS)

```bash
source venv/bin/activate
```

## Install all packages

```bash
python3 install -r requirments.txt
```

## Apply migrations

```bash
python3 manage.py makemigrations
```

## Migrate the models

```bash
python3 manage.py migrate
```

## Run the application

```bash
python3 manage.py runserver
```

## Cheers !!!

## To run with DOCKER

### Build the image

```bash
docker build -t health-backend .
```

### Run the Cntainer

```bash
docker run -d -p 8000:8000 health-backend
```

After running this command, the application should be accessible at `http://localhost:8080`
