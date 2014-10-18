# “StringBuilderToString” (Problem)

Will be copying the character array when calling `StringBuilder.ToString ()`:?

```cs
var builder = new StringBuilder(10);
for (int i = 0; i < 10; i++)
  builder.Append('a');
var str = builder.ToString();
```

[Solution](./StringBuilderToString-S.md)