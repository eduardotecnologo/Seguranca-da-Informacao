## * Erro na inicializacao do Apache2
*ERROR: Failed to start apache2.service: Unit apache2.service not found. 

**## * Solucao**
* sudo apt-get -o DPkg::Options::="--force-confmiss" --reinstall install apache2
**## * Para remover completamente os arquivos de configuração apache2, você deve:**
* sudo apt-get purge apache2
**## * Para reinstalar:**
* sudo apt-get install apache2
