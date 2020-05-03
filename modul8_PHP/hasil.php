<html>
     <head>
          <title>Praktikum DKP 2020</title>
     <head>
     <body>
    <table>
      <tr>
        <td>Nama Mahasiswa </td> 
        <td>: <?php echo $nama = $_POST['nama']; ?></td> 
      </tr>
      <tr>
        <td>Nim Mahasiswa</td> 
        <td>: <?php echo $nim = $_POST['nim']; ?></td> 
      </tr>
      
      <tr>
      
        <td><br> <?php $jk = $_POST['jk'];
        if ($jk == 'pria')
            {
            $hasil = 'Selamat datang mas '.$nama; 
            }
            else 
            {
            $hasil = 'Selamat datang mbak '.$nama;
            }       
            
            echo $hasil;?>
            </td> 
      </tr>
      <tr>
      <td>
        Hobby anda adalah : <br>
        <?php 
    if (isset($_POST['check1'])) {  
      echo $_POST['check1']." <br/>";  
        }  
    if (isset($_POST['check2'])) {  
      echo $_POST['check2']." <br/>";  
        }  
    if (isset($_POST['check3'])) {  
      echo $_POST['check3']." <br/>";  
        }  
    if (isset($_POST['check4'])) {  
      echo $_POST['check4']." <br/>";  
        } 
        if (isset($_POST['check5'])) {  
            echo $_POST['check5']." <br/>";  
              } 
              if (isset($_POST['check6'])) {  
                echo $_POST['check6']." <br/>";  
                  } 
        ?></td>
      </tr>
    </table>      
     </body>
</html>
