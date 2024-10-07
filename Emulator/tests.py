import unittest
import os
import tarfile
import io
from emulator import VirtualFileSystem, Shell
from unittest.mock import patch

TEST_TAR = 'test_data.tar'

def create_test_tar():
    """Создает тестовый tar-архив с примерами файлов."""
    with tarfile.open(TEST_TAR, "w") as tar:
        file1_data = io.BytesIO(b"Hello World!")
        tarinfo = tarfile.TarInfo(name="file1.txt")
        tarinfo.size = len(file1_data.getvalue())
        tar.addfile(tarinfo, file1_data)

        file2_data = io.BytesIO(b"Hello!")
        tarinfo = tarfile.TarInfo(name="file2.txt")
        tarinfo.size = len(file2_data.getvalue())
        tar.addfile(tarinfo, file2_data)

        tarinfo = tarfile.TarInfo(name="subdir/")
        tarinfo.type = tarfile.DIRTYPE
        tar.addfile(tarinfo)

        file3_data = io.BytesIO(b"Sub File")
        tarinfo = tarfile.TarInfo(name="subdir/file3.txt")
        tarinfo.size = len(file3_data.getvalue())
        tar.addfile(tarinfo, file3_data)

class TestVirtualFileSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_test_tar()  # Создаем тестовый архив перед выполнением тестов

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(TEST_TAR):
            os.remove(TEST_TAR)  # Удаляем архив после завершения тестов

    def setUp(self):
        self.vfs = VirtualFileSystem(TEST_TAR)
        self.shell = Shell(self.vfs)

    def test_list_files_root(self):
        """Проверяем количество файлов в корневом каталоге."""
        files = self.vfs.list_files()
        self.assertEqual(len(files), 5)  # Ожидаем 5 файлов в корневом каталоге

    def test_list_files_subdir(self):
        """Проверяем количество файлов в подкаталоге."""
        self.vfs.change_directory("subdir")
        files = self.vfs.list_files()
        self.assertEqual(len(files), 1)  # Ожидаем 1 файл в подкаталоге

    def test_change_directory(self):
        self.vfs.change_directory("subdir")
        self.assertEqual(self.vfs.get_current_directory(), "subdir")

    def test_change_directory_parent(self):
        self.vfs.change_directory("subdir")
        self.vfs.change_directory("..")
        self.assertEqual(self.vfs.get_current_directory(), "/")

    def test_change_directory_invalid(self):
        with self.assertRaises(FileNotFoundError):
            self.vfs.change_directory("nonexistent")

    def test_read_file(self):
        content = self.vfs.read_file("file1.txt")
        self.assertEqual(content, "Hello World!")

    def test_read_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            self.vfs.read_file("nonexistent.txt")

    def test_write_file(self):
        self.vfs.write_file("file4.txt", "New Content")
        self.assertIn("file4.txt", self.vfs.files)

    def test_write_file_overwrite(self):
        self.vfs.write_file("file1.txt", "New Content")
        content = self.vfs.read_file("file1.txt")
        self.assertEqual(content, "New Content")

    def test_find_file_in_subdir(self):
        """Проверяем поиск файла только во вложенных директориях."""
        self.vfs.change_directory("subdir")
        result = self.vfs.find_file("file3.txt")
        self.assertEqual(result, "subdir/file3.txt")  # Проверяем, что файл найден по полному пути

    def test_find_file_nonexistent(self):
        result = self.vfs.find_file("nonexistent.txt")
        self.assertIsNone(result)

    def test_copy_file(self):
        self.vfs.copy_file("file1.txt", "file1_copy.txt")
        content = self.vfs.read_file("file1_copy.txt")
        self.assertEqual(content, "Hello World!")

    # Тесты для команд
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ls_command(self, mock_stdout):
        self.shell.execute_command("ls")
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertIn("file1.txt", output)
        self.assertIn("file2.txt", output)
        self.assertIn("subdir", output)  # Проверяем, что директория отображается

    def test_cd_command_valid(self):
        self.shell.execute_command("cd subdir")
        self.assertEqual(self.vfs.get_current_directory(), "subdir")

    def test_cd_command_invalid(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.shell.execute_command("cd nonexistent")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Directory not found.")

    def test_cp_command(self):
        self.shell.execute_command("cp file1.txt file1_copy.txt")
        content = self.vfs.read_file("file1_copy.txt")
        self.assertEqual(content, "Hello World!")

    def test_cp_command_invalid_source(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.shell.execute_command("cp nonexistent.txt file1_copy.txt")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Source file not found.")

    def test_cp_command_2(self):
        self.shell.execute_command("cp file2.txt file2_copy.txt")
        content = self.vfs.read_file("file2_copy.txt")
        self.assertEqual(content, "Hello!")

    # Тесты для команды rev
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rev_command_string(self, mock_stdout):
        self.shell.execute_command("rev Hello")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "olleH")  # Проверяем реверс строки

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rev_command_file(self, mock_stdout):
        self.shell.execute_command("rev -f file1.txt")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "!dlroW olleH")  # Проверяем реверс содержимого файла

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rev_command_invalid_file(self, mock_stdout):
        self.shell.execute_command("rev -f nonexistent.txt")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "File not found.")  # Проверяем вывод при отсутствии файла

if __name__ == '__main__':
    unittest.main()
