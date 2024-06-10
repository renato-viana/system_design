# Curso Completo de Arquitetura de Microserviços e Design de Sistemas com Python & Kubernetes

## Configuração

### Instalação e Configuração do kubectl no Arch Linux

Primeiro, baixe o kubectl usando o seguinte comando:

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
```

Em seguida, instale o kubectl com o seguinte comando:

```bash
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

Para verificar a instalação, execute:

```bash
kubectl version --client
```

### Instalação do Minikube

Primeiro, baixe o Minikube usando o seguinte comando:

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```

Em seguida, instale o Minikube com o seguinte comando:

```bash
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

Para iniciar o Minikube, execute:

```bash
minikube start
```

### Instalação do k9s

```bash
sudo pacman -S k9s
```

### Criação de Ambiente Virtual

```bash
python3 -m venv venv
```

```bash
source ./venv/bin/activate
```

```bash
env | grep VIRTUAL
```

### Solução de Problemas com VS Code erro /mnt/c/Users/renat/AppData/Local/Programs/Microsoft VS Code/bin/code: line 61: /mnt/c/Users/renat/AppData/Local/Programs/Microsoft VS Code/Code.exe: cannot execute binary file: Exec format error

```bash
wsl.exe --shutdown
```

### Instalação das Dependências do Projeto

```bash
pip install pyjwt
```

```bash
pip install flask
```

```bash
sudo pacman -Sy
```

```bash
sudo pacman -S python base-devel mariadb-libs pkg-config
```

```bash
pip install flask_mysqldb

export MYSQL_HOST=localhost
```

```bash
pip install pyMongo
```

```bash
pip install Flask-PyMongo
```

```bash
pip install pika
```

```bash
pip install flask
```

```bash
pip install requests
```

```bash
pip install moviepy
```

### Execute os comandos Docker para executar o aquivo init.sql

- docker exec -i auth-mysql-server mysql -uroot < init.sql
- docker exec -i auth-mysql-server mysql -uroot -e "DROP USER auth_user@localhost"
- docker exec -i auth-mysql-server mysql -uroot -e "DROP DATABASE auth"

- docker run -it --name mysql-client --network auth-mysql-network --rm mysql:8.0.33 mysql -h mysql -uroot -p

### Todas as bibliotecas atualmente instaladas no seu ambiente virtual.

- pip freeze > requirements.txt
- pip install -r requirements.txt

### Kubernetes

- kubectl apply -f ./

- minikube addons list
- minikube addons enable ingress "NGINX Ingress Controller1"
- minikube tunnel
- kubectl get pods -n ingress-nginx1
- kubectl scale deployment --replicas=0 gateway

### Utilizando [Kind](https://kind.sigs.k8s.io/)

- kubectl config get-contexts
- kubectl config use-context kind-kind
- kind create cluster
- kind delete cluster

#### [Setting Up An Ingress Controller](https://kind.sigs.k8s.io/docs/user/ingress/)

```bash
cat <<EOF | kind create cluster --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
EOF
```

- kubectl apply -f https://projectcontour.io/quickstart/contour.yaml

```bash
kubectl patch daemonsets -n projectcontour envoy -p '{"spec":{"template":{"spec":{"nodeSelector":{"ingress-ready":"true"},"tolerations":[{"key":"node-role.kubernetes.io/control-plane","operator":"Equal","effect":"NoSchedule"},{"key":"node-role.kubernetes.io/master","operator":"Equal","effect":"NoSchedule"}]}}}}'
```
