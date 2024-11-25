# Тесты


```
\tests
```


Запуск тестов:

```
pytest
```

# Запуск проекта

1. Клонируйте репозиторий:

```
https://github.com/iMaanick/library_management.git
```

2. При необходимости установить Poetry ```pip install poetry```

3. Запустить виртуальное окружение ```poetry shell```

4. Установить зависимости ```poetry install```


5. Добавьте файл .env и заполните его как в примере .example.env:

```
DATABASE_URI=sqlite:///test.db
```
6. Выполните для создания таблиц

```
alembic upgrade head 
```

7. Далее можете выполнять желаемые команды

## Команды

### `add`
Добавить новую книгу в библиотеку.

**Usage:**
```bash
python -m app.main.main add <title> <author> <year>
```

**Arguments:**
- `title` (str): Название книги.
- `author` (str): Автор книги.
- `year` (int): Год издания.

**Example:**
```bash
python -m app.main.main add "1984" "George Orwell" 1949
```

---

### `delete`
Удалить книгу из библиотеки по ее идентификатору.

**Usage:**
```bash
python -m app.main.main delete <book_id>
```

**Arguments:**
- `book_id` Идентификатор книги, которую нужно удалить.

**Example:**
```bash
python -m app.main.main  delete 1
```

---

### `search`
Поиск книг в библиотеке.

**Usage:**
```bash
python -m app.main.main search [--title <title>] [--author <author>] [--year <year>]
```

**Options:**
- `--title` (str): Фильтровать по названию.
- `--author` (str): Фильтр по автору.
- `--year` (int): Фильтр по году публикации.

**Examples:**
```bash
python -m app.main.main search --title "1984"
python -m app.main.main search --author "George Orwell"
python -m app.main.main search --year 1949
```

---

### `update_status`
Обновить статус книги ("в наличии" или "выдана").

**Usage:**
```bash
python -m app.main.main update_status <book_id> <status>
```

**Arguments:**
- `book_id` (int): Идентификатор книги.
- `status` (choice): Новый статус (`"в наличии"` или `"выдана"`).

**Example:**
```bash
python -m app.main.main update_status 1 "выдана"
```

---

### `list_books`
Отображение всех книг.

**Usage:**
```bash
python -m app.main.main list_books
```

**Example:**
```bash
python -m app.main.main list_books
```

---

## Обработка ошибок
- CLI проверяет ввод для каждой команды.
- Ошибки, такие как неверные годы или несуществующие идентификаторы книг, отображаются красным цветом для лучшей видимости.

# Функциональность

 1. Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
 2. Удаление книги: Пользователь вводит id книги, которую нужно удалить.
 3. Поиск книги: Пользователь может искать книги по title, author или year.
 4. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
 5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).

# О проекте
1. Click для разработки cli
2. SQLite в качестве базы данных
3. SQLAlchemy для работы с базой данных
4. Alembic для управления миграциями
5. Dishka для di
6. Pytest для тестов
7. Poetry для управления зависимостями