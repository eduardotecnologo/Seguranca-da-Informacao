## * Tipos de Consultas.(Kali Linux)
* **WHOIS** (pronuncia-se "ruís" no Brasil) é um protocolo TCP (porta 43) específico para consultar informações de contato e **DNS** sobre entidades na internet.
* Uma entidade na internet pode ser um nome de domínio, um endereço IP ou um AS (Sistema Autônomo).
* O protocolo **WHOIS** apresenta três tipos de contatos para uma entidade: Contato Administrativo (Admin Contact), Contato Técnico (Technical Contact) e Contato de Cobrança (Registrant Contact). Estes contatos são informações de responsabilidade do provedor de internet, que as nomeia de acordo com as políticas internas de sua rede.
* Vale lembrar que outras empresas internacionais ainda podem ter um recurso de travar essas informações para as pessoas, chamado de **Whois privado.**
* Instalação: apt-get install whois

* ## **Comando host**
* Esse comando pode ser usado para obter o endereço IP de um domínio e vice-versa. Este comando é muito útil durante a depuração de problemas de rede.
* Aqui estão alguns exemplos de uso deste comando:
* Buscar informações relacionadas com o endereço IP de um domínio, simplesmente usando o domínio como argumento para o comando host.
* $ host google.com
* google.com has address 74.125.236.72
* google.com has address 74.125.236.78
* ## **Comando arch**
* Este comando é usado para saber a arquitetura de hardware do sistema.
* Aqui está o resultado deste comando na minha máquina:
* $ arch
* x86_64
* Então, isso significa que a minha máquina tem 64 bit e é da série de processadores x86 . Este comando tem a mesma saída do comando uname-m (que discutiremos mais tarde).
* ## **Netcraft**
**Netcraft** é uma empresa de serviços de Internet sediada em Bath, Inglaterra.
**Netcraft** oferece análise de quota de mercado para mercados de hospedagem de sites e de servidores web, incluindo detecção do sistema operacional e do servidor web. Em alguns casos, dependendo do sistema operacional do servidor consultado, o serviço é capaz de controlar **uptimes**;o acompanhamento do desempenho do **uptime** é comumente utilizado como fator de determinação da confiabilidade de um provedor de hospedagem na Web.
A **Netcraft** também oferece testes de segurança, e publica notícias sobre o estado das diversas redes que compõem a Internet.
É conhecida também por sua barra de ferramentas anti-phishing para os navegadores Firefox e o Internet Explorer. A partir da versão 9.5, a base de filtro anti-phishing do navegador Opera utiliza os mesmos dados, como a barra de ferramentas do Netcraft, eliminando a necessidade de uma barra instalada separadamente. Um estudo encomendado pela Microsoft elegeu a barra de ferramentas do Netcraft como um dos instrumentos mais eficazes para combater o phishing na Internet, embora esta posição tenha sido conquistada pelo Internet Explorer 7 com filtro de phishing da Microsoft, possivelmente como resultado da concessão de licenças de dados da **Netcraft**.

* ## **Archive**
* Ferramenta WEB utilizada saber de dados antigos de qualquer empresa WEB, ótima ferramenta para coolher mais informações de um suposto ALVO.
* http://archive.org/web/
