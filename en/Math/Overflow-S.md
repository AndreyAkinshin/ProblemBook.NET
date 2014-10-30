# “Overflow” (Solution)

```
Checked   Int32   increased max: OverflowException
Checked   Double  increased max: 1,79769313486232E+308
Checked   Decimal increased max: OverflowException
Unchecked Int32   increased max: -2147483607
Unchecked Double  increased max: 1,79769313486232E+308
Unchecked Decimal increased max: OverflowException
```

Overflow operations with `sbyte`, `byte`, `short`, `ushort`, `int`, `uint`, `long`, `ulong`, `char` throw `OverflowException` depending on `checked`/`unchecked` context (ECMA-334, 11.1.5).

Overflow operations with `float`, `double` never throw `OverflowException` (ECMA-334, 11.1.6).

Overflow operations with `decimal` always throw `OverflowException` (ECMA-334, 11.1.7).

[Problem](./Overflow-P.md)