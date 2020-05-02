import wpf

from System.Windows import Application, Window, MessageBox

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplication3.xaml')
        
    def button_Click(self, sender, e):
        x = self.textboxNama.Text.ToString()

        if x == "" or self.ComboBoxJk.Text == "" or (self.mkn.IsChecked == False and self.tdr.IsChecked == False and self.jln.IsChecked == False) :
            MessageBox.Show("Belum Diisi")
        else:
            #menentukan Gender
            if self.ComboBoxJk.Text == self.ComboBoxJk.Items.GetItemAt(0).ToString():
                gender = "Mas"
               # MessageBox.Show("Halo Mas "+x+ " yang suka")
            elif self.ComboBoxJk.Text == self.ComboBoxJk.Items.GetItemAt(1).ToString():
                gender = "mbak"
               # MessageBox.Show("Halo Mbak ")
            #menentukan Hobi
            if self.mkn.IsChecked:
                hobi="Makan"
            elif self.tdr.IsChecked:
                hobi="Tidur"
            elif self.jln.IsChecked:
                hobi="Jalan-Jalan"
            MessageBox.Show("Halo "+gender+" "+x+" yang hobinya "+hobi)
            pass
        pass

        
    

if __name__ == '__main__':
    Application().Run(MyWindow())
