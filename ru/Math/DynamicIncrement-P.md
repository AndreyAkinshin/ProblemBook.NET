# «DynamicIncrement» (Задача)

Что выведет следующий код?

```cs
byte foo = 1;
dynamic bar = foo;
Console.WriteLine(bar.GetType());
bar += foo;
Console.WriteLine(bar.GetType());
```

[Решение](./DynamicIncrement-S.md)