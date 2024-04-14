# Application deployment

Make sure you deployed model's API first.
1. Copy API URL (e.g. ailytics.francecentral.azurecontainer.io:8080/sql-azure-openai/invoke) with endpoint as environment variable in deployment.yml file.

2. Run following:
```
az login
docker login # (log in to the docker hub)
docker build -t <username>/<repository_name> .
docker push <username>/<repository_name>
az container create --resource-group <resource_group_name> --name ailytics -f deployment.yml
```

3. Application should be available under `<name>/<region>.azurecontainer.io` domain.