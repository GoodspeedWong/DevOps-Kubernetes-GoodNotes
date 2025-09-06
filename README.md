# DevOps-Kubernetes-GoodNotes

A demo k8s cluster running locally with Github Actions CI workflows (self-hosted runner) covers cluster creation and load testing for following tasks.


1. For each pull request to the default branch, trigger the CI workflow. (for example with GitHub Actions)
2. Provision a multi-node (at least 2 nodes) Kubernetes cluster (you may use [KinD](https://kind.sigs.k8s.io/) to provision this cluster on the [CI runner](https://github.com/actions/runner-images/blob/main/images/linux/Ubuntu2204-Readme.md) (localhost))
3. Deploy Ingress controller to handle incoming HTTP requests
4. Create 2 [http-echo](https://github.com/hashicorp/http-echo) deployments, one serving a response of “bar” and another serving a response of “foo”.
5. Configure cluster / ingress routing to send traffic for “bar” hostname to the bar deployment and “foo” hostname to the foo deployment on local cluster (i.e. route both [http://foo.localhost](http://foo.localhost/) and [http://bar.localhost](http://bar.localhost/)).
6. Ensure the ingress and deployments are healthy before proceeding to the next step.
7. Generate a load of randomized traffic for bar and foo hosts and capture the load testing result
8. Post the output of the load testing result as comment on the GitHub Pull Request (automated the CI job). Depending on the report your load testing script generates, ideally you'd post stats for http request duration (avg, p90, p95, ...), % of http request failed, req/s handled.


## Repository Structure

```text
.
├── .github/workflows           # Github Actions workflows for cluster creation and load testing
├── goodnotes-k8s-demo          # cluster configuration
├── kind-goodnotes-k8s-demo
│   ├── apps                    # cluster workloads
│   ├── ingress-controller      # NGINX Ingress Controller
│   ├── namespaces              # Namespaces configuration
│   └── prometheus              # Prometheus stack with Grafana for monitoring
└── scripts                     # Scripts location

```

## Access

[Prometheus Query UI](http://prometheus.localhost:8080)

[Grafana UI](http://grafana.localhost:8080)

## Examples PRs:

[Cluster Creation](https://github.com/GoodspeedWong/DevOps-Kubernetes-GoodNotes/pull/1)
[Apps replica update and load testing](https://github.com/GoodspeedWong/DevOps-Kubernetes-GoodNotes/pull/9)


## Cluster workloads provisions quickview by namespaces

### apps
```sh
➜  DevOps-Kubernetes-GoodNotes git:(main) ✗ k get all -n apps
NAME                       READY   STATUS    RESTARTS   AGE
pod/bar-5d84b94647-dm888   1/1     Running   0          29h
pod/bar-5d84b94647-kr9lw   1/1     Running   0          24h
pod/bar-5d84b94647-lgr2f   1/1     Running   0          16h
pod/bar-5d84b94647-tf5pf   1/1     Running   0          16h
pod/bar-5d84b94647-wfspj   1/1     Running   0          29h
pod/bar-5d84b94647-zdxgj   1/1     Running   0          24h
pod/foo-6b55bdf-f5sbf      1/1     Running   0          16h
pod/foo-6b55bdf-fr7mz      1/1     Running   0          29h
pod/foo-6b55bdf-lmxpr      1/1     Running   0          24h
pod/foo-6b55bdf-lzwbq      1/1     Running   0          29h
pod/foo-6b55bdf-mpgxs      1/1     Running   0          24h
pod/foo-6b55bdf-mvf7g      1/1     Running   0          16h

NAME          TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/bar   ClusterIP   10.96.38.224   <none>        80/TCP    29h
service/foo   ClusterIP   10.96.96.27    <none>        80/TCP    29h

NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/bar   6/6     6            6           29h
deployment.apps/foo   6/6     6            6           29h

NAME                             DESIRED   CURRENT   READY   AGE
replicaset.apps/bar-5d84b94647   6         6         6       29h
replicaset.apps/foo-6b55bdf      6         6         6       29h
➜  DevOps-Kubernetes-GoodNotes git:(main) ✗ 
```

### ingress-nginx
```sh
➜  DevOps-Kubernetes-GoodNotes git:(main) ✗ k get all -n ingress-nginx
NAME                                            READY   STATUS      RESTARTS   AGE
pod/ingress-nginx-admission-create-jztqr        0/1     Completed   0          28h
pod/ingress-nginx-admission-patch-fj4l4         0/1     Completed   0          28h
pod/ingress-nginx-controller-78d7c886bd-sm8rg   1/1     Running     0          26h

NAME                                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
service/ingress-nginx-controller             LoadBalancer   10.96.150.77    <pending>     80:31688/TCP,443:32093/TCP   28h
service/ingress-nginx-controller-admission   ClusterIP      10.96.194.144   <none>        443/TCP                      28h

NAME                                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/ingress-nginx-controller   1/1     1            1           28h

NAME                                                  DESIRED   CURRENT   READY   AGE
replicaset.apps/ingress-nginx-controller-76666fb69    0         0         0       28h
replicaset.apps/ingress-nginx-controller-78d7c886bd   1         1         1       26h

NAME                                       STATUS     COMPLETIONS   DURATION   AGE
job.batch/ingress-nginx-admission-create   Complete   1/1           2m14s      28h
job.batch/ingress-nginx-admission-patch    Complete   1/1           16m        28h
➜  DevOps-Kubernetes-GoodNotes git:(main) ✗  
```

### monitoring
```sh
➜  DevOps-Kubernetes-GoodNotes git:(main) ✗ k get all -n monitoring
NAME                                       READY   STATUS    RESTARTS   AGE
pod/alertmanager-main-0                    2/2     Running   0          18h
pod/alertmanager-main-1                    2/2     Running   0          18h
pod/alertmanager-main-2                    2/2     Running   0          18h
pod/blackbox-exporter-78cc978f77-ppvxr     3/3     Running   0          18h
pod/grafana-5c5f5b469f-w2fvh               1/1     Running   0          18h
pod/kube-state-metrics-5f96f94459-4qbv5    3/3     Running   0          18h
pod/node-exporter-6vrk7                    2/2     Running   0          18h
pod/node-exporter-9t22x                    2/2     Running   0          18h
pod/node-exporter-f6rd4                    2/2     Running   0          18h
pod/node-exporter-nhtm8                    2/2     Running   0          18h
pod/prometheus-adapter-599c88b6c4-dckz7    1/1     Running   0          18h
pod/prometheus-adapter-599c88b6c4-frzt2    1/1     Running   0          18h
pod/prometheus-k8s-0                       2/2     Running   0          18h
pod/prometheus-k8s-1                       2/2     Running   0          18h
pod/prometheus-operator-76cf594d46-ctrmr   3/3     Running   0          18h

NAME                            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
service/alertmanager-main       ClusterIP   10.96.205.196   <none>        9093/TCP,8080/TCP            18h
service/alertmanager-operated   ClusterIP   None            <none>        9093/TCP,9094/TCP,9094/UDP   18h
service/blackbox-exporter       ClusterIP   10.96.44.42     <none>        9115/TCP,19115/TCP           18h
service/grafana                 ClusterIP   10.96.11.146    <none>        80/TCP,3000/TCP              18h
service/kube-state-metrics      ClusterIP   None            <none>        8443/TCP,9443/TCP            18h
service/node-exporter           ClusterIP   None            <none>        9100/TCP                     18h
service/prometheus-adapter      ClusterIP   10.96.115.254   <none>        443/TCP                      18h
service/prometheus-k8s          ClusterIP   10.96.46.71     <none>        9090/TCP,8080/TCP            18h
service/prometheus-operated     ClusterIP   None            <none>        9090/TCP                     18h
service/prometheus-operator     ClusterIP   None            <none>        8443/TCP                     18h

NAME                           DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
daemonset.apps/node-exporter   4         4         4       4            4           kubernetes.io/os=linux   18h

NAME                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/blackbox-exporter     1/1     1            1           18h
deployment.apps/grafana               1/1     1            1           18h
deployment.apps/kube-state-metrics    1/1     1            1           18h
deployment.apps/prometheus-adapter    2/2     2            2           18h
deployment.apps/prometheus-operator   1/1     1            1           18h

NAME                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/blackbox-exporter-78cc978f77     1         1         1       18h
replicaset.apps/grafana-5c5f5b469f               1         1         1       18h
replicaset.apps/kube-state-metrics-5f96f94459    1         1         1       18h
replicaset.apps/prometheus-adapter-599c88b6c4    2         2         2       18h
replicaset.apps/prometheus-operator-76cf594d46   1         1         1       18h

NAME                                 READY   AGE
statefulset.apps/alertmanager-main   3/3     18h
statefulset.apps/prometheus-k8s      2/2     18h
➜  DevOps-Kubernetes-GoodNotes git:(main) ✗ 
```