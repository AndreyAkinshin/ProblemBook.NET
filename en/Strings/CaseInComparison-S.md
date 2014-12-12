# “CaseInComparison” (Solution)

## Answer

No.

## Explanation

It depends from current CultureInfo. An example:

```cs
var a = "i";
var b = "I";
Thread.CurrentThread.CurrentCulture = 
  CultureInfo.CreateSpecificCulture("tr-TR");
Console.WriteLine(
  string.Compare(a.ToUpper(), b.ToUpper())); //'1'
Console.WriteLine(
  string.Compare(a, b, StringComparison.OrdinalIgnoreCase)); //'0'
```

## Links

* [The Turkey Test](http://www.moserware.com/2008/02/does-your-code-pass-turkey-test.html)

[Problem](./CaseInComparison-P.md)