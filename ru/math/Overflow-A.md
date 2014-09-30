# «Overflow» (Решение)

```
Checked   Int32   increased max: OverflowException
Checked   Double  increased max: 1,79769313486232E+308
Checked   Decimal increased max: OverflowException
Unchecked Int32   increased max: -2147483607
Unchecked Double  increased max: 1,79769313486232E+308
Unchecked Decimal increased max: OverflowException
```

Операции с переполнением `sbyte`, `byte`, `short`, `ushort`, `int`, `uint`, `long`, `ulong`, `char` выбрасывают исключение `OverflowException` в зависимости от `checked`/`unchecked`-контекста (ECMA-334, 11.1.5).

Операции с переполнением `float`, `double` не выбрасывают исключение `OverflowException` (ECMA-334, 11.1.6).

Операции с переполнением `decimal` всегда выбрасывают исключение `OverflowException` (ECMA-334, 11.1.7).

[Задача](./Overflow-Q.md)