#!/bin/bash

if [ -z "$1" ]; then
  echo "Не введен первый параметр, отвечающий за версию проекта"
  exit 1
fi

version=$1
srcdir=$(pwd)
inputname=${srcdir##*/}
projname=${inputname}

echo "Источник: ${srcdir}"
echo "Имя проекта: ${projname}"
echo "Версия: ${version}"

# 1. Загрузка актуального состояния с сервера
echo "Загрузка актуального состояния с сервера..."
git pull origin master || { echo "Ошибка загрузки с сервера"; exit 1; }

# 2. Сборка проекта и установка зависимостей
echo "Сборка проекта..."
"C:/Users/Abdujalil/AppData/Local/Programs/Python/Python310/python.exe" -m pip install -r requirements.txt || { echo "Ошибка установки зависимостей"; exit 1; }

# 3. Выполнение unittest
echo "Запуск тестов unittest..."
"C:/Users/Abdujalil/AppData/Local/Programs/Python/Python310/python.exe" -m unittest discover -s "${srcdir}" -p "test_*.py" || { echo "Тесты не пройдены"; exit 1; }

# 4. Создание установщика с использованием PyInstaller для ui.py
echo "Создание установщика..."
"C:/Users/Abdujalil/AppData/Local/Programs/Python/Python310/python.exe" -m PyInstaller --onefile --windowed ui.py || { echo "Ошибка создания установщика"; exit 1; }

# 5. Перемещение установщика в папку установки
echo "Установка приложения..."
mv dist/ui.exe "C:/Users/Abdujalil/calculator-app" || { echo "Ошибка установки приложения"; exit 1; }

echo "Скрипт CI завершен успешно"

