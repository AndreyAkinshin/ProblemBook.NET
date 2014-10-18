# “AugmentedAssignment” (Problem)

What will the following code display?

```cs
int a = 0;
int Foo()
{
  a = a + 42;
  return 1;
}
void Main()
{
  a += Foo();
  Console.WriteLine(a);
}
```

[Solution](./AugmentedAssignment-S.md)