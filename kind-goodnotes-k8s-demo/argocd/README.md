

## Installation

```sh
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

helm template argocd argo/argo-cd \
  --namespace argocd \
  --create-namespace \
  -f values-poc.yaml > manifest.yaml

kustomize build kind-goodnotes-k8s-demo/argocd | kubectl diff -f -
```

