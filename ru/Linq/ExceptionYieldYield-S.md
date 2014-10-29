# «ExceptionYieldYield» (Решение)

При вызове `evenNumbers.FirstOrDefault()`. Строчки 

```cs
var numbers = GetSmallNumbers();
var evenNumbers = numbers.Select(n => n * 2);
```

только строят запрос, но не исполняют его. Логика `GetSmallNumbers()` начнёт исполняться при первом вызове метода `MoveNext()`, который соответствует вызову `evenNumbers.FirstOrDefault()`. В этот момент и произойдёт `Exception`.

[Задача](./ExceptionYieldYield-P.md)