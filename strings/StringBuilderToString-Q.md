# «StringBuilderToString» (Задача)
Будет ли происходить копирование символьного массива при вызове метода `StringBuilder.ToString()`:?
```cs
var builder = new StringBuilder(10);
for (int i = 0; i < 10; i++)
  builder.Append('a');
var str = builder.ToString();
```
[Решение](./StringBuilderToString-A.md)
