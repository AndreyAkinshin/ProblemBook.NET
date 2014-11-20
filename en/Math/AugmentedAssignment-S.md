# “AugmentedAssignment” (Solution)

## Answer

```
1
```

## Explanation

The construction

```cs
a += Foo();
```

will be transformed to

```cs
a = a + Foo();
```

[Problem](./AugmentedAssignment-P.md)