
* Gateway, ou ponte de ligação, é uma máquina intermediária geralmente destinada a interligar redes, separar domínios de colisão, ou mesmo traduzir protocolos. Exemplos de gateway podem ser os routers (ou roteadores) e firewalls, já que ambos servem de intermediários entre o utilizador e a rede. Um proxy também pode ser interpretado como um gateway (embora em outro nível, aquele da camada em que opera), já que serve de intermediário também.

* Depreende-se assim que o gateway tenha acesso ao exterior por meio de linhas de transmissão de maior débito, para que não constitua um estrangulamento entre a rede exterior e a rede local. E, neste ponto de vista, estará dotado também de medidas de segurança contra invasões externas, como a utilização de protocolos codificados.

* Cabe igualmente ao gateway traduzir e adaptar os pacotes originários da rede local para que estes possam atingir o destinatário, mas também traduzir as respostas e devolvê-las ao par local da comunicação. Assim, é frequente a utilização de protocolos de tradução de endereços, como o NAT — que é uma das implementações de gateway mais simples.

* Gateways habilitam a comunicação entre diferentes arquiteturas e ambientes. Ele realiza a conversão dos dados de um ambiente para o outro de modo que cada ambiente seja capaz de entender os dados. Eles podem ainda mudar o formato de uma mensagem de forma que ela fique de acordo com o que é exigido pela aplicação que estará recebendo esses dados. Por exemplo, um gateway pode receber as mensagens em um formato de rede e traduzi-las e encaminha-las no formato de rede usado pelo receptor. Um gateway liga dois sistemas que não usam:

* » Os mesmos protocolos de comunicação.

* » A mesma estrutura de formatação de dados.

* » A mesma linguagem.

* » A mesma arquitetura de rede.

* Gateways são referenciados pelo nome das tarefas especificas que eles desempenham, ou seja são dedicados a um tipo de transferência particular.

* O gateway pega o dado de um ambiente retira a pilha de protocolos antiga e reencapsula com a pilha de protocolos da rede destino.

* Note-se, porém, que o gateway opera em camadas baixas do Modelo OSI e que não pode, por isso, interpretar os dados entre aplicações (camadas superiores). No entanto, por meio do uso de heurísticas e outros métodos de detecção de ataques, o gateway pode incorporar alguns mecanismos de defesa. Esta funcionalidade pode ser complementada com um firewall.
