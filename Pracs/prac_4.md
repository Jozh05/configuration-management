# Задача 1
### Формулировка задачи
На сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing-git/ (цвета могут отличаться, есть команды undo/redo) с помощью команд эмулятора git получить следующее состояние проекта (сливаем master с first, перебазируем second на master): см. картинку ниже. Прислать свою картинку.
<img width="700" alt="Picture_1" src="https://github.com/user-attachments/assets/332eea25-74f8-43d9-b9c9-81b99ee39f49">
### Решение
```bash
git commit
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
git checkout [in_hash]
git tag in 
```
<img width="800" alt="Picture_1" src="https://github.com/user-attachments/assets/6f8a79fa-f76a-497a-86e7-23e87da0a012">

# Задача 2
### Формулировка задачи
Создать локальный git-репозиторий. Задать свои имя и почту (далее – coder1). Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git.
### Решение
<img width="700" alt="Picture_1" src="https://github.com/user-attachments/assets/df96207c-d666-41bf-a513-475f1431907f">

# Задача 3
### Формулировка задачи
Создать рядом с локальным репозиторием bare-репозиторий с именем server. Загрузить туда содержимое локального репозитория. Команда git remote -v должна выдать информацию о server! Синхронизировать coder1 с server.

Клонировать репозиторий server в отдельной папке. Задать для работы с ним произвольные данные пользователя и почты (далее – coder2). Добавить файл readme.md с описанием программы. Обновить сервер.

Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.

Coder2 добавляет в readme в раздел об авторах свою информацию и решает вопрос с конфликтами.

Прислать список набранных команд и содержимое git log.

Пример лога коммитов:
```
*   commit a457d748f0dab75b4c642e964172887de3ef4e3e
|\  Merge: 48ce283 d731ba8
| | Author: Coder 2 <coder2@corp.com>
| | Date:   Sun Oct 11 11:27:09 2020 +0300
| | 
| |     readme fix
| | 
| * commit d731ba84014d603384cc3287a8ea9062dbb92303
| | Author: Coder 1 <coder1@corp.com>
| | Date:   Sun Oct 11 11:22:52 2020 +0300
| | 
| |     coder 1 info
| | 
* | commit 48ce28336e6b3b983cbd6323500af8ec598626f1
|/  Author: Coder 2 <coder2@corp.com>
|   Date:   Sun Oct 11 11:24:00 2020 +0300
|   
|       coder 2 info
| 
* commit ba9dfe9cb24316694808a347e8c36f8383d81bbe
| Author: Coder 2 <coder2@corp.com>
| Date:   Sun Oct 11 11:21:26 2020 +0300
| 
|     docs
| 
* commit 227d84c89e60e09eebbce6c0b94b41004a4541a4
  Author: Coder 1 <coder1@corp.com>
  Date:   Sun Oct 11 11:11:46 2020 +0300
  
      first commit
```
### Решение
```bash
ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1
$ git init
Initialized empty Git repository in D:/Programming/MIREA/KONFIG/Pract_4/coder1/.git/

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ git config user.name "Coder 1"

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ git config user.email "coder1@corp.com"

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ echo "print('Hello from RTU MIREA')" > prog.py

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ git add prog.py
warning: in the working copy of 'prog.py', LF will be replaced by CRLF the next time Git touches it

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ git commit -m "first commit"
[main (root-commit) e26dc96] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ cd ..

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4
$ git init --bare server.git
Initialized empty Git repository in D:/Programming/MIREA/KONFIG/Pract_4/server.git/

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4
$ cd coder1

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ git remote add server ../server.git

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ git remote -v
server  ../server.git (fetch)
server  ../server.git (push)

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ git push server main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 234 bytes | 234.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ../server.git
 * [new branch]      main -> main

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ cd ..

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4
$ git clone server.git coder2
Cloning into 'coder2'...
done.

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4
$ cd coder1

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ echo "Program_1 info" >> README.md

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ git add README.md
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ git commit -m "coder 1 info"
[main 68a15ba] coder 1 info
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ git push server main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 279 bytes | 279.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ../server.git
   e26dc96..68a15ba  main -> main

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder1 (main)
$ cd ../coder2

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main)
$ echo "Program_2 info" >> README.md

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main)
$ git add README.md
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main)
$ git config user.name "Coder 2"

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main)
$ git config user.email "coder2@corp.com"

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main)
$ git commit -m "coder2 info"
[main c6ac512] coder2 info
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main)
$ git push origin main
To D:/Programming/MIREA/KONFIG/Pract_4/server.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'D:/Programming/MIREA/KONFIG/Pract_4/server.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main)
$ git pull origin main
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 259 bytes | 64.00 KiB/s, done.
From D:/Programming/MIREA/KONFIG/Pract_4/server
 * branch            main       -> FETCH_HEAD
   e26dc96..68a15ba  main       -> origin/main
Auto-merging README.md
CONFLICT (add/add): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main|MERGING)
$ git add README.md

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main|MERGING)
$ git commit -m "readme fix"
[main d5257be] readme fix

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main)
$ git push origin main
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 12 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 620 bytes | 620.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To D:/Programming/MIREA/KONFIG/Pract_4/server.git
   68a15ba..d5257be  main -> main

ljken@Dmitrybwm MINGW64 /d/Programming/MIREA/KONFIG/Pract_4/coder2 (main)
$ git log --graph --all
*   commit d5257be56a5189b1923f44894c2536ad7f05f8d0 (HEAD -> main, origin/main, origin/HEAD)
|\  Merge: c6ac512 68a15ba
| | Author: Coder 2 <coder2@corp.com>
| | Date:   Wed Nov 6 20:34:53 2024 +0300
| |
| |     readme fix
| |
| * commit 68a15ba92253243373430c5ca614417c1f08b8e2
| | Author: Coder 1 <coder1@corp.com>
| | Date:   Wed Nov 6 20:28:08 2024 +0300
| |
| |     coder 1 info
| |
* | commit c6ac512ad70f08e516da97e8e17d9118d4a47a8d
|/  Author: Coder 2 <coder2@corp.com>
|   Date:   Wed Nov 6 20:30:03 2024 +0300
|
|       coder2 info
|
* commit e26dc965e1f97f1d169cb178c3851d2681759ae6
  Author: Coder 1 <coder1@corp.com>
  Date:   Wed Nov 6 20:24:53 2024 +0300

      first commit

```
<img width="700" alt="Picture_1" src="https://github.com/user-attachments/assets/1f13328f-bc5b-4fa9-a226-2ccfa5f12652">

# Задача 4
### Формулировка задачи
Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git.
### Решение
```Python
import subprocess


def list_git_objects():
    try:
        result = subprocess.run(
            ["git", "rev-list", "--all", "--objects"],
            capture_output=True, text=True, check=True
        )
        return [line.split()[0] for line in result.stdout.splitlines()]
    except subprocess.CalledProcessError:
        print("Ошибка при получении списка объектов")
        return []


def main():
    for obj in list_git_objects():
        print(f"\n{'=' * 45}\nHash {obj}\n{'=' * 45}")
        subprocess.run(["git", "cat-file", "-p", obj], check=True)


if __name__ == "__main__":
    main()
```
<img width="600" alt="Picture_1" src="https://github.com/user-attachments/assets/61c6d21b-707a-4a19-a0aa-6816f48df216">