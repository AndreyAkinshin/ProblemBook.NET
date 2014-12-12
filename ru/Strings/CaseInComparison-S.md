# «CaseInComparison» (Решение)

## Ответ

Нет.

## Объяснение

В некоторых локалях результат будет разный. Пример:

```cs
var a = "i";
var b = "I";
Thread.CurrentThread.CurrentCulture = 
  CultureInfo.CreateSpecificCulture("tr-TR");
Console.WriteLine(
  string.Compare(a.ToUpper(), b.ToUpper())); //'1'
Console.WriteLine(
  string.Compare(a, b, StringComparison.OrdinalIgnoreCase)); //'0'
```

## Ссылки

* [The Turkey Test](http://www.moserware.com/2008/02/does-your-code-pass-turkey-test.html)

[Задача](./CaseInComparison-P.md)