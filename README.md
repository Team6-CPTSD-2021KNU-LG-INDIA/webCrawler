# webCrawler
develop python web crawling services

> At linux, Python 3.8, pip, google-chrome 92 ver installation are required!!!
> 
> Install python packages

### 1. make python virtual env  
> python -m venv virtual environment name(가상환경이름)  

### 2. activate python virtual env  
> source virtual environment name(가상환경이름)/bin/activate

### 3. install python package pip
> pip install -r requirements.txt

### using windows WSL,  
> 1. install google-chrome for selenium  
> sudo apt install ./google-chrome-stable_current_amd64.deb  
> 2. install VcXsrv Windows X Server at windows and execute
> https://sourceforge.net/projects/vcxsrv/
> 3. at wsl shell, modify shell rc file
> ex) zsh ->  
> vi ~/.zshrc  
> add  
> export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0"  
> export LIBGL_ALWAYS_INDIRECT=1
