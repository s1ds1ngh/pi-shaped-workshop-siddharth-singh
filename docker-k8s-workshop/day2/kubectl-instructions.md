# Kubectl Apply and Verification Instructions

## Prerequisites
- Kubernetes cluster is up and running
- kubectl is installed and configured to communicate with your cluster
- Docker image has been built and pushed to a registry (from Day 1 assignment)

## Labeling Your Nodes
Before applying the manifest, you need to label your nodes to match the affinity rules:

```bash
# Label a node with environment=production
kubectl label nodes <node-name> environment=production

# Label a node with disktype=ssd
kubectl label nodes <node-name> disktype=ssd

# Label a node with app-type=api
kubectl label nodes <node-name> app-type=api
```

Replace `<node-name>` with the actual name of your node. You can get node names using:
```bash
kubectl get nodes
```

## Applying the Manifest
To apply the combined manifest:

```bash
kubectl apply -f combined-manifest.yaml
```

## Verifying Deployment
Check if the deployment was created:

```bash
kubectl get deployments
```

## Verifying Pod Placement
To verify that pods were scheduled according to the node affinity rules:

```bash
kubectl get pods -o wide
```

This command will show you which nodes the pods are running on. The output should confirm that pods are scheduled on nodes that match the affinity rules (nodes labeled with environment=production).

## Checking Pod Details
To see detailed information about a pod, including which affinity rules were applied:

```bash
kubectl describe pod <pod-name>
```

Replace `<pod-name>` with the name of one of your pods from the previous command.

## Checking Logs
To check the logs of your application:

```bash
kubectl logs <pod-name>
```

## Cleaning Up
When you're done, you can delete the deployment:

```bash
kubectl delete -f combined-manifest.yaml
```
