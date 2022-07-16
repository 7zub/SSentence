# -*- coding: cp1251 -*-
import os
import pathlib
from subprocess import call
from verb import *
import tkinter.messagebox as mb

dir = str(pathlib.Path.cwd()) + '\TXT\\'

def open_words():
    print(dir)
    call(['notepad', dir + r'words.txt'])

def open_articles():
    call(['notepad', dir + r'articles.txt'])
    
def exec_verb():
    try:
        verb()
        mb.showinfo('Выполено!', 'Результат сохранен в файл out.txt')
        call(['notepad', dir + r'out.txt'])
    except Exception as e:
        mb.showerror('Ошибка!', 'Не удалось выполнить поиск: ' + str(e))


try:
    if not os.path.exists(dir):
        os.makedirs(dir)

    open(dir + r'words.txt', 'a').close()
    open(dir + r'articles.txt', 'a').close()
except:
    mb.showerror('Ошибка!', 'Не удалось создать файлы words.txt и articles.txt')
    exit(0)