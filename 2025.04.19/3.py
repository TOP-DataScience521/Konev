# очень сложное задание((
# первый раз буду использовать * для всех имен в вспомогательном файле
from utils import *
from pathlib import Path

def search_context(main_keyword, *other_keywords, context=0):
    """главная функция для поиска"""
    # все ключевые слова
    keywords = [main_keyword] + list(other_keywords)
    results = []
    
    # проверка на папку
    data_dir = Path('data')
    if not data_dir.exists():
        print("Папка 'data' не найдена!")
        return results
    
    # ищу .txt файлы с использованием глобальной переменной
    for filepath in data_dir.glob('*.txt'):
        # смотрю все строки
        try:
            lines = get_file_lines(filepath)
        except:
            continue
            
        # тепаерь посмотрим ключевые слова по строкам
        for i, line in enumerate(lines, 1):
            found_keywords = find_keywords_in_text(line, keywords)
            
            # проверяю на совпадению
            if found_keywords:
                # тут по поводу контекста вокрул ключевого слова
                if context > 0:
                    context_lines = get_context_lines(lines, i, context)
                    text = ''.join(context_lines).strip()
                else:
                    text = line.strip()
                
                # результаты по ключам и типам словоря
                for keyword in found_keywords:
                    result = {
                        'keyword': keyword,
                        'filename': filepath.name,
                        'line': i,
                        'context': context,
                        'text': text
                    }
                    results.append(result)
    
    return results