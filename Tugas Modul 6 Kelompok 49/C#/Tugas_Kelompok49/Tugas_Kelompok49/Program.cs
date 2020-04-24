using System;

namespace Tugas_Kelompok49
{
    internal class Program
    {
        private class Mahasiswa
        {
            private string a;
            private string b;
            private string c;
            private string d;
            private string e;

            public void seta(string val)
            {
                this.a = val;
            }

            public string geta()
            {
                return a;
            }

            public void setb(string val)
            {
                this.b = val;
            }

            public string getb()
            {
                return b;
            }

            public void setc(string val)
            {
                this.c = val;
            }

            public string getc()
            {
                return c;
            }

            public void setd(string val)
            {
                this.d = val;
            }

            public string getd()
            {
                return d;
            }

            public void sete(string val)
            {
                this.e = val;
            }

            public string gete()
            {
                return e;
            }
        }

        private static void Main(string[] args)
        {
            Mahasiswa call = new Mahasiswa();
            Console.Write("Nama : ");
            string a = Console.ReadLine();
            Console.Write("NIM : ");
            string b = Console.ReadLine();
            Console.Write("Kelompok : ");
            string c = Console.ReadLine();
            Console.Write("Hobi : ");
            string d = Console.ReadLine();
            Console.Write("Asal : ");
            string e = Console.ReadLine();
            Console.WriteLine();

            call.seta(a);
            call.setb(b);
            call.setc(c);
            call.setd(d);
            call.sete(e);

            Console.WriteLine(
                "--------------------Output Data---------------------" +
                "\nNama :  " + call.geta() +
                "\nNIM : " + call.getb() +
                "\nKelompok :  " + call.getc() +
                "\nHobi :  " + call.getd() +
                "\nAsal :  " + call.gete() +
                "\n------------------------------------------------\n" +
                "Nama mahasiswa adalah " + call.geta() +
                " dengan NIM " + call.getb() +
                " dari Kelompok " + call.getc() +
                " dan berasal dari " + call.gete() +
                " memiliki Hobi " + call.getd()
                );

            Console.ReadLine();
        }
    }
}