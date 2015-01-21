# «StaticFieldInGenericType» (Решение)

## Ответ

```
0
```

## Объяснение

Классы `Foo<int>` и `Foo<double>` — это два разных класса, у каждого из них собственное статитческое поле `Bar`.

CSharp Language Specification 5.0, 10.5.1: «When a field declaration includes a  static modifier, the fields introduced by the declaration are static fields. When no  static modifier is present, the fields introduced by the declaration are instance fields. Static fields and instance fields are two of the several kinds of variables (§5) supported by C#, and at times they are referred to as static variables and instance variables, respectively. A static field is not part of a specific instance; instead, it is shared amongst all instances of a closed type (§4.4.2). No matter how many instances of a closed class type are created, there is only ever one copy of a static field for the associated application domain.»

## Ссылки

* [Microsoft Code Analysis for Managed Code Warnings, CA1000](https://msdn.microsoft.com/library/ms182139.aspx)
* [ReSharper wiki: Static field in generic type](https://confluence.jetbrains.com/display/ReSharper/Static+field+in+generic+type)

[Задача](./StaticFieldInGenericType-P.md)