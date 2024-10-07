# Задача 1
### Формулировка задачи
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета.
### Решение
```
pip show matplotlib
```

![image](https://github.com/user-attachments/assets/9134bc16-85f1-4d92-9d66-7ecfcdef582d)

#### Основные элементы содержимого файла со служебной информацией из пакета:
* Name: matplotlib (имя пакета)
* Version: 3.9.2 (версия пакета по стандарту семантического версионирования (SemVer). В данном случае 3.9.2 указывает на третью основную версию (MAJOR — 3), с девятым минорным обновлением (MINOR — 9), а патч (PATCH — 2) включает исправления ошибок без изменения функциональности)
* Summary: Python plotting package (краткое описание пакета. В этом случае пакет matplotlib — это библиотека для построения графиков в Python)
* Home-page: https://matplotlib.org (ссылка на официальный сайт или документацию пакета)
* Author: John D. Hunter, Michael Droettboom (авторы пакета)
* Author-email: Unknown matplotlib-users@python.org (контактная информация автора)
* License: License agreement for matplotlib versions 1.3.0 and later (лицензия, по которой распространяется пакет)
### Формулировка задачи
Как получить пакет без менеджера пакетов, прямо из репозитория?
### Решение
Чтобы скачать и установить пакет без использования менеджера пакетов, можно получить его исходный код напрямую из репозитория, например, с GitHub.
```
git clone https://github.com/matplotlib/matplotlib.git
cd matplotlib
pip install .
```
![image](https://github.com/user-attachments/assets/0ddb123b-a22a-4a92-b89b-7dcffefe8b94)

![image](https://github.com/user-attachments/assets/1afab009-da0c-40f8-a8a0-b9c3c0b3bac5)

# Задача 2
### Формулировка задачи
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
### Решение
```
npm view express
```
![image](https://github.com/user-attachments/assets/58af8e9a-f182-4962-8a7f-cc4ffcad8f4a)

#### Основные элементы содержимого файла со служебной информацией из пакета:
* express (имя пакета)
* 4.21.0 (Версия пакета по стандарту семантического версионирования (SemVer). В данном случае 4.21.0 указывает на четвёртую основную версию (MAJOR — 4), с двадцать первым минорным обновлением (MINOR — 9), а патч (PATCH — 0) включает исправления ошибок без изменения функциональности)
* MIT (лицензия, по которой распространяется пакет (в данном случае MIT, одна из самых открытых лицензий)
* deps: 31 (количество зависимостей. Пакет Express требует 31 внешнюю библиотеку для работы)
* versions: 279 (количество опубликованных версий Express.js)
* Fast, unopinionated, minimalist web framework (краткое описание пакета: Express — это быстрый, минималистичный веб-фреймворк для Node.js)
* http://expressjs.com/ (ссылка на официальный сайт, где можно найти документацию и другие ресурсы, связанные с пакетом)
* keywords: express, framework, sinatra, web, http, rest, restful, router, app, api (список ключевых слов, по которым можно найти пакет)
* dist (информация о дистрибуции пакета)
  * .tarball: https://registry.npmjs.org/express/-/express-4.21.0.tgz (ссылка на архив пакета в формате .tgz, который можно скачать)
  * .shasum: d57cb706d49623d4ac27833f1cbc466b668eb915 (контрольная сумма (SHA-1) для проверки целостности пакета)
  * .integrity: sha512-VqcNGcj/Id5ZT1LZ/cfihi3ttTn+NJmkli2eZADigjq29qTlWi/hAQ43t/VLPq8+UX06FCEx3ByOYet6ZFblng== (контрольная сумма по алгоритму SHA-512 для подтверждения целостности)
  * .unpackedSize: 220.8 kB (размер распакованного пакета)
* dependencies (список зависимостей пакета и их версии)
* maintainers (список мейнтейнеров пакета и их контактные данные)
* dist-tags (теги дистрибуции)
  * latest: 4.21.0 (стабильная версия пакета)
  * next: 5.0.0 (следующая версия, которая еще не является стабильной)
### Формулировка задачи
Как получить пакет без менеджера пакетов, прямо из репозитория?
### Решение
Чтобы скачать и установить пакет без использования менеджера пакетов, можно получить его исходный код напрямую из репозитория, например, с GitHub.
```
git clone https://github.com/expressjs/express.git
cd express
npm install
```
![image](https://github.com/user-attachments/assets/2615b8ea-b156-4af6-b1b6-cc088693b446)


# Задача 3
### Формулировка задачи
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.
### Решение
Создадим .dot файл для зависимостей matplotlib:
```dot
digraph mygraph {
    "matplotlib" -> "libjs-jquery";
    "matplotlib" -> "libjs-jquery-ui";
    "matplotlib" -> "python-matplotlib-data";
    "matplotlib" -> "python3-dateutil";
    "matplotlib" -> "python3-pil.imagetk";
    "matplotlib" -> "python3-pyparsing";
    "matplotlib" -> "python3-six";
    "matplotlib" -> "python3-numpy";
    "matplotlib" -> "python3-numpy-abi9";
    "matplotlib" -> "python3";
    "matplotlib" -> "python3";
    "matplotlib" -> "python3-cycler";
    "matplotlib" -> "python3-fonttools";
    "matplotlib" -> "python3-kiwisolver";
    "matplotlib" -> "python3-packaging";
    "matplotlib" -> "python3-pil";
    "matplotlib" -> "python3:any";
    "matplotlib" -> "libc6";
    "matplotlib" -> "libfreetype6";
    "matplotlib" -> "libgcc-s1";
    "matplotlib" -> "libqhull-r8.0";
    "matplotlib" -> "libstdc++6";
}
```

![example](https://github.com/user-attachments/assets/fcf623d4-7314-4d84-a8ee-818385c1c111)

Создадим .dot файл для зависимостей express:
```dot
digraph mygraph {
    "express" -> "node-accepts";
    "express" -> "node-array-flatten";
    "express" -> "node-body-parser";
    "express" -> "node-content-disposition";
    "express" -> "node-content-type";
    "express" -> "node-cookie";
    "express" -> "node-cookie-signature";
    "express" -> "node-debug";
    "express" -> "node-depd";
    "express" -> "node-encodeurl";
    "express" -> "node-escape-html";
    "express" -> "node-etag";
    "express" -> "node-finalhandler";
    "express" -> "node-fresh";
    "express" -> "node-merge-descriptors";
    "express" -> "node-methods";
    "express" -> "node-on-finished";
    "express" -> "node-parseurl";
    "express" -> "node-path-to-regexp";
    "express" -> "node-proxy-addr";
    "express" -> "node-qs";
    "express" -> "node-range-parser";
    "express" -> "node-safe-buffer";
    "express" -> "node-send";
    "express" -> "node-serve-static";
    "express" -> "node-setprototypeof";
    "express" -> "node-statuses";
    "express" -> "node-type-is";
    "express" -> "node-utils-merge";
    "express" -> "node-vary";
    "express" -> "nodejs:any";
}
```

![example_2](https://github.com/user-attachments/assets/8bbd8eb5-8994-4555-bc0a-38098ccab79f)

# Задача 4
### Формулировка задачи
Следующие задачи можно решать с помощью инструментов на выбор:

Решатель задачи удовлетворения ограничениям (MiniZinc).
SAT-решатель (MiniSAT).
SMT-решатель (Z3).
Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.

Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.
### Решение
```MiniZinc
include "alldifferent.mzn";

% Определяем переменные для каждой цифры билета
array[1..6] of var 0..9: digits;

% Ограничение: все цифры должны быть разными
constraint all_different(digits);

% Сумма первых трех цифр должна равняться сумме последних трех цифр
constraint sum(digits[1..3]) = sum(digits[4..6]);

% Найдем минимальное решение для суммы первых трех цифр
var int: sum1 = sum(digits[1..3]);
solve minimize sum1;

% Читаем вывод
output [
    "Digits: ", show(digits), "\n",
    "Sum of first three digits: ", show(sum1), "\n"
];
```
### Ответ
![image](https://github.com/user-attachments/assets/61b48110-d888-488a-a52c-3d66392658bd)


# Задача 5
### Формулировка задачи
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.
![image](https://github.com/user-attachments/assets/fee5e211-23b4-46a8-86b8-508047ca42d5)

### Решение
```MiniZinc
% Определяем количество версий для каждого компонента
int: totalMenu = 6;        % Общее количество версий для меню
int: totalDropdown = 5;    % Общее количество версий для выпадающего списка (dropdown)
int: totalIcon = 2;        % Общее количество версий для иконки (icon)

% Переменные для выбора версии каждого компонента
var 1..totalMenu: menu;            % Выбранная версия для меню
var 1..totalDropdown: dropdown;    % Выбранная версия для выпадающего списка
var 1..totalIcon: icon;            % Выбранная версия для иконки

% Массив, содержащий версии для меню в формате (major, minor, patch)
array[1..totalMenu] of tuple(int, int, int): menuVersions = 
  [(1,0,0), (1,1,0), (1,2,0), (1,3,0), (1,4,0), (1,5,0)];
  
% Массив, содержащий версии для выпадающего списка
array[1..totalDropdown] of tuple(int, int, int): dropdownVersions = 
  [(1,8,0), (2,0,0), (2,1,0), (2,2,0), (2,3,0)];
  
% Массив, содержащий версии для иконки
array[1..totalIcon] of tuple(int, int, int): iconVersions = 
  [(1,0,0), (2,0,0)];

% Ограничения по версиям компонентов

% Меню должно быть либо версии (1,0,0), либо версии (1,5,0), 
% при этом иконка должна быть версии (1,0,0)
constraint (menuVersions[menu] == (1,0,0) \/ 
            (menuVersions[menu] == (1,5,0) /\ iconVersions[icon] == (1,0,0)));

% Если версия меню между 1.1.0 и 1.5.0, то версия выпадающего списка должна быть 
% либо (2,3,0), либо (2,0,0)
constraint (menuVersions[menu].2 >= 1 /\ menuVersions[menu].2 <= 5) -> 
          (dropdownVersions[dropdown] == (2,3,0) \/ dropdownVersions[dropdown] == (2,0,0));

% Если версия меню (1,0,0), то версия выпадающего списка должна быть (1,8,0)
constraint menuVersions[menu] == (1,0,0) -> dropdownVersions[dropdown] == (1,8,0);

% Если версия выпадающего списка имеет minor версию от 0 до 3, то версия иконки должна быть (2,0,0)
constraint (dropdownVersions[dropdown].2 >= 0 /\ dropdownVersions[dropdown].2 <= 3) -> 
          iconVersions[icon] == (2,0,0);

solve satisfy;

% Вывод выбранных версий для каждого компонента
output [
  "Selected Menu Version: ", show(menuVersions[menu]), "\n",
  "Selected Dropdown Version: ", show(dropdownVersions[dropdown]), "\n",
  "Selected Icon Version: ", show(iconVersions[icon]), "\n"
];
```
### Ответ
![image](https://github.com/user-attachments/assets/1f93feba-be97-42c7-945d-c7065393fc0a)
