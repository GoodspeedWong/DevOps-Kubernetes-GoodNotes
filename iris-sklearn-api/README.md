

## Image build
```sh
docker build -t iris-sklearn-api:local .
```

### Build logs
```text
➜  Iris-traning git:(main-ingress-controller-updates) ✗ docker build -t iris-sklearn-api:local .
[+] Building 28.3s (12/12) FINISHED                                                                                                                                                                                                                            docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                                           0.0s
 => => transferring dockerfile: 369B                                                                                                                                                                                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                                                                                                                            3.3s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                                                                                                  0.0s
 => [internal] load .dockerignore                                                                                                                                                                                                                                              0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                                0.0s
 => [1/6] FROM docker.io/library/python:3.11-slim@sha256:e4676722fba839e2e5cdb844a52262b43e90e56dbd55b7ad953ee3615ad7534f                                                                                                                                                      2.6s
 => => resolve docker.io/library/python:3.11-slim@sha256:e4676722fba839e2e5cdb844a52262b43e90e56dbd55b7ad953ee3615ad7534f                                                                                                                                                      0.0s
 => => sha256:c318c623f71690dfe89caa29d2f7ab5cc4adbc3a11b5e42c8eede49516ed721d 248B / 248B                                                                                                                                                                                     0.7s
 => => sha256:e6303e21d64b9e80197b44e27731d6d0898a31e447dfd8910ae8e62d835ffc9e 14.31MB / 14.31MB                                                                                                                                                                               1.6s
 => => sha256:8e8ea7735c83f82e69e5b70f8a34ee72969666d6434d9c442a8680e9a5aa0167 1.27MB / 1.27MB                                                                                                                                                                                 1.6s
 => => sha256:51365f04b68881c6fd3d04aa38cdb689fdee6efba2aa6afcf2da5385022cf475 30.14MB / 30.14MB                                                                                                                                                                               2.0s
 => => extracting sha256:51365f04b68881c6fd3d04aa38cdb689fdee6efba2aa6afcf2da5385022cf475                                                                                                                                                                                      0.3s
 => => extracting sha256:8e8ea7735c83f82e69e5b70f8a34ee72969666d6434d9c442a8680e9a5aa0167                                                                                                                                                                                      0.0s
 => => extracting sha256:e6303e21d64b9e80197b44e27731d6d0898a31e447dfd8910ae8e62d835ffc9e                                                                                                                                                                                      0.2s
 => => extracting sha256:c318c623f71690dfe89caa29d2f7ab5cc4adbc3a11b5e42c8eede49516ed721d                                                                                                                                                                                      0.0s
 => [internal] load build context                                                                                                                                                                                                                                              0.0s
 => => transferring context: 2.24kB                                                                                                                                                                                                                                            0.0s
 => [2/6] WORKDIR /app                                                                                                                                                                                                                                                         0.2s
 => [3/6] COPY requirements.txt .                                                                                                                                                                                                                                              0.0s
 => [4/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                                                                                                  15.4s
 => [5/6] COPY train.py app.py ./                                                                                                                                                                                                                                              0.0s 
 => [6/6] RUN python train.py                                                                                                                                                                                                                                                  0.5s 
 => exporting to image                                                                                                                                                                                                                                                         6.1s 
 => => exporting layers                                                                                                                                                                                                                                                        5.1s 
 => => exporting manifest sha256:baff18f58024e3daa78387136a9f8c628dc6f8a7d794d378894c54e0b41d2789                                                                                                                                                                              0.0s 
 => => exporting config sha256:10f128454884019e6dd076f8f99b2ba49d93c170b2205e7e8c5b8d5bf3948f19                                                                                                                                                                                0.0s 
 => => exporting attestation manifest sha256:c3fa73e5b32e610947ef8544abba3f1d73bdfd555877f54a43950ea45b4e32f5                                                                                                                                                                  0.0s
 => => exporting manifest list sha256:96614ecae7796c536c6b25eed5c3e7a9d136fd215e2f5b44c8eb0fbf587fd740                                                                                                                                                                         0.0s
 => => naming to docker.io/library/iris-sklearn-api:local                                                                                                                                                                                                                      0.0s
 => => unpacking to docker.io/library/iris-sklearn-api:local                                                                                                                                                                                                                   0.9s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/16se3r4n7u516xo3cdwnf91th
➜  Iris-traning git:(main-ingress-controller-updates) ✗ 
```



