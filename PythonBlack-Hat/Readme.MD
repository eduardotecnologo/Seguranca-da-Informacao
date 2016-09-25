Não é necessário a utilização do Kali Linux para Técnicas de Invasão, um terminal UNIX é o suficiente se bem configurado, porém o Kali já nos fornece todas as ferramentas necessárias, mas utilizarei um MAC

Se voce deseja atualizar seu Kali 1.x para o Kali 2.0 o que voce tem a fazer e editar as entradas do seu arquivo source.list e executar um dist-upgrade como mostrado abaixo.


// adicionar entradas no seu source.list
cat << EOF > /etc/apt/sources.list
deb http://http.kali.org/kali sana main non-free contrib
deb http://security.kali.org/kali-security/ sana/updates main contrib non-free
EOF

Depois execute os seguintes comandos, prepare e tome seu cafe!!! 🙂
# apt-get update
# apt-get dist-upgrade
# reboot

Ou baixe a versão mais atual https://www.kali.org/news/kali-linux-rolling-edition-2016-1/

Atualização do python no MAC OS
https://www.python.org/downloads/mac-osx/

Módulo - Network Hacking
-Possibilita gerenciar todos dispositivos presentes na rede
-Para trabalhar com Network Hacking utilizamos o "Scapy", um poderoso Packet Tool para criação e manipulação de pacotes
----Instalação:
    ---Linux
    $sudo pip3 install scapy-python3
    ----Instalação:
    ---windows
    https://github.com/phaethon/scapy
Criando e Enviando Pacotes
-ip = IP(dst="192.168.0.1")       #Destino e informação no Header
-tcp = TCP(dport=80, flags="5")   #Porta de destino e informação no Header TCP
-pkt = ip/tcp                     #Assembly do Pacote tcp(TCP/IP PROT)
-send(pkt)                        #Enviar pacote
-sr(pkt)                          #Eviar e receber respostas
-sr1(pkt)                         #Enviar e receber apenas primeira resposta

Iniciando
Importando o Scapy
>>>from scapy.all import *