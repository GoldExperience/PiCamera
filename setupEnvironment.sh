#!/bin/sh

# install git
sudo apt-get update
sudo apt-get install git

# install berryconda(link: https://github.com/jjhelmus/berryconda)
wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv6l.sh
chmod +x Berryconda3-2.0.0-Linux-armv6l.sh
./Berryconda3-2.0.0-Linux-armv6l.sh

# (Optional) setup zsh & oh-my-zsh(https://github.com/ohmyzsh/ohmyzsh) 
sudo apt-get install zsh
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
# then edit ~/.zshrc 'plugins=(zsh-autosuggestions)'

# activate berryconda base environment
echo '. /home/pi/berryconda3/etc/profile.d/conda.sh' >> .zshrc
echo 'conda activate base' >> .zshrc
zsh

# install Libraries
conda install -y -c menpo opencv
conda install -y flask 
pip install -y flask-uploads



