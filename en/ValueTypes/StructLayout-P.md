# “StructLayout” (Problem)

What will the following code display?

```cs
public struct Foo
{
  public byte Byte1;
  public int Int1;
}
public struct Bar
{
  public byte Byte1;
  public byte Byte2;
  public byte Byte3;
  public byte Byte4;
  public int Int1;
}
void Main()
{
  Console.WriteLine(Marshal.SizeOf(typeof(Foo)));
  Console.WriteLine(Marshal.SizeOf(typeof(Bar)));
}
```

[Solution](./StructLayout-S.md)