# Программа TOR (Temporary Opened Directory)

Программа TOR (Temporary Opened Directory) предоставляет простой и удобный способ управления вашими файлами и директориями. Это приложение помогает вам быстро находить и открывать файлы, особенно полезно при массовом скачивании или для доступа к свежим файлам.
![ TOR](https://github.com/tarantin902/TOR/TOR.png)

## Возможности

- Открытие и просмотр директорий на вашем компьютере.
- Отображение файлов в директории по свежести, новые файлы вверху списка.
- Возможность выбрать директорию с помощью кнопки "Выбрать папку".
- Простой и понятный интерфейс для быстрого доступа к своим файлам.

## Использование

1. Запустите программу TOR.
2. Нажмите кнопку "Выбрать папку" и выберите директорию, которую вы хотите исследовать.
3. После выбора директории, список файлов и поддиректорий будет отображен на экране.
4. Файлы сортируются по времени создания, с новыми файлами вверху списка.
5. Чтобы открыть выбранный файл или директорию, просто нажмите на него в списке.

## Зависимости

Для корректной работы программы, убедитесь, что у вас установлены следующие библиотеки:

- [os](https://docs.python.org/3/library/os.html)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [filedialog](https://docs.python.org/3/library/dialog.html)
- [Scrollbar](https://docs.python.org/3/library/tkinter.ttk.html#scrollbar)
- [Listbox](https://docs.python.org/3/library/tkinter.html#listbox)

## Установка

Для установки библиотеки, выполните следующую команду:

```bash
pip install -r requirements.txt

также есть виндовс версия , в папке (\windows\TOR\TOR.exe) просто запустить TOR.exe
TOR.zip в нем есть папка , там виндовс версия програмы запакована через pyinstaller в исполняемый вормат
для виндовса.. что бы не парится ..а открыть сразу
