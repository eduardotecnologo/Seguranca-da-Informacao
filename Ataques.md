## * Tipos de Ataques.
* **WHOIS** (pronuncia-se "ruís" no Brasil) é um protocolo TCP (porta 43) específico para consultar informações de contato e **DNS** sobre entidades na internet.
* Uma entidade na internet pode ser um nome de domínio, um endereço IP ou um AS (Sistema Autônomo).
* O protocolo **WHOIS** apresenta três tipos de contatos para uma entidade: Contato Administrativo (Admin Contact), Contato Técnico (Technical Contact) e Contato de Cobrança (Registrant Contact). Estes contatos são informações de responsabilidade do provedor de internet, que as nomeia de acordo com as políticas internas de sua rede.
* Vale lembrar que outras empresas internacionais ainda podem ter um recurso de travar essas informações para as pessoas, chamado de **Whois privado.**
**## Comando host**
* Esse comando pode ser usado para obter o endereço IP de um domínio e vice-versa. Este comando é muito útil durante a depuração de problemas de rede.
* Aqui estão alguns exemplos de uso deste comando:
* Buscar informações relacionadas com o endereço IP de um domínio, simplesmente usando o domínio como argumento para o comando host.
* $ host google.com
* google.com has address 74.125.236.72
* google.com has address 74.125.236.78
## **Comando arch**
* Este comando é usado para saber a arquitetura de hardware do sistema.
* Aqui está o resultado deste comando na minha máquina:
* $ arch
* x86_64
* Então, isso significa que a minha máquina tem 64 bit e é da série de processadores x86 . Este comando tem a mesma saída do comando uname-m (que discutiremos mais tarde).
