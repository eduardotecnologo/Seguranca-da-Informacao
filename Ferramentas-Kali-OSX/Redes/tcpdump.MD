Tcpdump é o sniffer de rede utilizado pela linha de comando. Seu “concorrente” gráfico é o Wireshark. Mesmo assim, muitos continuam a usá-lo com frequência pela flexibilidade da linha de comando. Pode não ter os recursos gráficos e suporte a diversos protocolos como o Wireshark, mas o tcpdump faz bem seu trabalho com menos recursos computacionais.

Capturar o rastreamento de pacote

Abra o Terminal que está na pasta Utilitários da pasta Aplicativos.
Digite o comando a seguir, mas substitua BSDname pelo nome do dispositivo BSD (como en0, en1 ou ppp0) nas Informações do Sistema: 

sudo tcpdump -i BSDname -s 0 -B 524288 -w ~/Desktop/DumpFile01.pcap

Pressione Return e insira a senha de administrador quando for solicitada.
O Terminal deve exibir tcpdump: listening on... para indicar que está atento a uma atividade na interface de rede.
Enquanto o Terminal estiver aberto, execute a função de rede que deseja testar.
Quando a função de rede for concluída, retorne ao Terminal e pressione Control + C para capturar o rastreamento de pacote. O Terminal o salva na sua área de trabalho em um arquivo chamado "DumpFile01.pcap". 
Para ver o conteúdo do arquivo, use este comando no Terminal:

tcpdump -s 0 -n -e -x -vvv -r ~/Desktop/DumpFile01.pcap

Para capturar rastreamentos de pacotes adicionais, modifique o comando do Terminal para incrementar o número do arquivo salvo (DumpFile02.pcap, DumpFile03.pcap e assim por diante).