Helpers Linux
Matar processo em portas:
$ apt-get install net-tools
$ lsof -w -n -i tcp:8080

$ fuser -n tcp 8080

$ netstat -anp | grep :8080

E para matar o processo é só utilizar o comando kill

$ kill -9 pid

Até a próxima
