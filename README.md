### Destination
- A simple script written by python to transfer a large count of libraries from the {username}/.m2/repository/ folder to Nexus.

### Usage
- For the script work, you must have a file settings.xml in the folder {username}/.m2/ with the configuration of the Nexus server, such as
```xml
<servers>
      <server>
      <id>nexus</id> <!-- It will be your repoId -->  
      <username>username</username>
      <password>password</password>
   </server>
</servers>
```
- Use the following command to get a description of the script startup arguments: `python upload_files.py -h`
- Example of using this script: `python upload_files.py -url https://example.com/repository/Example -repoId nexus`

---

### Предназначение

- Простой скрипт, написанный на python для переноса большого количества библиотек из папки {username}/.m2/repository/ в Nexus.

### Использование
- Для работы скрипта, у Вас должен иметься файл settings.xml в папке {username}/.m2/ с конфигурацией сервера Nexus, такого как
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
