// See https://aka.ms/new-console-template for more information
Console.WriteLine("Client API in C#");
string url = "http://127.0.0.1:5000/house";
while (true)
{
    Console.Write("Saisir une surface: ");
    string s = Console.ReadLine();
    if (s == "") break;
    var client = new HttpClient();
    Console.WriteLine($"Appel de {url}/{s}");
    var result = await client.GetAsync($"{url}/{s}");
    var json = await result.Content.ReadAsStringAsync();
    var loyer = float.Parse(json);
    Console.WriteLine($"Loyer estimé: {(int)loyer} Euro");
}


