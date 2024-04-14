# Application deployment


1. Fill in environment variables in `deployment.yml` file in the specified places.

2. Run following:
```
az login
docker login # (log in to the docker hub / Azure Container Registry)
docker build -t <username>/<repository_name> .
docker push <username>/<repository_name>
az container create --resource-group <resource_group_name> --name ailytics -f deployment.yml
```

3. Application should be available under `<name>/<region>.azurecontainer.io` domain.