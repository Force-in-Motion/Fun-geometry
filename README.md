# Fun-geometry
Интерактивное приложение для создания и визуализации геометрических фигур с использованием библиотеки turtle.
## Функциональность
Приложение позволяет:
- Создавать различные геометрические фигуры (звезды, многоугольники)
- Настраивать параметры окна отображения (размер, цвет)
- Кастомизировать фигуры:
  - Размер сторон
  - Количество углов
  - Цвет фигуры
  - Скорость отрисовки
  - Толщину линий
  - Время отображения
## Установка
1. Клонируйте репозиторий:
bash
git clone https://github.com/your-username/Fun-geometry.git
cd Fun-geometry



2. Установите зависимости:
bash
pip install -r requirements.txt



## Использование
1. Запустите приложение:
bash
python main.py



2. Следуйте интерактивным подсказкам для настройки:
   - Укажите размеры окна
   - Выберите цвет фона
   - Выберите тип фигуры:
     - 1: Звезда
     - 2: Круг
     - 3: Многоугольник
   - Настройте параметры фигуры:
     - Длина стороны
     - Количество углов
     - Цвет фигуры
     - Скорость отрисовки
     - Толщину линии
     - Время отображения
3. После отрисовки фигуры вы можете:
   - Создать новую фигуру (введите "да", "yes" или "y")
   - Завершить работу (любой другой ответ)
## Структура проекта
- `main.py` - основной файл приложения
- `src/`
  - `bl_hight/` - высокоуровневая бизнес-логика
  - `bl_low/` - низкоуровневая бизнес-логика
  - `config/` - конфигурационные файлы
  - `interface/` - интерфейсы
  - `model/` - модели фигур и их модификаторы
## Требования
- Python 3.x
- turtle
- tkinter
- matplotlib
Этот README.md файл содержит:

Краткое описание проекта
Основную функциональность
Инструкции по установке
Подробное руководство по использованию
Описание структуры проекта
Требования к окружению