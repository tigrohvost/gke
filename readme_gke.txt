https://github.com/tigrohvost/gke

https://console.cloud.google.com/kubernetes/list/overview?walkthrough_id=gke_quickstart&project=total-zodiac-335107

https://habr.com/ru/post/589415/
https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/

https://github.com/jamiehannaford/what-happens-when-K8S


git PAT
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

cool kompose DO guide
https://www.digitalocean.com/community/tutorials/how-to-migrate-a-docker-compose-workflow-to-kubernetes


export DOCKER_REGISTRY_SERVER=https://index.docker.io/v1/
export DOCKER_USER=tigrohvostgke
export DOCKER_PASSWORD=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

kubectl create secret docker-registry myregistrykey \
  --docker-server=$DOCKER_REGISTRY_SERVER \
  --docker-username=$DOCKER_USER \
  --docker-password=$DOCKER_PASSWORD


https://logz.io/blog/containerized-app-gke/


containerPort - the port app on which app can be reached inside the container
