

## Deployment

```sh

kustomize build kind-goodnotes-k8s-demo/apps/<app_name> | kubectl diff -f -

```

Raise a PR and paste diff output with comment for review

apply it once approved and without code confliction.

```sh
kubectl apply -k kind-goodnotes-k8s-demo/apps/<app_name>
```
