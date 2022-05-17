
![](img/previe.png)

### Description

TCP сервер, который распознает заданный формат данных и отображает его в требуемом формате. Запись данных введется log.txt.

Формат данных BBBBxNNxHH:MM:SS.zhqxGGCR 
- BBBB - номер участника
- x - пробельный символ
- NN - id канала
- HH - Часы 
- MM - минуты
- SS - секунды
- zhq - десятые сотые тысячные 
- GG - номер группы

Пример данных: 0002 C1 01:13:02.877 00

Вывод: спортсмен, нагрудный номер 0002 прошёл отсечку C1 в «01:13:02.8»



### Use
```
$ git clone git@github.com:vladjong/SimpleTCPServer.git
$ cd app/
$ python server.py
$ python client.py
```