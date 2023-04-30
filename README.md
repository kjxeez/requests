# requests
1. Если вы для выполнения заданий используете утилиту, отличную от curl, HTTPie или Postman, то кратко опишите ее. Если вы используете язык программирования, то кратко опишите библиотеку, которую используете или встроенные средства самого языка. 

#### Requests для Python - это простой в использовании HTTP-клиент для языка Python, который позволяет отправлять HTTP/1.1 запросы к веб-серверам. Она поддерживает большое количество функций, таких как автоматическая поддержка cookies, установка заголовков, SSL-верификация и т.д. Requests позволяет легко работать с HTTP-сессиями, авторизацией и аутентификацией.

2. Используя сервис httpbin.org сформируйте и передайте GET запрос с двумя параметрами:
• fname — значение этого параметра ваше имя, записанное латиницей;
• lname — ваша фамилия, также записанная латиницей.
Отобразите содержимое HTTP запроса (первую строку, заголовок и тело) сперва с помощью
той утилиты, которой вы пользуйтесь, а потом с изучив ответ с сервера. Есть ли между ними
разница?

### requests:

![image](https://user-images.githubusercontent.com/82978703/234848080-9d376827-1a1a-4126-82f4-146f6dcb6356.png)

### other way:

![image](https://user-images.githubusercontent.com/82978703/234842081-a1b7d2f1-5be4-4db6-a114-fd5198ada82d.png)

3. По какому адресу нужно совершить GET запрос, чтобы httpbin его корректно обработал?
#### https://httpbin.org/get или  "url": "https://httpbin.org/get?fname='Isabella'&lname='Akopyan'"

4. Отобразите заголовок HTTP ответа, который прислал вам сервер. Объясните назначение каждого из полей данного заголовка.

![image](https://user-images.githubusercontent.com/82978703/234848137-e3067ff7-bcda-470d-8059-c8e80d8ba638.png)

#### User-Agent
Содержит информацию о программе, которая инициировала запрос (в данном случае python-requests/2.29.0). Это позволяет серверу знать, какой тип клиента (браузер, почтовый клиент, скрипт и т.д.) делает запрос, чтобы он мог оптимизировать ответы под этот тип клиента.
#### Accept-Encoding
Определяет, какие кодировки содержимого клиент может принять, в данном случае gzip и deflate (сжатые форматы).
#### Accept
Указывает типы содержимого, которые клиент готов принять в ответе. Здесь указан тип application/json, что означает, что клиент ожидает ответ в формате JSON.
#### Connection
Указывает тип соединения, в данном случае keep-alive, что означает, что клиент желает установить постоянное соединение с сервером для повторного использования его в будущем.

5. В какой части HTTP сообщения были отправлены параметры fname и lname?

#### Параметры fname и lname были отправлены в части URL, как часть query-строки (стартовая строка). В данном случае, они были переданы в качестве параметров в requests.get(), который затем включил их в URL запроса. Таким образом, полный URL запроса выглядел следующим образом: https://httpbin.org/get?fname=Isabella&lname=Akopyan.
С

6. Теперь отправьте на сервер POST запрос, передав параметры fname, lname и stdnum, где
stdnum — номер вашего студенческого билета. Необходимо, чтобы сервер воспринял эти параметры как поля вебформы.

#### Вместо params нужно использовать data, чтобы передавать параметры в теле запроса в виде полей формы.

![image](https://user-images.githubusercontent.com/82978703/234853756-795334dd-0b41-4699-b50c-3deac0992ed2.png)

#### Здесь мы используем параметр data для передачи данных в виде полей формы, а также указываем соответствующий заголовок Content-Type.

7. Отобразите содержимое HTTP запроса (первую строку, заголовок и тело). Какое поле заголовка HTTP сообщения указывает, что переданные данные являются полями вебформы?

![image](https://user-images.githubusercontent.com/82978703/234867780-1be0d0b9-83cf-4b68-918b-555848383523.png)
![image](https://user-images.githubusercontent.com/82978703/234867890-a8f1775d-2ecb-4a59-b4bb-70b76940518a.png)
![image](https://user-images.githubusercontent.com/82978703/234867950-ed2292fc-4ff8-451a-9d08-f478a6d17ba5.png)

![image](https://user-images.githubusercontent.com/82978703/234868031-9f6a518c-1363-4628-8a59-eeec78970ccc.png)

Content-Type указывает на то, что переданные данные являются полями вебформы

8. По какому адресу вы отправили запрос?

#### По адресу url2 'https://httpbin.org/post'

9. В какой части HTTP сообщения содержатся пересылаемые параметры?

#### данные параметры были переданы в заголовке запроса в строке `headers2` в формате, указываемом в параметре `'Content-Type': 'application/x-www-form-urlencoded'`.

#### Тело HTTP-ответа содержит информацию, полученную в отклике на Ваш запрос, и также содержит параметры, переданные Вами в качестве формы с именами параметров "fname", "lname" и "stdnum": 

```
"form": {
    "fname": "Isabella", 
    "lname": "Akopyan", 
    "stdnum": "1032203961"
  }
  -> в теле
10. Перешлите те же параметры в виде JSON документа. Какие поля нужно установить в заголовке HTTP сообщения, чтобы сервер воспринял передаваемое сообщение как JSON документ

#### Чтобы передать параметры в виде JSON, нужно изменить тип контента в заголовке запроса на "application/json"

11. В какой части HTTP сообщения передается JSON документ?

