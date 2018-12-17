set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
" Plugin 'scrooloose/nerdtree'
Plugin 'wycats/nerdtree'
Plugin 'flazz/vim-colorschemes'
Plugin 'glench/vim-jinja2-syntax'
Plugin 'gorodinskiy/vim-coloresque'
Plugin 'vim-airline/vim-airline'

call vundle#end()
filetype plugin indent on

:syntax on
:colorscheme jellybeans
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" Brief help
" :PluginList
" :PluginInstall | to update just :PluginUpdate
" :PluginSearch foo - searches for foo
" :PluginClean      - confirms removal of unused plugins

nnoremap <S-o> :syntax off<CR>
nnoremap <S-s> :syntax on<CR>
nnoremap <S-q> :colorscheme molokai<CR>
nnoremap <S-w> :colorscheme jellybeans<CR>
nnoremap <C-n> :NERDTree<CR>
