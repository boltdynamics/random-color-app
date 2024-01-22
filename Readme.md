## RANDOM COLOR APP

A simple app that renders a html page that changes color each time you refresh your screen!

https://github.com/boltdynamics/random-color-app/assets/42393225/09ff1b4b-ce19-49c5-8ccd-6b243948805c

### Commands to run on google cloud shell

* Create a folder
```bash
mkdir projects && cd projects
```

* Clone the repository
```bash
git clone https://github.com/boltdynamics/random-color-app
```

* Deploy app to Google Cloud Run
```bash
gcloud run deploy random-color-app --source . --allow-unauthenticated --region=us-central1 --project pras-sandbox-405410
```
