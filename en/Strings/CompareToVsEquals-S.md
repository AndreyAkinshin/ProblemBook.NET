# “CompareToVsEquals” (Solution)

## Answer

Yes.

## Explanation

`CompareTo` executes according to CultureInfo, `Equals` — without.

An example: the string `"ß"` ([Eszett ](https://en.wikipedia.org/wiki/%C3%9F), \u00df) and `"ss"` will be equal by `CompareTo` in German CultreInfo.

The `==` operator works like the `String.Equals` method.

[Problem](./CompareToVsEquals-P.md)