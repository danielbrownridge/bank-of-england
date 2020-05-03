# Kubernetes Deployment YAML
A developer gives you a daemon that listens on port tcp/3000. They ask you to containerise it, and deploy it into a kubernetes cluster.

Please write deployment YAML to support this.

## Answer

`deployment.yaml`**

```yaml
apiVersion: app/v1
kind: Deployment
metadata:
  name: daemon-deployment
  labels:
    app: daemon
spec:
  replicas: 2
  selector:
    matchLabels:
      app: daemon
  template:
    metadata:
      labels:
        app: daemon
    spec:
      containers:
      - name: daemon
        image: daemon:1.0.0
        ports:
        - containerPort: 3000
```

This will create two replicas of a container called `daemon`. 
This assumes that such a container exists. For the deployment YAML to work A
container would have needed to been defined and uploaded to a suitable container
repository.

###Dockerfile**

```dockerfile
FROM ubuntu
ENTRYPOINT ["daemon"]
```
