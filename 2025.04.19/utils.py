# попробую функцию для размера терминала
from shutil import get_terminal_size

# функция для рамки
def important_message(text):
  
    
    # пробую получить размер терминала
    terminal_width = get_terminal_size().columns
    
    # вычтем единицу 
    width = terminal_width - 1
    
    # границы рамки
    border = '#' + '=' * (width - 2) + '#'
    
    # пустые строки внутри рамки
    empty_line = '#' + ' ' * (width - 2) + '#'
    
    # длинный текст не поместился,попробуем так
    words = text.split(' ')
    lines = []
    current_line = ''
    
    # соберу все в кучу
    for word in words:
        # ограничу строку
        if len(current_line) + len(word) + 1 <= width - 6:  # -6 потому что по 2 пробела и # с каждой стороны
            if current_line:
                current_line += ' ' + word
            else:
                current_line = word
        else:
            lines.append(current_line)
            current_line = word
    
    # добавлю еще строку
    if current_line:
        lines.append(current_line)
    
    # центрую, насколько возможно
    centered_lines = []
    for line in lines:
        centered_line = line.center(width - 4)  # -4 потому что по 2 пробела с каждой стороны
        centered_lines.append(centered_line)
    
    # еще раз все собераю в кучу
    result = []
    result.append(border)       # верх
    result.append(empty_line)   # пустота
    
    # отступы и текст
    for line in centered_lines:
        result.append('#  ' + line + '  #')
    
    result.append(empty_line)   # пустота
    result.append(border)       # низ
    
    # попробуем через переносы соединить строки
    return '\n'.join(result)
  



  
    
import re
from pathlib import Path

def is_similar_word(word, keyword):
    """проверка слов с ключевым в разных вариантах"""
    word = word.lower()
    keyword = keyword.lower()
    
    # при полном совпадении
    if word == keyword:
        return True
    
    # например на такие формы слов
    if word.startswith(keyword):
        remaining = word[len(keyword):]
        # с такими окончаниями
        if remaining in ['ся', 'сь', 'а', 'я', 'и', 'ы', 'у', 'ю', 'ом', 'ем']:
            return True
    
    return False

def find_keywords_in_text(text, keywords):
    """ключевые слова в тексте"""
    found = []
    words = re.findall(r'\w+', text)
    for word in words:
        for keyword in keywords:
            if is_similar_word(word, keyword):
                found.append(keyword)
                break
    return found

def get_file_lines(filepath):
    """смотрим файлы и возращаем список"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()

def get_context_lines(lines, line_num, context):
    """+ контекст вокруг"""
    start = max(0, line_num - 1 - context)
    end = min(len(lines), line_num + context)
    return lines[start:end]