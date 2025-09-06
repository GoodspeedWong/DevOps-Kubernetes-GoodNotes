
## 1st time installation

1. Checkout from main branch
```sh
git checkout -b main-update-namespaces
```
2. Create yaml file and run `kustomize build`
```sh
kustomize build kind-goodnotes-k8s-demo/namespaces | kubectl diff -f -
```

3. Commit and create PR with pasting diff output for review.

```sh
kubectl apply -k kind-goodnotes-k8s-demo/namespaces

```

4. PR approved then apply the changes. merge and delete branch. 
```sh
kubectl apply -k kind-goodnotes-k8s-demo/namespaces
```

## Manual updates

1. checkout from main branch
```sh
git checkout -b main-update-namespaces
```

2. update yaml file and run the `kubectl diff`
```sh
kubectl diff -k kind-goodnotes-k8s-demo/namespaces
```

3. Commit and create PR with pasting diff output for review.

4. PR approved then apply the changes. merge and delete branch. 
```sh
kubectl apply -k kind-goodnotes-k8s-demo/namespaces
```