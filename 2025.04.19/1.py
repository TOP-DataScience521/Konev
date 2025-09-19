from pathlib import Path

def list_files(path: str) :
   
    directory = Path(path)
    
    
    # Получаю файлы без тех что в подкотологах
    files = [item.name for item in directory.iterdir() if item.is_file()]
    
    # Возвращаю файлы в виде кортежа
    return tuple(sorted(files))
    
    
    
    
#    C:\Users\Admin\Konev\2025.04.19>python -i 1.py
# >>> list_files(r'C:\Users\Admin\Konev\2025.04.19\data')
# ('7MD9i.chm', 'E3ln1.txt', 'F1jws.jpg', 'conf.py', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
# >>>