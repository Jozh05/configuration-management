import os
import tarfile
import sys
import io

class VirtualFileSystem:
    def __init__(self, tar_path):
        self.tar_path = tar_path
        self.current_path = "/"
        self.files = {}
        self.load_files()

    def load_files(self):
        self.files.clear()  # Очистка текущего списка файлов
        with tarfile.open(self.tar_path, "r") as tar:
            for member in tar.getmembers():
                self.files[member.name] = member

    def list_files(self):
        unique_files = set()

        for f in self.files:
            if self.current_path == "/" and f.count("/") == 0:
                unique_files.add(os.path.basename(f))
            elif f.startswith(self.current_path) and not self.files[f].isdir():
                unique_files.add(os.path.basename(f))

        return list(unique_files)

    def change_directory(self, path):
        if path == "/":
            self.current_path = "/"
        elif path == "..":
            self.current_path = "/".join(self.current_path.split("/")[:-1]) or "/"
        elif path in self.files and self.files[path].isdir():
            self.current_path = path
        else:
            raise FileNotFoundError("Directory not found.")

    def read_file(self, filename):
        if filename in self.files:
            with tarfile.open(self.tar_path, "r") as tar:
                member = tar.extractfile(self.files[filename])
                return member.read().decode()
        else:
            abs_path = self.find_file(filename)
            if abs_path:
                with tarfile.open(self.tar_path, "r") as tar:
                    member = tar.extractfile(self.files[abs_path])
                    return member.read().decode()
            else:
                raise FileNotFoundError("File not found.")

    def write_file(self, filename, content):
        fileobj = io.BytesIO(content.encode())
        tarinfo = tarfile.TarInfo(name=filename)
        tarinfo.size = len(content.encode())

        with tarfile.open(self.tar_path, "a") as tar:
            tar.addfile(tarinfo, fileobj)

        self.load_files()  # Обновляем список файлов после записи

    def find_file(self, filename):
        for path in self.files:
            if os.path.basename(path) == filename and path.startswith(self.current_path):
                return path
        return None

    def copy_file(self, src, dest):
        abs_src = src if src in self.files else self.find_file(src)

        if not abs_src:
            raise FileNotFoundError("Source file not found.")

        if dest in self.files and self.files[dest].isdir():
            dest_path = os.path.join(dest, os.path.basename(src))

            self.write_file(dest_path, self.read_file(src))
        else:
            if dest in self.files:
                self.write_file(dest, self.read_file(src))
            else:
                self.write_file(dest, self.read_file(src))

    def get_current_directory(self):
        return self.current_path

class Shell:
    def __init__(self, vfs):
        self.vfs = vfs

    def execute_command(self, command):
        if not command.strip():  # Проверка на пустую строку
            return

        parts = command.split(maxsplit=1)
        cmd = parts[0]

        if cmd == "ls":
            files = self.vfs.list_files()
            if files:
                print("\n".join(files))
            else:
                print("No files found.")
        elif cmd == "cd":
            if len(parts) > 1:
                try:
                    self.vfs.change_directory(parts[1])
                except FileNotFoundError as e:
                    print(e)
            else:
                print("cd: missing argument")
        elif cmd == "exit":
            sys.exit(0)
        elif cmd == "rev":
            self.handle_rev_command(parts)
        elif cmd == "clear":
            os.system('cls')
        elif cmd == "cp":
            self.handle_cp_command(parts)
        elif cmd == "pwd":
            print(self.vfs.get_current_directory())
        else:
            print(f"{cmd}: command not found")

    def handle_cp_command(self, parts):
        if len(parts) != 2:
            print("Usage: cp <source> <destination>")
            return

        source_dest = parts[1].split()
        if len(source_dest) != 2:
            print("Usage: cp <source> <destination>")
            return

        source, destination = source_dest
        try:
            self.vfs.copy_file(source, destination)
        except FileNotFoundError as e:
            print(e)

    def handle_rev_command(self, parts):
        if len(parts) != 2:
            print("Usage: rev <string> or rev -f <filename>")
        else:
            param = parts[1]
            if param.startswith('-f'):
                filename = param[3:].strip()
                try:
                    content = self.vfs.read_file(filename)
                    reversed_content = content[::-1]
                    print(reversed_content)
                except FileNotFoundError as e:
                    print(e)
            else:
                print(param[::-1])  # Реверсируем строку

def main():
    if len(sys.argv) != 2:
        print("Usage: python emulator.py <path_to_tar>")
        sys.exit(1)

    vfs = VirtualFileSystem(sys.argv[1])
    shell = Shell(vfs)

    while True:
        command = input(f"{vfs.get_current_directory()} $ ")
        shell.execute_command(command)

if __name__ == "__main__":
    main()
