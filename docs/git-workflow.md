# Git Workflow

Документация описывает базовый Git workflow для командной разработки.

Основная идея:

- `main` напрямую не изменяем.
- Для каждой задачи создаём отдельную ветку.
- Перед Pull Request обновляем свою ветку относительно актуального `main`.
- После завершения задачи удаляем рабочую ветку.

---

## 1. Перед новой задачей

Перед началом новой задачи нужно перейти в `main`:

```bash
git switch main
```

Обновить `main`:

```bash
git pull --ff-only
```

`--ff-only` нужен для того, чтобы Git не создал случайный merge commit при обновлении `main`.

После этого создать новую ветку от актуального `main`:

```bash
git switch -c feature/new-feature
```

---

## 2. Работа в своей ветке

После внесения изменений нужно проверить состояние файлов:

```bash
git status
```

Добавить изменения:

```bash
git add .
```

Создать commit:

```bash
git commit -m "feat: setup frontend"
```

Первый push новой ветки:

```bash
git push -u origin feature/new-feature
```

После первого push для следующих изменений в этой же ветке достаточно:

```bash
git add .
git commit -m "..."
git push
```

---

## 3. Если случайно начал работать в main

Если изменения ещё не были закоммичены, можно просто создать новую ветку:

```bash
git switch -c feature/new-feature
```

Git перенесёт текущие незакоммиченные изменения в новую ветку.

После этого можно продолжить работу и сделать commit уже в правильной ветке:

```bash
git add .
git commit -m "feat: add new feature"
```

Если изменения уже были закоммичены в `main`, лучше не исправлять это самостоятельно, а сначала согласовать с командой.

---

## 4. Обновление ветки через rebase

Если за время работы в `main` появились новые изменения, нужно подтянуть их в свою ветку через `rebase`.

Сначала перейти в `main`:

```bash
git switch main
```

Обновить `main`:

```bash
git pull --ff-only
```

Вернуться в свою ветку:

```bash
git switch feature/new-feature
```

Перед `rebase` желательно проверить, что нет незакоммиченных изменений:

```bash
git status
```

Если всё чисто, выполнить `rebase` от актуального `main`:

```bash
git rebase main
```

Если конфликтов нет, можно продолжать работу.

Если ветка уже была запушена раньше, после `rebase` нужен push с флагом:

```bash
git push --force-with-lease
```

Важно использовать именно:

```bash
git push --force-with-lease
```

а не:

```bash
git push --force
```

`--force-with-lease` безопаснее, потому что не перезапишет чужие изменения, если кто-то успел обновить эту же remote-ветку.

---

## 5. Важное правило про rebase

`rebase` безопасно делать в своей личной рабочей ветке.

Если в одной ветке работает несколько человек, `rebase` нужно делать только после согласования.

Причина: `rebase` переписывает историю коммитов. Из-за этого у других участников могут появиться проблемы с синхронизацией ветки.

---

## 6. Если во время rebase появились конфликты

Git покажет файлы с конфликтами.

Нужно открыть эти файлы и исправить конфликты вручную.

После исправления конфликтов добавить файлы:

```bash
git add .
```

Продолжить `rebase`:

```bash
git rebase --continue
```

Если конфликтов несколько, Git может попросить повторить эти действия несколько раз.

Если нужно отменить `rebase`:

```bash
git rebase --abort
```

После успешного `rebase`, если ветка уже была запушена, выполнить:

```bash
git push --force-with-lease
```

---

## 7. Pull Request

Когда работа готова, нужно создать обычный Pull Request.

`Draft Pull Request` не используем, если команда отдельно не договорилась об обратном.

Перед созданием Pull Request желательно убедиться, что ветка актуальна относительно `main`.

Для этого:

```bash
git switch main
git pull --ff-only

git switch feature/new-feature
git rebase main
```

Если после `rebase` ветка уже была запушена, отправить изменения:

```bash
git push --force-with-lease
```

---

## 8. Pull Request checklist

Перед созданием Pull Request проверить:

- ветка создана от актуального `main`;
- ветка обновлена через `rebase main`;
- проект запускается;
- нет лишних файлов;
- нет временных комментариев и мусора в коде;
- commit message написаны понятно;
- Pull Request имеет понятное название;
- описание Pull Request заполнено, если изменение не очевидное.

---

## 9. Merge Pull Request

Когда Pull Request проверен и готов, предпочтительно использовать один из двух вариантов:

```text
Squash and merge
```

или:

```text
Rebase and merge
```

### Что выбрать

#### Squash and merge

Хороший default-вариант.

Он объединяет все коммиты из ветки в один commit в `main`.

Подходит, если:

- в ветке было много мелких commit;
- commit message были неидеальные;
- нужно сохранить чистую историю `main`.

#### Rebase and merge

Хороший вариант, если в ветке уже аккуратные и осмысленные commit.

Подходит, если:

- каждый commit имеет отдельный смысл;
- историю изменений важно сохранить;
- commit message написаны аккуратно.

#### Merge pull request

Обычный `Merge pull request` лучше не использовать.

Он создаёт дополнительный merge commit, из-за чего история `main` становится менее чистой.

### Рекомендация

По умолчанию использовать:

```text
Squash and merge
```

Если в ветке аккуратные и важные отдельные commit — использовать:

```text
Rebase and merge
```

Обычный:

```text
Merge pull request
```

не использовать.

---

## 10. После merge

После merge нужно перейти в `main`:

```bash
git switch main
```

Обновить `main`:

```bash
git pull --ff-only
```

Удалить локальную ветку:

```bash
git branch -d feature/new-feature
```

Если Git ругается, можно удалить ветку принудительно:

```bash
git branch -D feature/new-feature
```

Важно: `git branch -D` использовать только если точно понятно, что ветка уже не нужна.

После этого можно почистить список remote-веток:

```bash
git fetch -p
```

Посмотреть remote-ветки:

```bash
git branch -r
```

На GitHub после merge нужно нажать:

```text
Delete branch
```

---

## Branch names

### Основные типы веток

```text
feature/...   новая функциональность
fix/...       исправление бага
refactor/...  изменение структуры без новой логики
hotfix/...    срочный фикс
chore/...     настройки, конфиги, зависимости
docs/...      документация
```

### Примеры

```text
feature/add-auth-page
fix/login-validation
refactor/user-card
hotfix/fix-production-error
chore/update-dependencies
docs/git-workflow
```

### Правила именования веток

- использовать lowercase;
- слова разделять через `-`;
- название должно кратко описывать задачу;
- не использовать пробелы;
- не использовать кириллицу.

---

## Commit message

### Основные типы commit message

```text
feat: новая функциональность
fix: исправление бага
refactor: изменение структуры без новой логики
chore: настройки, конфиги, зависимости
docs: документация
style: изменения стилей без изменения логики
test: добавление или изменение тестов
```

### Примеры

```text
feat: add login form
fix: fix email validation
refactor: move auth logic to service
chore: install eslint
docs: add git workflow
style: update button styles
test: add login form tests
```

### Правила commit message

- писать коротко и понятно;
- использовать английский язык;
- начинать с типа изменения;
- не писать слишком общие сообщения.

---

## Короткая версия workflow

### Новая задача

```bash
git switch main
git pull --ff-only
git switch -c feature/task-name
```

### Работа в ветке

```bash
git status
git add .
git commit -m "feat: add task feature"
git push -u origin feature/task-name
```

### Перед Pull Request

```bash
git switch main
git pull --ff-only

git switch feature/task-name
git rebase main
git push --force-with-lease
```

### После merge

```bash
git switch main
git pull --ff-only
git branch -d feature/task-name
git fetch -p
git branch -r
```

---

## Главные правила

- `main` напрямую не трогаем.
- Новую ветку создаём только от актуального `main`.
- Для каждой задачи создаём отдельную ветку.
- Перед Pull Request делаем `rebase main`.
- После `rebase`, если ветка уже была запушена, используем `git push --force-with-lease`.
- `rebase` чужой или общей ветки не делаем без согласования.
- `Draft Pull Request` не используем, если команда отдельно не договорилась.
- Обычный `Merge pull request` лучше не использовать.
- По умолчанию используем `Squash and merge`.
- Не мержим чужие Pull Request без согласования.
- После merge удаляем рабочую ветку.
