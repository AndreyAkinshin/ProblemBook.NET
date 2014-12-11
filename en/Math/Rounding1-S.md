# “Rounding1” (Solution)

## Answer

```
| Number | Round | Floor | Ceiling | Truncate | Format |
|   -2.9 |    -3 |    -3 |      -2 |       -2 |     -3 |
|   -0.5 |     0 |    -1 |       0 |        0 |     -1 |
|    0.3 |     0 |     0 |       1 |        0 |      0 |
|    1.5 |     2 |     1 |       2 |        1 |      2 |
|    2.5 |     2 |     2 |       3 |        2 |      3 |
|    2.9 |     3 |     2 |       3 |        2 |      3 |
```

## Explanation

If the number is exactly halfway between two possibilities, the following rules will work:

* [Math.Round](http://msdn.microsoft.com/library/system.math.round.aspx) rounds to the nearest even integer (by default).
* [Math.Floor](http://msdn.microsoft.com/library/system.math.floor.aspx) rounds down towards the negative infinity.
* [Math.Ceiling](http://msdn.microsoft.com/library/system.math.ceiling.aspx) rounds up towards the positive infinity.
* [Math.Truncate](http://msdn.microsoft.com/library/system.math.truncate.aspx) rounds down or up towards zero.
* [String.Format](http://msdn.microsoft.com/library/system.string.format.aspx) rounds towards the number away from zero.

## Links

* [Standard Numeric Format Strings](http://msdn.microsoft.com/en-us/library/dwhawy9k.aspx)
* [Custom Numeric Format Strings](http://msdn.microsoft.com/en-us/library/0c899ak8.aspx)

[Problem](./Rounding1-P.md)