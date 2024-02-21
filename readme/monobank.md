# Недоліки існуючої інтеграції Wallet - Monobank

### [Синхронізація даних:](https://support.budgetbakers.com/hc/en-us/articles/7152012249618-How-often-does-my-bank-account-data-update)
Дані оновлюються автоматично раз на 24 години, уночі. Якщо оновлення даних не відбулося з якихось причин, то потрібно чекати ще 24 години.

Ініціювати синхронізацію даних вручну неможливо.

### [Період синхронізації:](https://support.budgetbakers.com/hc/en-us/articles/7183726011538-How-many-transactions-will-appear-in-Wallet-when-I-first-connect-to-my-bank)
Коли ви вперше налаштовуєте інтеграцію з банком, то вивантажються всі транзакції за останні 3 місяці. Обрати період неможливо.

Вручну видалити непотрібні транзакції також не можна, та є ~~лайфхак~~ [костиль](https://www.reddit.com/r/BudgetBakers/comments/1af31q1/new_year_new_expense_tracking_app/)

### Видалення транзакцій:
Немає змоги видалити транзакції з приєднаних рахунків. А з 

### Правильність заповнення даних:
[Monobank API](https://api.monobank.ua/docs/index.html#tag/Kliyentski-personalni-dani/paths/~1personal~1statement~1{account}~1{from}~1{to}/get) віддає поля: 
> comment - коментар до переказу, уведений користувачем. Якщо не вказаний, поле буде відсутнім.

> description - опис транзакцій. В цьому полі також вказується платник або отримувач.

Wallet об'єднує comment та description та додає в додатку в поле Нотатка (Note).