# -*- coding: cp1251 -*-
from tkinter import RIGHT, Button, Tk, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label
from event import *

class Main(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title('Поиск предложений')
        self.pack(fill=BOTH, expand=True)
 
        frame1 = Frame(self)
        frame1.pack(fill=X)
 
        lbl1 = Label(frame1, text='Введите слова(фразы), которые нужно найти (1 на строку):')
        lbl1.pack(side=LEFT, padx=5, pady=5)

        btn_w = Button(frame1, text='words.txt', command=open_words)
        btn_w.pack(side=LEFT, padx=5, pady=5)
 
        frame2 = Frame(self)
        frame2.pack(fill=X)
 
        lbl2 = Label(frame2, text='Вставьте тексты стетей (разделитель статей "###")')
        lbl2.pack(side=LEFT, padx=5, pady=5)

        btn_w = Button(frame2, text='articles.txt', command=open_articles)
        btn_w.pack(side=LEFT, padx=5, pady=5)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btn_search = Button(frame3, text='Искать!', command=exec_verb)
        btn_search.pack(side=LEFT, padx=5, pady=5)

def main():
    root = Tk()
    root.geometry('540x300+300+300')
    app = Main()
    root.mainloop()

if __name__ == '__main__':
    main()