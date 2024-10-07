## Задача 1

```bash
Код реализации:
cut -d: -f1 /etc/passwd | sort
```
![image](https://github.com/user-attachments/assets/7c947a8b-dd87-4c04-a05f-a230345ef2f4)

## Задача 2
```bash
Код реализации:
cat /etc/protocols | tail -n 5 | sort -nrk2 | awk '{print $2, $1}'
```
![image](https://github.com/user-attachments/assets/1e72c854-3274-4de7-946c-ba43b99e719e)

## Задача 3
```bash
Код реализации:
#!/usr/bin/bash
string="$1"
size=$(echo "$string" | wc -m)
echo -n "+"
for ((i=-2;i<size;i++))
do
echo -n "-"
done
echo "+"
echo "|  $string |"
echo -n "+"
for ((i=-2;i<size;i++))
do
echo -n "-"
done
echo "+"
```
![image](https://github.com/user-attachments/assets/114ac328-c4e7-4a0f-9694-a862395b0860)

## Задача 4
```bash
grep -o '\b[a-zA-Z_][a-zA-Z_]*\b' Evaluator.cpp | sort | uniq
```
![image](https://github.com/user-attachments/assets/7630479f-f14a-47e3-b794-60f820c6dac0)


## Задача 5
```bash
#!/usr/bin/bash
chmod +x "$1"
cp "$1" /usr/local/bin
```
![image](https://github.com/user-attachments/assets/e31e5312-9e6b-4bc0-a4f4-5c637192b8f4)
![image](https://github.com/user-attachments/assets/39160839-7ed8-4d23-9418-4abe717ef99c)

## Задача 6
```python
#! /usr/bin/python3
from sys import argv
name = argv[1]
with open(name, 'r') as file:
  line = file.readline().strip()
  try:
    if (line[0:2] == '//' and name.split('.')[-1] in ("js", "c")) or (line[0] == '#' and name.split('.')[-1] == "py"):
      print("File has a comment in the first line")
    else:
      print("File does not have a comment in the first line")
  except IndexError:
    print("Некорректный файл")
```
![image](https://github.com/user-attachments/assets/5051a1ce-01c4-4d79-94f3-6d1398889219)

Код скрипта

![image](https://github.com/user-attachments/assets/90d7e4cf-a895-4687-a209-a2918660c211)

Содержимое проверяемого файла

![image](https://github.com/user-attachments/assets/b80bbc44-da22-4f21-8b6a-fb8f82e9f082)

Результат работы программы

## Задача 7
![image](https://github.com/user-attachments/assets/5c3bc052-f862-4db5-ac2b-1c3f926484b6)

Код скрипта

![image](https://github.com/user-attachments/assets/21d24e67-1129-4a5d-9f82-2d697b279001)

Функционирование программы

## Задача 8
```bash
#!/bin/bash
find . -name "*.$1" -print0 -maxdepth 1 | tar -czvf archive.tar.gz --null -T -
```
![image](https://github.com/user-attachments/assets/1e17b61e-9969-43e8-9581-cb5cdebff1c5)

![image](https://github.com/user-attachments/assets/08475d13-15f6-4941-86ff-0f6bd11e5785)



## Задача 9
```bash
#!/bin/bash
sed 's/    /\t/g' "$1" > "$2"
```
![image](https://github.com/user-attachments/assets/05830cbb-ff0b-456e-922c-f6b18d58f96f)

Доказательство успешного выполнения скрипта

![image](https://github.com/user-attachments/assets/a7c162bb-5078-4898-ae10-4d52795f19b0)

Содержимое файла task_9.txt

![image](https://github.com/user-attachments/assets/ba1f4c87-5237-45d8-b3eb-e386a26ca65f)

Содержимое файла task_9_out.txt



## Задача 10
```bash
#!/usr/bin/bash
find "$1" -type f -empty -name "*.txt"
```
![image](https://github.com/user-attachments/assets/fe8d592f-2fd1-4f25-b106-11e0bc1d9b89)

Примечание: "4.txt" не пустой
