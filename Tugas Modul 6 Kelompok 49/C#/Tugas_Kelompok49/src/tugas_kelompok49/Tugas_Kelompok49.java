package tugas_kelompok49;
import java.util.Scanner;

public class Tugas_Kelompok49 {

    public static void main(String[] args) {
        Mahasiswa call = new Mahasiswa();
        Scanner in = new Scanner (System.in);
        System.out.println("----------------Input Data----------------");
        System.out.print("Nama : ");
        String a = in.nextLine();
        System.out.print("NIM : ");
        String b = in.nextLine();
        System.out.print("Umur(Tahun) : ");
        String c = in.nextLine();
        System.out.print("Hobi : ");
        String d = in.nextLine();
        System.out.print("Asal : ");
        String e = in.nextLine();
        System.out.println("------------------------------------------");
        call.seta(a);
        call.setb(b);
        call.setc(c);
        call.setd(d);
        call.sete(e);
        
        String f = call.geta();
        String g = call.getb();
        String h = call.getc();
        String i = call.getd();
        String j = call.gete();
        
        System.out.println("");
        System.out.println("");
        System.out.println("----------------Data Mahasiswa----------------");
        System.out.println("Nama : "+f);
        System.out.println("NIM : "+g);
        System.out.println("Umur : "+h+" Tahun");
        System.out.println("Hobi : "+i);
        System.out.println("Asal : "+j);
        System.out.println("------------------------------------------");
        System.out.println("Mahasiswa dengan nama "+f+" Yang memiliki NIM "+g+", serta berumur "+h+" Tahun dan berasal dari "+j+" Memiliki Hobi "+i);
        
        
        

        
    }
    
}
