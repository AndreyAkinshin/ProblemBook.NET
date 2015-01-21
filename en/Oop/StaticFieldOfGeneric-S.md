# “StaticFieldOfGeneric” (Solution)

## Answer

```
0
```

## Explanation

The `Foo<int>` and `Foo<double>` are two different classes. Each of them has own static `Bar` field.

CSharp Language Specification 5.0, 1.6.5: “A static field identifies exactly one storage location. No matter how many instances of a class are created, there is only ever one copy of a static field”.

CSharp Language Specification 5.0, 4.4: “A generic type declaration, by itself, denotes an unbound generic type that is used as a “blueprint” to form many different types, by way of applying type arguments”.

[Problem](./StaticFieldOfGeneric-P.md)