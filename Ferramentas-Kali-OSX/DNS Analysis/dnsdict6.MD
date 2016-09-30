O **dnsdict6** é um utilitário usado para enumerar um domínio para as entradas de DNS IPv6. Sendo útil para encontrar sub-domínios que podem ser invisíveis para o público, mas ainda existem nos registros DNS. Muitas vezes, estes domínios esquecidos estão desatualizados e podem ser um vetor para explorar ataques contra o domínio. dnsdict6 usa uma lista/dicionário que é usado para adivinhar possíveis entradas de DNS.

* App name: dnsmap 
* App description: Passive DNS network mapper (a.k.a. subdomains bruteforcer) 
* App website: Not Available 
*** Install the App**

Press Command+Space and type Terminal and press enter/return key. Run in Terminal app: 
->ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null 

And press enter/return key. Wait for the command to finish. Run: 
->brew install dnsmap 

**Done! You can now use dnsmap.**

**Run **

->dnsmap
