#find default setup here: /usr/share/zsh/manjaro-zsh-config

# Use powerline
USE_POWERLINE="true"
# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi
# Use manjaro zsh prompt
if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
  source /usr/share/zsh/manjaro-zsh-prompt
fi
source /usr/share/nvm/init-nvm.sh
source /usr/share/nvm/init-nvm.sh

########## < Felix start > ################################################
# to install plugins use: antidote install {github_username/github_repo_name}

# source antidote
source ${ZDOTDIR:-~}/.antidote/antidote.zsh
# initialize plugins statically with ${ZDOTDIR:-~}/.zsh_plugins.txt
antidote load


# aliases
alias dcu='docker compose up --build'
alias dcd='docker compose down'
alias c='clear'
alias x='exit'
alias reload='source ~/.zshrc'
alias -g L='| less' # a suffix alias to pipe output through less 
alias config='/usr/bin/git --git-dir=$HOME/.cfg/.git/ --work-tree=$HOME' # alias for git when it comes to the dotfile repo .cfg

# git add commit push - will add all files and push the current changes with given message
function gacp() {
  str="'$*'"
  git add .
  git commit -m "${str:1:${#str}-2}"
  git push
}

# git commit push - will push the current staged files with given message
function gcp() {
  str="'$*'"
  git commit -m "${str:1:${#str}-2}"
  git push
}


path+=("/home/felixk/.local/share/JetBrains/Toolbox/scripts/")
path+=("/home/felixk/.local/share/JetBrains/Toolbox/bin/")


##########  </ Felix end >  ###############################################
