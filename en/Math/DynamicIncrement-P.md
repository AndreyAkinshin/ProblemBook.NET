# “DynamicIncrement” (Problem)

What will the following code display?

```cs
byte foo = 1;
dynamic bar = foo;
Console.WriteLine(bar.GetType());
bar += foo;
Console.WriteLine(bar.GetType());
```

[Solution](./DynamicIncrement-S.md)