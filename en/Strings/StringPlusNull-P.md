# “StringPlusNull” (Problem)

What will the following code display?

```cs
try
{
  Console.WriteLine(((string)null + null + null) == null);
}
catch (Exception e)
{
  Console.WriteLine(e.GetType());
}
```

[Solution](./StringPlusNull-S.md)