# “AugmentedAssignment” (Solution)

```
1
```

The construction

```cs
a += Foo();
```

will be transformed to

```cs
a = a + Foo();
```

[Problem](./AugmentedAssignment-P.md)