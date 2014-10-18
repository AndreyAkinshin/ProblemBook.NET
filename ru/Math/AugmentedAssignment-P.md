# «AugmentedAssignment» (Задача)

Что выведет следующий код?

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

[Решение](./AugmentedAssignment-S.md)