# «CurrentCulture» (Задача)

Рассмотрим следующий код:

```cs
Thread.CurrentThread.CurrentUICulture = 
  CultureInfo.CreateSpecificCulture("ru-RU");
Thread.CurrentThread.CurrentCulture = 
  CultureInfo.CreateSpecificCulture("en-US");
var dateTime = new DateTime(2014, 12, 31, 13, 1, 2);
Console.WriteLine(dateTime);
```

В какой локали будет отформатирована дата?

[Решение](./CurrentCulture-S.md)