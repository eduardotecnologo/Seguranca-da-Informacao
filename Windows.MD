## Métodos para alterar a senha de um ADM via CMD no Windows10

* 1 - Insira o CD do Windows10,8.1, 7 ou um Live CD HirensBoot
* 2 - Inicie a instalação do Sistema até a tela de "Repar o Computador", vá em "Opções Avançadas", "Soluções de Problemas", "Opções Avançadas" e "Pronpt de Comandos".

* Digite "DISKPART" para entrar em um utilitários de unidades e "LIST VOL", para identificar em qual unidade está instalado o Windows, e siga os passos.Nesse exemplo o sistema se encontra na unidade C:.
* **## Comandos Parte I **
**## Entre em : **
* C:
* cd windows
* cd system32
* **Digite:**
* copy cmd.exe cmd.exe.original
* copy Utilman.exe Utilman.exe.original
* del Utilman.exe
* ren cmd.exe Utilman.exe
* Exit

* Agora reinicie o sistema e clique no ícone entre o "**Redes e Power**", como os comandos anteriores ele irá abrir o CMD e siga os seguintes passos.

* **## Comandos Parte II**
* Net user (Irá listar os Usuários)
* Net user seu + usuario *(Irá pedir uma nova senha, digite ou deixe em branco)
* Exit
*** Comandos Parte III (Agora desfaz essas mudanças para que o sistema não fique vulnerável)**
* C:
* cd windows
* cd system32
* del Utilman.exe
* ren Utilman.exe.original Utilman.exe
* ren cmd.exe.original cmd.exe
* Exit

## Métodos para criar um ADM via CMD no Windows10
* 1 - Insira o CD do Windows10,8.1, 7 ou um Live CD HirensBoot
* 2 - Inicie a instalação do Sistema até a tela de "Repar o Computador", vá em "Opções Avançadas", "Soluções de Problemas", "Opções Avançadas" e "Pronpt de Comandos".
* **Digite:**
* NET USER "NovoUser" /ADD (Sem aspas)
* NET LOCALGROUP ADMINISTRADORES "NovoUser" /ADD (Define as permissões de ADM)
* exit
* Reinicie o computador e seja feliz.
