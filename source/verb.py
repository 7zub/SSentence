import os
import re

dir = os.path.dirname(__file__) + '\TXT\\'

def verb():
    words = open(dir + r'words.txt', 'r').read().splitlines()
    arts = open(dir + r'articles.txt', 'r').read().split('###')
    out_file = open(dir + r'out.txt', 'w')

    out_words = dict()
    for w in words:
        out_words[w] = ''

    for i_art, art in enumerate(arts):
        art = re.split(r'(?<=[.!?;])', art)
        
        for word in words:
            for i_sen, sen in enumerate(art):
                search_word = re.search(r'\b' + word.lower(), sen.lower())

                if search_word != None and out_words[word] in ('','--'):
                    out_sen = re.sub(r'\[[^\]]+\]', '', sen).replace('  ', ' ').replace(' .', '.').replace('\n', '').strip()
                    out_words[word] = (out_sen + ';[' + str(i_art+1) + ':' + str(i_sen+1) + ']').replace(';;', '.;').capitalize()
                    break
                elif search_word == None and out_words[word] == '':
                    out_words[word] = '--'

    for ow in out_words:
        out_file.write(ow + ';' + out_words[ow] + '\n')