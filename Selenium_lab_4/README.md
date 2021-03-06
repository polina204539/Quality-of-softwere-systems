# QA_Selenium
---
## Автоматическое тестирование на Python Selenium

Четвёртое задание по дисциплине Управление Качеством Программных Систем.

Для создания приложения автоматического тестирования сайта я взяла NIKE https://www.nike.com/ru/women из моего первого задания.

## Условия
Для повышения реалистичности тестирования я выбрал 6 логически последовательных тест-кейсов, описывающих "жизненный цикл товара" во время работы пользователя с сайтом.

А именно:
1. Поиск товара на сайте.
2. Сортировка/отсеивание выбранной категории.
3. Добавление товара в список желаемого.
4. Добавление товара в корзину.
5. Удаление товара из корзины.
6. Переход на станицу Instagram NIKE.

## Особенности
Для качественного выбора элементов конкретных страниц я использовала возможности **Selenium** и подключила библиотеку **_selenium.webdriver.common.by_**. Чтобы получить интересующие данные, необходимо всего лишь создать запрос, описывающий эти данные. Поэтому, это простой и эффективный вариант.

Все Тест-кейсы подписаны коомментариями в коде. В консоли отображаются логи. Достаточно запустить файл.
