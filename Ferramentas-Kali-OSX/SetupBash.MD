# Install Bash 4 using homebrew
brew install bash

# Or build it from source...
curl -O http://ftp.gnu.org/gnu/bash/bash-4.2.tar.gz
tar xzf bash-4.2.tar.gz
cd bash-4.2
./configure --prefix=/usr/local/bin && make && sudo make install

# Add the new shell to the list of legit shells
sudo bash -c "echo /usr/local/bin/bash >> /private/etc/shells"

# Change the shell for the user
chsh -s /usr/local/bin/bash

# Restart terminal.app (new window works too)

# Check for Bash 4 and /usr/local/bin/bash...
echo $BASH && echo $BASH_VERSION