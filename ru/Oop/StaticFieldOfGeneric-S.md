# «StaticFieldOfGeneric» (Решение)

## Ответ

```
0
```

## Объяснение

Классы `Foo<int>` и `Foo<double>` — это два разных класса, у каждого из них собственное статитческое поле `Bar`.

CSharp Language Specification 5.0, 1.6.5: «A static field identifies exactly one storage location. No matter how many instances of a class are created, there is only ever one copy of a static field».

CSharp Language Specification 5.0, 4.4: «A generic type declaration, by itself, denotes an unbound generic type that is used as a “blueprint” to form many different types, by way of applying type arguments».

[Задача](./StaticFieldOfGeneric-P.md)