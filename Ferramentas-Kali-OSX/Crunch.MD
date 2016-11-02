
**Install crunch on Mac OSX**
**About the App**

* App name: crunch
* App description: Wordlist generator
* App website: http://sourceforge.net/projects/crunch-wordlist

* Install the App

**Press Command+Space and type Terminal and press enter/return key.**
* Run in Terminal app:

    -> ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null

* and press enter/return key. Wait for the command to finish.
**Run:**

    ->brew install crunch

**Done! You can now use crunch.**

**Como usar:**

* Estou na pasta "Tecnicas-de-invasao", mas execute de onde quizer.

➜  Tecnicas-de-invasao git:(master) crunch

crunch version 3.6

Crunch can create a wordlist based on criteria you specify.  The outout from crunch can be sent to the screen, file, or to another program.

Usage: crunch <min> <max> [options]
where min and max are numbers

Please refer to the man page for instructions and examples on how to use crunch.

➜  Tecnicas-de-invasao git:(master)crunch 1 4 0123456789 -o /Users/eduardodeveloper/Documents/Developer/GITHUB/Tecnicas-de-invasao/WordList/wordlist1.txt **=>(Caminho onde será salvo a WordList Criada)**


Crunch will now generate the following amount of data: 54320 bytes
0 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 11110

crunch: 100% completed generating output
➜  Tecnicas-de-invasao git:(master) ✗


**Obs.**
* 1 4 (Lista com combinação de 1 a 4 caracteres como **"0123"** usando numeros de 0 a 9, você configura o tamanho desejado, no caso de letras é só setar a quantidade de caracteres como **"01234567"** um exemplo de 8, e **"abcdefgh"** até onde desejar���)

