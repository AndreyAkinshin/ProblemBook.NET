# «Rounding1» (Решение)

## Ответ

```
| Number | Round | Floor | Ceiling | Truncate | Format |
|   -2.9 |    -3 |    -3 |      -2 |       -2 |     -3 |
|   -0.5 |     0 |    -1 |       0 |        0 |     -1 |
|    0.3 |     0 |     0 |       1 |        0 |      0 |
|    1.5 |     2 |     1 |       2 |        1 |      2 |
|    2.5 |     2 |     2 |       3 |        2 |      3 |
|    2.9 |     3 |     2 |       3 |        2 |      3 |
```

## Объяснение

Если число находится ровно посередине между двумя возможными вариантами, то работают следующие правила:

[Math.Round](http://msdn.microsoft.com/library/system.math.round.aspx) по умолчанию округляет к ближайшему чётному целому.

[Math.Floor](http://msdn.microsoft.com/library/system.math.floor.aspx) округляет вниз по направлению к отрицательной бесконечности.

[Math.Ceiling](http://msdn.microsoft.com/library/system.math.ceiling.aspx) округляет вверх по направлению к положительной бесконечности.

[Math.Truncate](http://msdn.microsoft.com/library/system.math.truncate.aspx) округляет вниз или вверх по направлению к нулю.

[String.Format](http://msdn.microsoft.com/library/system.string.format.aspx) округляет к числу, которое дальше от нуля (см. также [Standard Numeric Format Strings](http://msdn.microsoft.com/en-us/library/dwhawy9k.aspx), [Custom Numeric Format Strings](http://msdn.microsoft.com/en-us/library/0c899ak8.aspx)).

[Задача](./Rounding1-P.md)