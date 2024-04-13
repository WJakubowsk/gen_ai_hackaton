# Application deployment

Run following:
```
az login
docker login # (log in to the docker hub)
docker build -t <username>/<repository_name> . # eg. wiktorjakubowski/ailytics
docker push
az container create --resource-group RESOURCE_GR_4 --name ailytics -f deployment.yml
```
