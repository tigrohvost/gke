# gke

Docker part:
All we need is to run
'docker-compose up'
and curl to localhost (or ip of the server we run it on) at port 8001

K8s part (GKE specific):
kubectl apply -f ./back-pod.yaml
kubectl apply -f ./front-pod.yaml
kubectl create -f service-front-lb.yaml
kubectl apply -f ./service-back.yaml
