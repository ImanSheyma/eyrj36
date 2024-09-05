# Запуск
- клонируем репозитрий (git clone https://github.com/ImanSheyma/eyrj36)
- "поднимаем" сервисы командой: 
'''
  docker compose up
'''

команды по установке docker (если требуется):
'''
  sudo apt update
'''

'''
  sudo apt install apt-transport-https ca-certificates curl software-properties-common
'''

'''
  curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
  echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
'''

'''
  sudo apt update
'''

'''
  sudo apt install docker-ce docker-ce-cli containerd.io
'''

'''
  sudo systemctl start docker
'''

'''
  sudo systemctl enable docker
'''

по ссылке http://localhost:5000/form переходим к странице с формой
