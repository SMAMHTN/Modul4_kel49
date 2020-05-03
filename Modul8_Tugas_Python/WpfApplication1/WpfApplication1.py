import wpf

from System.Windows import Application, Window, MessageBox

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplication1.xaml')
    

    def button_Click(self, sender, e):
        x = self.textboxNama.Text.ToString()
        y = self.textboxEmail.Text.ToString()

        if x == "" or y == "" or self.ComboBoxJk.Text == "" or (self.low.IsChecked == False and self.medium.IsChecked == False and self.high.IsChecked == False) :
            MessageBox.Show("Mohon Data Datanya Dilengkapi")
        else:
            if self.ComboBoxJk.Text == self.ComboBoxJk.Items.GetItemAt(0).ToString():
                gender = "Bapak"
            elif self.ComboBoxJk.Text == self.ComboBoxJk.Items.GetItemAt(1).ToString():
                gender = "Ibu"

            if self.low.IsChecked:
                tabungan="Reguler"
                gbunga=1
            elif self.medium.IsChecked:
                tabungan="Gold"
                gbunga=2
            elif self.high.IsChecked:
                tabungan="Platinum"
                gbunga=3

            for x in gbunga:
                bunga=x*5

            MessageBox.Show("Terima Kasih "+gender+" "+x+", Anda telah Membuka Tabungan  "+tabungan +" Dengan bunga per bulan "+bunga+".\n\nEmail Verivikasi telah dikirimkan ke : "+y)
            pass
        pass
    
        


if __name__ == '__main__':
    Application().Run(MyWindow())
