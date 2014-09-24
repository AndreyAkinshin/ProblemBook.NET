# «Overflow» (Задача)
Что выведет следующий код?
```cs
var maxInt32 = Int32.MaxValue;
var maxDouble = Double.MaxValue;
var maxDecimal = Decimal.MaxValue;
checked
{
  Console.Write("Checked   Int32   increased max: ");
  try { Console.WriteLine(maxInt32 + 42); }
  catch { Console.WriteLine("OverflowException"); }
  Console.Write("Checked   Double  increased max: ");
  try { Console.WriteLine(maxDouble + 42); }
  catch { Console.WriteLine("OverflowException"); }
  Console.Write("Checked   Decimal increased max: ");
  try { Console.WriteLine(maxDecimal + 42); }
  catch { Console.WriteLine("OverflowException"); }
}
unchecked
{
  Console.Write("Unchecked Int32   increased max: ");
  try { Console.WriteLine(maxInt32 + 42); }
  catch { Console.WriteLine("OverflowException"); }
  Console.Write("Unchecked Double  increased max: ");
  try { Console.WriteLine(maxDouble + 42); }
  catch { Console.WriteLine("OverflowException"); }
  Console.Write("Unchecked Decimal increased max: ");
  try { Console.WriteLine(maxDecimal + 42); }
  catch { Console.WriteLine("OverflowException"); }
}
```
[Решение](./Overflow-A.md)
