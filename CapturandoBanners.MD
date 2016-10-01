## Capturando Banners

*** Terminal do MAC**

*** 10.0.0.16(IP Metasploitable)**

➜ Tecnicas-de-invasao git:(master) ✗ ftp 10.0.0.16 Connected to 10.0.0.16. 220 (vsFTPd 2.3.4) Name (10.0.0.16:eduardodeveloper):

*** Setar uma requisição telnet para 4linux na port 25**

➜ Tecnicas-de-invasao git:(master) ✗ telnet 4linux.com.br 25 Trying 107.23.128.206... Connected to 4linux.com.br. Escape character is '^]'. 220 webserver.4linux.com.br ESMTP Postfix (Ubuntu)

*** NMAP, inumeração de Serviços (Teste realizado no ip do Metasploitable)**

*** -sV = Mostra as versões de serviços sendo rodados -O = Captura e identifica o Sistema Operacional**

➜ Tecnicas-de-invasao git:(master) ✗ nmap -sV -O 10.0.0.16 

TCP/IP fingerprinting (for OS scan) requires root privileges. QUITTING! 

➜ Tecnicas-de-invasao git:(master) ✗ sudo nmap -sV -O 10.0.0.16 Password:


Starting Nmap 7.25BETA2 ( https://nmap.org ) at 2016-10-01 12:51 BRT Nmap scan report for 10.0.0.16 

Host is up (0.00039s latency). 

Not shown: 977 closed ports 

PORT STATE SERVICE VERSION 

21/tcp open ftp vsftpd 2.3.4 

22/tcp open ssh OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0) 
23/tcp open telnet Linux telnetd 25/tcp open smtp Postfix smtpd 
53/tcp open domain ISC BIND 9.4.2 
80/tcp open http Apache httpd 2.2.8 ((Ubuntu) DAV/2) 
111/tcp open rpcbind 2 (RPC #100000) 
139/tcp open netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP) 
445/tcp open netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP) 
512/tcp open exec netkit-rsh rexecd 
513/tcp open login 
514/tcp open tcpwrapped 
1099/tcp open rmiregistry GNU Classpath grmiregistry 
1524/tcp open shell Metasploitable root shell 
2049/tcp open nfs 2-4 (RPC #100003) 
2121/tcp open ftp ProFTPD 1.3.1 
3306/tcp open mysql MySQL 5.0.51a-3ubuntu5 
5432/tcp open postgresql PostgreSQL DB 8.3.0 - 8.3.7 
5900/tcp open vnc VNC (protocol 3.3) 
6000/tcp open X11 (access denied) 
6667/tcp open irc Unreal ircd
8009/tcp open ajp13 Apache Jserv (Protocol v1.3) 
8180/tcp open http Apache Tomcat/Coyote JSP engine 1.1 
MAC Address: 08:00:27:4E:25:19 (Oracle VirtualBox virtual NIC) 
Device type: general purpose 
Running: Linux 2.6.X 
OS CPE: cpe:/o:linux:linux_kernel:2.6 OS details: Linux 2.6.9 - 2.6.33 
Network Distance: 1 hop 
Service Info: Hosts: metasploitable.localdomain, localhost, irc.Metasploitable.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 16.37 seconds 

➜ Tecnicas-de-invasao git:(master) ✗

*** Utilizando o XPROBE2 no terminal do Kali Linux**

root@kai:˜# xprobe2 -h (Abrir o Help)

*** -T = Enable TCP portscan for especified port(s) **
*** -A Perform analysis of samlpe packets gethered during portscan....**

**EXEMPLO** 

root@kai:˜# xprobe2 -A -T 80 4linux.com.br

AMAP 

➜ Tecnicas-de-invasao git:(master) ✗ amap 10.0.0.16 80 

amap v5.4 (www.thc.org/thc-amap) started at 2016-10-01 13:22:12 - APPLICATION MAPPING mode

Protocol on 10.0.0.16:80/tcp matches http Protocol on 10.0.0.16:80/tcp matches http-apache-2

Unidentified ports: none.

amap v5.4 finished at 2016-10-01 13:22:18 

➜ Tecnicas-de-invasao git:(master) ✗
