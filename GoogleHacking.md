## *** Exemplos**
*** google hacking database;**
* https://www.exploit-db.com/google-hacking-database/
* https://www.offensive-security.com/community-projects/google-hacking-database/

*  Comandos Avançados do Google (OPERADORES)
*  **intitle, allintitle**

* Busca conteúdo no título (tag title) da página.
* Quando utilizamos o comando intitle, é importante prestar atenção à sintaxe
* da string de busca, posto que a palavra que segue logo após o comando intitle é considerada como a string de busca. O comando allintitle quebra essa regra, dizendo ao Google que todas as palavras que seguem devem ser encontradas no title da página, por isso, esse último comando é mais restritivo.

* **inurl, allinurl**

* **Encontra texto em uma URL.**
* Como explicado no operador intitle, pode parecer uma tarefa relativamente  simples utilizar o operador inurl sem dar maior atenção ao mesmo. Mas devemos ter em mente que uma URL é mais complicada do que um simples title, e o funcionamento do operador inurl pode ser igualmente complexo.
* Assim como o operador intitle, inurl também possui um operador companheiro, que é o allinurl, que funciona de maneira idêntica e de forma restritiva, exibindo resultados apenas em que todas as strings foram encontradas.

* **Filetype**
* **Busca por um arquivo de determinado tipo.**
* O Google pesquisa mais do que apenas páginas web. É possível pesquisar muitos tipos diferentes de arquivos, incluindo PDF (Adobe Portable Document Format) e Microsoft Office. O operador filetype pode ajudá-lo na busca de tipo de arquivos específicos. Mais especificamente, podemos utilizar esse operador para pesquisas de páginas que terminam em uma determinada extensão.

*  **Allintext**
* Localiza uma string dentro do texto de uma página.
* O operador allintext é talvez o mais simples de usar, pois realiza a função de busca mais conhecida como: localize o termo no texto da página.
* Embora este operador possa parecer genérico para ser utilizado, é de grande ajuda quando sabe que a string de busca apenas poderá ser encontrada no texto da página. Utilizar o operador allintext também pode servir como um atalho para "encontrar esta string em qualquer lugar, exceto no title, URL e links".

*  **Site**
* Direciona a pesquisa para o conteúdo de um determinado site.
* Apesar de ser tecnicamente uma parte da URL, o endereço (ou nome de domínio) de um servidor pode ser mais bem pesquisada com o operador site. Site permite que você procure apenas as páginas que estão hospedadas em um servidor ou domínio específico.

* **Link**
* Busca por links para uma determinada página.
* Em vez de fornecer um termo de pesquisa, o operador necessita de um link URL ou nome do servidor como um argumento.

*  **Inanchor**
* Localiza texto dentro de uma âncora de texto.
* Este operador pode ser considerado um companheiro para o operador link, uma vez que ambos buscam links. O operado inanchor, no entanto, pesquisa a representação de texto de um link, não o URL atual.
* Inanchor aceita uma palavra ou expressão como argumento, como inanchor:click ou inanchor:oys. Este tipo de pesquisa será útil especialmente quando começamos a estudar formas de buscar relações entre sites.

* **Daterange**
* Busca por páginas publicadas dentro de um “range” de datas.
* Você pode usar este operador para localizar páginas indexadas pelo Google em um determinado intervalo de datas. Toda vez que o Google rastreia uma página, a data em sua base de dados é alterada. Se o Google localizar alguma página Web obscura, pode acontecer de indexá-la apenas uma vez e nunca retornar à ela.
* Se você achar que suas pesquisas estão entupidas com esses tipos de páginas obscuras, você pode removê-las de sua pesquisa (e obter resultados mais atualizados) através do uso eficaz do operador daterange.
* Lembrando que a data deve ser informada no formato do calendário Juliano, informando o número de dias existentes entre 4713 AC e a data em que se quer buscar.

* **Cachê**
* Mostra a versão em cache de uma determinada página.
* Como já discutimos, o Google mantém "snapshots" de páginas que indexou e que podemos acessar através do link em cache na página de resultados de busca. Se quiser ir direto para a versão em cache de uma página, sem antes fazer uma consulta ao Google para chegar ao link em cache na página de resultados, você pode simplesmente usar o operador cache em uma consulta, como cache:blackhat.com ou cache:www.netsec.net/content/index.jsp.

*  **Info**
* Mostra conteúdo existente no sumário de informações do Google.
* O operador info mostra o resumo das informações de um site e fornece links para outras pesquisas do Google que podem pertencer a este site. O parâmetro informado à este operador, deve ser uma URL válida.

* **Listando SubDominios**
* ➢ site:* .globo.com

*** Exemplos**

*** Busca por arquivos de base de dados em sites do governo:**

* ➢ site:gov.br ext:SQL

* **Busca por um servidor específico**

* ➢ inurl:"powered by" site:sistema.com.br

* **A pesquisa busca arquivos de e-mail em formato .mdb**

* ➢ inurl:e-mail filetype:mdb

*** Essa pesquisa busca telefones disponíveis em intranet encontradas pelo Google**

* ➢ inurl:intranet + intext:"telefone"

* **Realizando uma pesquisa dessa maneira é possível identificar muitos dos subdomínios da Oracle**

* ➢ site:oracle.com -site:www.oracle.com

* **Detectando sistemas que usando a porta 8080**

* ➢ inurl:8080 -intext:8080

* **Encontrando VNC**

* intitle:VNC inurl:5800 intitle:VNC

* **Encontrando VNC**

* ➢ intitle:"VNC Viewer for Java"

* **Encontrando Webcam ativa**

* ➢ "Active Webcam Page" inurl:8080

* **Encontrando Webcam da toshiba:**

* ➢ intitle:"toshiba network camera - User Login"

* **Encontrando Apache 1.3.20:**

* ➢ "Apache/1.3.20 server at" intitle:index.of

* **Asterisk VOIP Flash Interface**

* ➢ intitle:"Flash Operator Panel" -ext:php -wiki -cms -inurl:as

* **Possíveis falhas em aplicações web:**

* ➢ allinurl:".php?site="
* ➢ allinurl:".php?do="
* ➢ allinurl:".php?content="
* ➢ allinurl:".php?meio="
* ➢ allinurl:".php?produto="
* ➢ allinurl:".php?cat="


* **Google Hacking Database**

* Há um banco de dados virtual, com tags de busca no Google previamente criadas, para conseguir informações específicas. A partir das tags existentes, podemos encontrar muitas coisas interessantes sem precisarmos nos preocupar em como desenvolver buscas específicas, utilizando os operadores do Google, e testá-las até conseguirmos que os filtros corretos funcionem. Mas o mais importante que devemos manter em mente, é a possibilidade e adaptar tais tags de busca para nossas necessidades.

