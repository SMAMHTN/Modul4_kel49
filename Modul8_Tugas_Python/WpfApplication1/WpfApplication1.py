import wpf

from System.Windows import Application, Window, MessageBox

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplication1.xaml')
    

    def button_Click(self, sender, e):
        x = self.textboxNama.Text.ToString()
        y = self.textboxEmail.Text.ToString()
        z = self.textboxSaldo.Text.ToString()
        a = int(z)

        if x == "" or y == "" or self.ComboBoxJk.Text == "" or (self.low.IsChecked == False and self.medium.IsChecked == False and self.high.IsChecked == False) :
            MessageBox.Show("Mohon Data Datanya Dilengkapi")
        else:
            if self.ComboBoxJk.Text == self.ComboBoxJk.Items.GetItemAt(0).ToString():
                gender = "Bapak"
            elif self.ComboBoxJk.Text == self.ComboBoxJk.Items.GetItemAt(1).ToString():
                gender = "Ibu"

            if self.low.IsChecked:
                tabungan="Reguler"
                bunga = "5%"
            elif self.medium.IsChecked:
                tabungan="Gold"
                bunga = "10%"
            elif self.high.IsChecked:
                tabungan="Platinum"
                bunga="20%"

            if a<100000:
                MessageBox.Show("Saldo Tidak Mencukupi")
                pass
            else:
                MessageBox.Show("Terima Kasih "+gender+" "+x+", Anda telah Membuka Tabungan  "+tabungan +" Dengan bunga per bulan "+bunga+".\n\nEmail Verivikasi telah dikirimkan ke : "+y+"\n Saldo Awal anda adalah : "+z)
                pass
            pass
        pass
    
        


if __name__ == '__main__':
    Application().Run(MyWindow())
