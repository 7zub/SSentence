# -*- coding: cp1251 -*-
import os
from subprocess import call
from verb import *
import tkinter.messagebox as mb

dir = os.path.dirname(__file__) + '\TXT\\'

def open_words():
    call(['notepad', dir + r'words.txt'])

def open_articles():
    call(['notepad', dir + r'articles.txt'])
    
def exec_verb():
    try:
        verb()
        mb.showinfo('��������!', '��������� �������� � ���� out.txt')
        call(['notepad', dir + r'out.txt'])
    except Exception as e:
        mb.showerror('������!', '�� ������� ��������� �����: ' + str(e))


try:
    if not os.path.exists(dir):
        os.makedirs(dir)

    open(dir + r'words.txt', 'a').close()
    open(dir + r'articles.txt', 'a').close()
except:
    mb.showerror('������!', '�� ������� ������� ����� words.txt � articles.txt')
    exit(0)