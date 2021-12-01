Console.WriteLine(System.Environment.GetCommandLineArgs()[1] switch {
    "1" => System.IO.File.ReadLines("input")
        .ToList()
        .Select(int.Parse)
        .Dot(a => a.Zip(a.Skip(1), (a, b) => (a: a, b: b)))
        .Select(ab => ab.a < ab.b ? 1 : 0)
        .Sum(),
    "2" => System.IO.File.ReadLines("input")
        .ToList()
        .Select(int.Parse)
        .Dot(a => a.Zip(a.Skip(1), (a, b) => (a: a, b: b)))
        .Dot(ab => ab.Zip(ab.Skip(1), (ab, bc) => (a: ab.a, b: ab.b, c: bc.b)))
        .Select(abc => abc.a + abc.b + abc.c)
        .Dot(a => a.Zip(a.Skip(1), (a, b) => (a: a, b: b)))
        .Select(ab => ab.a < ab.b ? 1 : 0)
        .Sum(),
    _ => "welp"
});

static class X {
    public static U Dot<T, U>(this T t, Func<T, U> f) => f(t);
}
