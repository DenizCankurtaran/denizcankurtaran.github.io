Kibana: http://sun30.ris.beuth-hochschule.de:5601

Muss in ssh tunnel sein `ssh -L 5601:sun30.ris.beuth-hochschule.de:5601 sun31` . \
http://localhost:5601

Login: 
  - elastic
  - elastic

interessante attribute:
 - kubernetes.namespace_name
 - log
 - @timestamp

Beispiel queries:
 - kubernetes.namespace_name: "troeger"
 - kubernetes.namespace_name: "troeger" and log: "Runner listener exit with retryable error, re-launch runner in 5 seconds."
    - 332,325
 - kubernetes.namespace_name: "troeger" and kubernetes.host: "cl-worker26"
    - 1,212,547
 - kubernetes.*: "jupyterhub"
    - 2,246,016 
