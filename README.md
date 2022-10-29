# YGGTORRENT BOT
[![Docker Image CI](https://github.com/mainmain-rl/bot-ratio-yggtorrent-python/actions/workflows/docker-image.yaml/badge.svg?branch=main)](https://github.com/mainmain-rl/bot-ratio-yggtorrent-python/actions/workflows/docker-image.yaml)
![Docker Image CI](https://img.shields.io/github/license/mainmain-rl/bot-ratio-yggtorrent-python)

## What am I doing ?
Hello ! I'm a bot to get your yggtorrent seeding informations and upload it in datadog !

I get your upload and download public information, I made the ratio of it and it's in your datadog account !

The exporting data can be in To or Go.
## How to use me?
My images are availables in ARM & AMD platform !

I work with 3 variables:
* DD_API_KEY=YOUR_API_KEY
* DD_SITE="https://datadoghq.eu"
* YGGTORRENT_PROFILE_URL="https://www5.yggtorrent.fi/profile/xxxxx-you_name"

You can find your yggtorrent public id in "my account", near of your upload/download data there is an eye, click on it, this is the link !
## Example with docker:

```bash
docker run --name bot-yggtorrent-test \
    -e DD_API_KEY=YOUR_API_KEY \
    -e DD_SITE="https://datadoghq.eu" \
    -e YGGTORRENT_PROFILE_URL="https://www5.yggtorrent.fi/profile/xxxxx-you_name" \
    mainmainrl/bot-yggtorrent:0.0.4
```

## Example with Kubernetes:
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: bot-yggtorrent
spec:
  schedule: "*/5 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: bot-yggtorrent
            image: mainmainrl/bot-yggtorrent:cronjob-v1.0
            imagePullPolicy: IfNotPresent
            env:
            - name: DD_API_KEY
              value: YOU_TOKEN_HERE
            - name: DD_SITE
              value: "https://datadoghq.eu"
            - name: YGGTORRENT_PROFILE_URL
              value: "https://www5.yggtorrent.fi/profile/YOUR_ID_HERE"
          restartPolicy: OnFailure
```

## in Datadog:

You can explore the 3 metrics:
* yggtorrent.metric.upload
* yggtorrent.metric.download
* yggtorrent.metric.ratio

## Never forget:
You can update me !