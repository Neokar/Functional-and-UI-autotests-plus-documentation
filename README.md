# Module-28-Finall-project
Функциональное и UI тестирование сайта https://b2c.passport.rt.ru/ Описание того, что именно делает конкретный тест, можно найти в коде самих тестов

Для запуска необходимы библиотеки pytest, selenium (версия 4) и webdriver для браузера (в проекте приложен драйвер для браузера Chrome 108 версии). Если версия вашего браузера отличается от 108, то необходимый драйвер можно скачать по ссылке https://chromedriver.chromium.org/downloads

Команда для запуска тестов: pytest -v --driver Chrome --driver-path <путь до webdriver> 

Пример: pytest -v --driver Chrome --driver-path D:/chromedriver.exe
