# Webim-test-task
### Тестовое задание для компании Webim

При открытии страница показывает кнопку «авторизоваться», по нажатию делает oauth авторизацию github. Страница авторизованного пользователя сразу выводит на экран каждое сгенерированное сервером число, заменяя прошлое. При последующих запусках/заходах на страницу сразу выводит данные сервера, т.к. уже понимает, что авторизовано и авторизация запоминается. Не авторизованные пользователи видеть данные не должны.
Сгенерированные данные для всех пользователей должны совпадать.
На странице должна присутствовать возможность разлогиниться.

## Архитектурный подход:
* Frontend - React + Material UI
* Backend - Flask
* Метод сообщения - Server Sent Event

## Результат:
![gif](https://i.imgur.com/DTyTmqd.gif)
