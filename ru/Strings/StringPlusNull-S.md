# «StringPlusNull» (Решение)

## Ответ

```
False
```

## Объяснение

Фрагмент из [C# Language Specification](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=DFBF523C-F98C-4804-AFBD-459E846B268E), раздел 7.8.4 Addition operator:

«String concatenation:

```cs
string operator +(string x, string y);
string operator +(string x, object y);
string operator +(object x, string y);
```

These overloads of the binary + operator perform string concatenation. **If an operand of string concatenation is null, an empty string is substituted**. Otherwise, any non-string argument is converted to its string representation by invoking the virtual ToString method inherited from type object. If ToString returns null, an empty string is substituted.»

Другими словами, при строковых операциях `null` превращается в пустую строку. Таким образом:

```cs
((string)null + null + null) == ("" + null + null) ==
  (("" + null) + null) == (("" + "") + null) == ("" + null) ==
  ("" + "") == ""
"" != null
```

## Ссылки

* [Microsoft Reference Source](http://referencesource.microsoft.com/#mscorlib/system/string.cs)
* [Mono 3.10.0 Source](https://github.com/mono/mono/blob/mono-3.10.0/mcs/class/corlib/System/String.cs)

[Задача](./StringPlusNull-P.md)