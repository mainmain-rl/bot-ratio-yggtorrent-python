# YGGTORRENT BOT

## What am I doing ?
Hello ! I'm a bot to get your yggtorrent seeding informations and upload it in datadog !

I get your upload and download public information, I made the ratio of it and it's in your datadog account !

All the data is in Go.
## How to use me ?

I work with 3 variables :
* DD_API_KEY=YOUR_API_KEY
* DD_SITE="https://datadoghq.eu"
* YGGTORRENT_PROFILE_URL="https://www5.yggtorrent.fi/profile/xxxxx-you_name"

You can find your yggtorrent public id in "my account", near of your upload/download data there is an eye, click on it, this is the link !

### exemple with docker :

You can run me like that:
```bash
docker run --name bot-yggtorrent-test \
    -e DD_API_KEY=YOUR_API_KEY \
    -e DD_SITE="https://datadoghq.eu" \
    -e YGGTORRENT_PROFILE_URL="https://www5.yggtorrent.fi/profile/67491-garzeus" \
    mainmain-rl/bot-yggtorrent:latest
```

Don't hesitate to use me with docker-compose or Kubernetes !

## Never forget:
You can update me !