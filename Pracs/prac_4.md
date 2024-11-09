# Практическое задание №4. Системы контроля версий

П.Н. Советов, РТУ МИРЭА

Работа с Git.

## Задача 1

На сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing-git/ (цвета могут отличаться, есть команды undo/redo) с помощью команд эмулятора git получить следующее состояние проекта (сливаем master с first, перебазируем second на master): см. картинку ниже. Прислать свою картинку.

![image](https://github.com/user-attachments/assets/0c5eb29b-3d30-4ee2-a860-9dc6207231ae)


## Решение
```
git commit
git tag in
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
git rebase second
git checkout in
```

![image](https://github.com/user-attachments/assets/47ce2a3d-3f85-441f-bafd-2824974a9610)

---


## Задача 2

Создать локальный git-репозиторий. Задать свои имя и почту (далее – coder1). Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git.

## Решение
```
root@vd4662:~/config/task2# git init
Initialized empty Git repository in /root/config/task2/.git/
root@vd4662:~/config/task2# git config --global user.name "coder1"
root@vd4662:~/config/task2# git config --global user.email "coder1@example.com"
root@vd4662:~/config/task2# echo "# test file" > prog.py
root@vd4662:~/config/task2# git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        prog.py

nothing added to commit but untracked files present (use "git add" to track)
root@vd4662:~/config/task2# git add prog.py
root@vd4662:~/config/task2# git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   prog.py

root@vd4662:~/config/task2# git commit -m "add prog.py"
[main (root-commit) 3325ae7] add prog.py
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py
root@vd4662:~/config/task2# git log --oneline
3325ae7 (HEAD -> main) add prog.py
root@vd4662:~/config/task2#
```

![5](https://github.com/user-attachments/assets/eddb76ad-db7b-466f-af6b-82b64e5edd0d)

---


## Задача 3

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

## Решение
```
$ git init
Initialized empty Git repository in C:/Temp/Mikhail Krysin/coder1/.git/

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ git config user.name "Coder 1"

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ git config user.email "coder1@corp.com"

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ echo "print('Hello from RTU MIREA')" > prog.py

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ git add prog.py
warning: in the working copy of 'prog.py', LF will be replaced by CRLF the next time Git touches it

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ git commit -m "first commit"
[master (root-commit) 0341c1b] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ cd ..

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin
$ git init --bare server.git
Initialized empty Git repository in C:/Temp/Mikhail Krysin/server.git/

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin
$ cd coder1/

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ git remote add server ../server.git

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ git remote -v
server  ../server.git (fetch)
server  ../server.git (push)

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ git push server master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 234 bytes | 234.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ../server.git
 * [new branch]      master -> master

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ cd ..

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin
$ git clone server.git coder2
Cloning into 'coder2'...
done.

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin
$ cd coder1

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ echo "Program_1 info" >> README.md

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ git add README.md
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ git commit -m "coder 1 info"
[master e32a685] coder 1 info
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ git push server master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 279 bytes | 279.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To ../server.git
   0341c1b..e32a685  master -> master

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder1 (master)
$ cd ../coder2

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master)
$ echo "Program_2 info" >> README.md

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master)
$ git add README.md
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master)
$ git config user.name "Coder 2"

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master)
$ git config user.email "coder2@corp.com"

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master)
$ git commit -m "coder2 info"
[master e3c75d8] coder2 info
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master)
$ git push origin master
To C:/Temp/Mikhail Krysin/server.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'C:/Temp/Mikhail Krysin/server.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master)
$ git pull origin master
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 259 bytes | 37.00 KiB/s, done.
From C:/Temp/Mikhail Krysin/server
 * branch            master     -> FETCH_HEAD
   0341c1b..e32a685  master     -> origin/master
Auto-merging README.md
CONFLICT (add/add): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master|MERGING)
$ git add README.md

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master|MERGING)
$ git commit -m "readme fix"
[master 6d607b0] readme fix

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master)
$ git push origin master
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 12 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 613 bytes | 613.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To C:/Temp/Mikhail Krysin/server.git
   e32a685..6d607b0  master -> master

misha@DESKTOP-1AOHSQN MINGW64 /c/Temp/Mikhail Krysin/coder2 (master)
$ git log --graph --all
*   commit 6d607b0fb29ec27877b4cfea1ba8265db48ecb0d (HEAD -> master, origin/master, origin/HEAD)
|\  Merge: e3c75d8 e32a685
| | Author: Coder 2 <coder2@corp.com>
| | Date:   Sat Nov 9 18:31:26 2024 +0300
| |
| |     readme fix
| |
| * commit e32a68574c6a2693e2f92b5e8849813b8f8d83ea
| | Author: Coder 1 <coder1@corp.com>
| | Date:   Sat Nov 9 18:28:52 2024 +0300
| |
| |     coder 1 info
| |
* | commit e3c75d877e0ea1c4b966aee78921025f7703f3af
|/  Author: Coder 2 <coder2@corp.com>
|   Date:   Sat Nov 9 18:30:32 2024 +0300
|
|       coder2 info
|
* commit 0341c1bc261a0dd38fc4225e9eaf63516fada482
  Author: Coder 1 <coder1@corp.com>
  Date:   Sat Nov 9 18:25:38 2024 +0300
:

```
![image](https://github.com/user-attachments/assets/fb23b408-b17c-4f6f-9473-5ab3db0518be)


---


## Задача 4

Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git.

## Решение
```python
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
![image](https://github.com/user-attachments/assets/6c190867-9060-452f-b690-95332e617a69)

