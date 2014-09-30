# «CaseInComparison» (Решение)

Нет, в некоторых локалях результат будет разный. Пример:

```cs
var a = "i";
var b = "I";
Thread.CurrentThread.CurrentCulture = 
  CultureInfo.CreateSpecificCulture("tr-TR");
Console.WriteLine(
  string.Compare(a.ToUpper(), b)); //'1'
Console.WriteLine(
  string.Compare(a, b, StringComparison.OrdinalIgnoreCase)); //'0'
```

См. [The Turkey Test](http://www.moserware.com/2008/02/does-your-code-pass-turkey-test.html).

[Задача](./CaseInComparison-Q.md)