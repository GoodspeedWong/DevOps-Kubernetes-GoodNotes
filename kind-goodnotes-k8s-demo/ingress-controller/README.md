

## Deployment

create `ingress-nginx` namespace before creating ingress-controller

```sh

kustomize build kind-goodnotes-k8s-demo/ingress-controller | kubectl diff -f -

kubectl apply -k kind-goodnotes-k8s-demo/ingress-controller
```
