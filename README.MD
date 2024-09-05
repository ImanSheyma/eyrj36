# Запуск
- клонируем репозитрий (https://github.com/ImanSheyma/eyrj36)
- "поднимаем" сервисы командой: 
```
  docker compose up
```
- по ссылке http://localhost:5000/form переходим к странице с формой

# Установка docker (если требуется):

Обновление установленных пактов
```
  sudo apt update
```
Установим необходимые пакеты
```
  sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
Добавим Docker репозиторий
```
  curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
снова обновим пакеты
```
  sudo apt update
```
установим Docker Engine
```
  sudo apt install docker-ce docker-ce-cli containerd.io
```
запускаем
```
  sudo systemctl start docker
```

```
  sudo systemctl enable docker
```
