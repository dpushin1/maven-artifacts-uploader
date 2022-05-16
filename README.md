### Предназначение

- Простой скрипт, написанный на python для переноса большого количества библиотек из папки username/.m2/repository/ в Nexus.

### Использование
- Для работы скрипта, у Вас должен иметься файл settings.xml в папке username/.m2/ с конфигурацией сервера Nexus, такого как
```xml
<servers>
      <server>
      <id>nexus</id> <!-- It will be your repoId -->  
      <username>username</username>
      <password>password</password>
   </server>
</servers>
```
- Используйте следующую команду для получения описания аргументов запуска скрипта: `python upload_files.py -h`
- Пример использования скрипта: `python upload_files.py -url https://example.com/repository/Example -repoId nexus`
