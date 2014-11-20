# “InheritanceNestedClass” (Solution)

## Answer

```
Foo.Quux()
```

## Explanation

The `Bar.Quux` class is declared in `private` scope, you can't use it from a child class. Thus, the call of the `Quux` method from the `Baz` class will be used the `Foo.Quux` class.

[Problem](./InheritanceNestedClass-P.md)