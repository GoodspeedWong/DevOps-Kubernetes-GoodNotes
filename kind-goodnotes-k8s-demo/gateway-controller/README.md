

## Installation
```sh
helm template eg oci://docker.io/envoyproxy/gateway-helm \
  -n gateway \
  -f ./kind-goodnotes-k8s-demo/gateway-controller/values.yaml \
  > ./kind-goodnotes-k8s-demo/gateway-controller/manifest.yaml

 k diff -f kind-goodnotes-k8s-demo/gateway-controller/manifest.yaml

 k apply -f kind-goodnotes-k8s-demo/gateway-controller/manifest.yaml

```