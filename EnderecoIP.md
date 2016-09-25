Endereço IP, de forma genérica, é uma identificação de um dispositivo (computador, impressora, etc) 
em uma rede local ou pública. Cada computador na internet possui um IP (Internet Protocol ou Protocolo de internet) 
único, que é o meio em que as máquinas usam para se comunicarem na Internet.

* Endereço IP, de forma genérica, é uma identificação de um dispositivo (computador, impressora, etc) 
em uma rede local ou pública. Cada computador na internet possui um IP (Internet Protocol ou Protocolo de internet)único, que é o meio em que as máquinas usam para se comunicarem na Internet.
Formato do Cabeçalho do IPv4

*     Versão - o primeiro campo do cabeçalho de um datagrama IPv4 é o campo de versão, com quatro bits.
*     Tamanho do cabeçalho (IHL) - o segundo campo, de quatro bits, é o IHL (acrónimo para Internet Header Length, ou seja, Comprimento do Cabeçalho da Internet) com o número de palavras de 32 bits no cabeçalho IPv4. Como o cabeçalho IPv4 pode conter um número variável de opções, este campo essencialmente especifica o offset para a porção de dados de um datagrama IPv4. Um cabeçalho mínimo tem vinte bytes de comprimento, logo o valor mínimo em decimal no campo IHL seria cinco.

## Funcionamento
* Os dados numa rede IP que são enviados em blocos referidos como ficheiros (os termos são basicamente sinónimos no IP, sendo usados para os dados em diferentes locais nas camadas IP). Em particular, no IP nenhuma definição é necessária antes do nó tentar enviar ficheiros para um nó com o qual não comunicou previamente.

* O IP oferece um serviço de datagramas não confiável (também chamado de melhor esforço); ou seja, o pacote vem quase sem garantias. O pacote pode chegar desordenado (comparado com outros pacotes enviados entre os mesmos nós), também podem chegar duplicados, ou podem ser perdidos por inteiro. Se a aplicação requer maior confiabilidade, esta é adicionada na camada de transporte.

* 1. Os roteadores são usados para reencaminhar datagramas IP através das redes interconectadas na segunda camada. A falta de qualquer garantia de entrega significa que o desenho da troca de pacotes é feito de forma mais simplificada. (Note que se a rede cai, reordena ou de outra forma danifica um grande número de pacotes, o desempenho observado pelo utilizador será pobre, logo a maioria dos elementos de rede tentam arduamente não fazer este tipo de coisas - melhor esforço. Contudo, um erro ocasional não irá produzir nenhum efeito notável.)

* 1. O IP é o elemento comum encontrado na Internet pública dos dias de hoje. É descrito no RFC 791 da IETF, que foi pela primeira vez publicado em Setembro de 1981. Este documento descreve o protocolo da camada de rede mais popular e atualmente em uso. Esta versão do protocolo é designada de versão 4, ou IPv4. O IPv6 tem endereçamento de origem e destino de 128 bits, oferecendo mais endereçamentos que os 32 bits do IPv4.

## Endereçamento IPv4 e encaminhamento

* Talvez os aspectos mais complexos do IP sejam o endereçamento e o encaminhamento. O endereçamento define como os endereços IP dos nós finais são atribuídos e como as subredes dos endereços de IP dos nós são divididos e agrupados. O encaminhamento IP é feito por todos os nós, mas mais comumente por roteadores de rede, que tipicamente usam os protocolos IGP ou EGP para ajudar na leitura de datagramas IP que reencaminhem decisões através de IPs em redes ligadas.

* Na internet, e nas redes particulares que vemos hoje nas empresas ou mesmo nas residências, o protocolo de comunicação usado pelos computadores chama-se IP - sigla para Internet Protocol. Criado no fim dos anos 70, o protocolo IP tem como "missão" não só fazer dois computadores "conversarem", mas também possibilitar a interligação de duas ou mais redes separadas. Com raríssimas exceções, praticamente todas as redes do mundo acabaram, de uma forma ou de outra, sendo conectadas entre si e foi essa comunhão de redes que acabou formando o que conhecemos hoje por internet (nome que, em português, pode ser traduzido por "inter-redes" ou "redes interligadas").

* TCP/IP
* IP: 32 Bits V4
* 00000000 | 00000000 | 00000000 | 00000000 |
*     0          0          0          0
*     |          |          |          |
*    255        255        255        255
* Exemplo de IPs **reservados** usados em redes internas (192.168.0.1),são IPs "Não Rotiáveis",exclusivos para usos privados.
* Com o objectivo de serem possíveis redes de diferentes dimensões, foram definidas cinco diferentes classes de endereços IP (Classes: A, B, C, D e E).

* A classe A possui um conjunto de endereços que vão desde o 1.0.0.0 até 127.0.0.0, onde o primeiro octeto (primeiros 8 bits N.H.H.H) de um endereço IP identifica  a rede e os restantes 3 octetos ( 24 bits) irão identificar um determinado host nessa rede.

*     **Exemplo de um endereço Classe** A – 120.2.1.0
de 10.0.0.1 -> 10.255.255.25

* A classe B possui um conjunto de endereços que vão desde o 128.0.0.0 até 191.255.0.0, onde os dois primeiros octetos (16 bits N.N.H.H) de um endereço IP identificam  a rede e os restantes 2 octetos ( 16 bits) irão identificar um determinado host nessa rede.

*     **Exemplo de um endereço Classe** B – 152.13.4.0
de 172.16.0.0 -> 172.31.255.255

* A classe C possui um conjunto de endereços que vão desde o 192.0.0.0 até 223.255.255.0, onde os três primeiros octetos (24 bits N.N.N.H) de um endereço IP identificam  a rede e o restante octeto ( 8 bits) irão identificar um determinado host nessa rede.

*     **Exemplo de um endereço Classe** C – 192.168.10.0
de 192.168.0.0 -> 192.168.255.255

