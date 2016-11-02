**Install crunch on Mac OSX**
* About the App

    App name: crunch
    App description: Wordlist generator
    App website: http://sourceforge.net/projects/crunch-wordlist

**Install the App**

* Press Command+Space and type Terminal and press enter/return key.
* Run in Terminal app:

-> ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
* and press enter/return key. Wait for the command to finish.
**Run:**

-> brew install crunch

Done! You can now use crunch.

**Como usar:**

* Execute "crunch" no terminal:�(Estou executando dentro da minha pasta "Tecnicas-de-invasao" , mas pode ser em qualquer lugar)

➜  Tecnicas-de-invasao git:(master) ✗ crunch

crunch version 3.6

Crunch can create a wordlist based on criteria you specify.  The outout from crunch can be sent to the screen, file, or to another program.

Usage: crunch <min> <max> [options]
where min and max are numbers

Please refer to the man page for instructions and examples on how to use crunch.

➜  Tecnicas-de-invasao git:(master) ✗crunch 0 4 0123456789 -o /Users/eduardodeveloper/Documents/Developer/GITHUB/Tecnicas-de-invasao/Ferramentas-Kali-OSX/WordList/wordlist2.txt

Crunch will now generate the following amount of data: 3710 bytes

0 MB

0 GB

0 TB

0 PB

Crunch will now generate the following number of lines: 780

crunch: 100% completed generating output

➜  Tecnicas-de-invasao git:(master) ✗

**Obs:**
* 0 4 = Isso seta combinações de 5 caracteres, de 0 a 9 ("20316")
* 0123456789 = Isso seta os tipos de caracteres, nesse caso possibilidades combinando numeros de 0 a 9
* -o / = Seta o local a ser salvo o .txt com as combinações
* Em caso de letras podemos usar:
**Combinação de 8 caracteres ou mais**

➜  Tecnicas-de-invasao git:(master) ✗ crunch 0 8 abcdefgh -o /local

* Misturando caracteres (Continua......)
