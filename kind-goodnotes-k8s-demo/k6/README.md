
## Installation

```sh

helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm template k6-operator grafana/k6-operator \
--namespace k6 \
--values kind-goodnotes-k8s-demo/k6/values.yaml \
> kind-goodnotes-k8s-demo/k6/manifests.yaml


kustomize build kind-goodnotes-k8s-demo/k6 | kubectl diff -f -

# Create PR pasting diff output and apply once approved

kubectl apply -k kind-goodnotes-k8s-demo/k6

```