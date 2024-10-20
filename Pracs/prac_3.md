# Задача 1
### Формулировка задачи
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
### Пример
```JSON
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сидоров С.С."
    },
    {
      "age": 19,
      "group": "ИКБО-10-23",
      "name": "Барташевский Д.Д."
    }
  ],
  "subject": "Конфигурационное управление"
} 
```
### Решение
```Jsonnet
local generateGroups = [ 
  "ИКБО-%d-20" % i for i in std.range(1, 24) 
];

local createStudent = function(name, age, groupName) {
  name: name,
  age: age,
  group: groupName
};

local studentsList = [
  createStudent("Иванов И.И.", 19, generateGroups[3]),
  createStudent("Петров П.П.", 18, generateGroups[4]),
  createStudent("Сидоров С.С.", 18, generateGroups[4]),
  createStudent("Крысин М.А.", 19, "ИКБО-10-23")
];

local course = "Конфигурационное управление";

{
  groups: generateGroups,
  students: studentsList,
  subject: course
}
```
![image](https://github.com/user-attachments/assets/ea48f8a4-44e5-467d-a617-58a7699a174e)

