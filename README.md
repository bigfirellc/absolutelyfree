# absolutelyfree

The Absolutely Free Random Band Name Maker, at [www.absolutelyfree.net](https://www.absolutelyfree.net). A very simple random band name and album name generator, backended with Django, complete with admin panel and PostgreSQL hooks. Static files and media files can be uploaded to any AWS compatible storage bucket. Comes with optional "Jumble" mode that shuffles the inputted band names together.

## Docker
Absolutely Free is deployed via Docker Compose. Clone the repo into `/app/absolutelyfree`, and build the Docker image:

```
docker compose build -t absolutelyfree .
```

Then run it and the PostgreSQL instance with docker compose:

```
docker compose up -d
```