# WSentence
Поиск предложений в статьях, содержащий заданные слова.

# Вход
Файл words.txt - список слов (фраз) 1 cлово на строку
Файл articles.txt - текст статей, разделенных знаком "###"

# Выход
Файл out.txt - список первых найденных предложений, в которых встречается каждое слово в формате csv:
Пример файла out.txt:
<разыскиваемое слово>;<найденное предложение>;<[порядковый номер статьи:порядковый номер предложения в котором слво найдено]>

<img src="https://user-images.githubusercontent.com/41264164/179364372-fc21d1ad-a51d-494b-9465-74970c99d2b6.png" width="400" />
# Сборка exe-шника
Ввести в консоли:
`pip install pyinstaller` - установка библеотки для сборки exe-файла
`pyinstaller --onefile --windowed source/Main.py` - команда для сборки exe-файла
exe-файл создастся в папке dist/Main.exe
