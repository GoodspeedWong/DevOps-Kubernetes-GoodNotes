
## Installation

```sh
kustomize build kind-goodnotes-k8s-demo/namespaces | kubectl diff -f -
```


```sh
kubectl apply -k kind-goodnotes-k8s-demo/namespaces

```