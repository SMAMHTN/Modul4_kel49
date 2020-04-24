<html>
    <body>
        <h3>Encoded by kelompok 49</h3>
        <h3>"Aldi Mulyawan 21120119120026</h3>
        <h3>"Mochamad Pratama Wibawa 21120119130062"</h3>
        <h3></h3>
        <h1>Data Mahasiswa</h1>
        <h2>Masukkan Data:</h2>
        <form action="./" method="POST" enctype="multipart/form-data">
            <table>
                <tr>
                    <td>Nama</td>
                    <td>:</td>
                    <td><input type="text" name="a" required ></td>
                </tr>
                <tr>
                    <td>NIM</td>    
                    <td>:</td>
                    <td><input type="text" name="b" required ></td>
                </tr>
                <tr>
                    <td>Kelompok</td>
                    <td>:</td>
                    <td><input type="text" name="c" required ></td>
                </tr>
                <tr>
                    <td>Asal</td>
                    <td>:</td>
                    <td><input type="text" name="d" required ></td>
                </tr>
                <tr>
                    <td>Hobi</td>
                    <td>:</td>
                    <td><input type="text" name="e" required ></td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td><input type="submit" name="submit" value="Submit Data"></td>
                </tr>
            </table>
        </form>

        <?php
        if(isset($_POST['submit'])){
            $a    =$_POST['a'];
            $b    =$_POST['b'];
            $c    =$_POST['c'];
            $d    =$_POST['d'];
            $e    =$_POST['e'];

            $call = new Mahasiswa();
            $call->seta($a);
            $call->setb($b);
            $call->setc($c);
            $call->setd($d);
            $call->sete($e);
    
            $f=$call->geta($a);
            $g=$call->getb($b);
            $h=$call->getc($c);
            $i=$call->getd($d);
            $j=$call->gete($e);
    
            echo nl2br(
                "
                ----------------Output Data----------------\n
                Nama : $f \n 
                NIM : $g \n
                Kelompok : $h \n 
                Asal : $i \n
                Hobi : $j \n
                -------------------------------------------\n
                Nama Mahasiswa $f memiliki NIM $g dan dari kelompok $h yang berasal dari $i dan memiliki hobi $j
                "
            ); 
        }


        Class Mahasiswa { 

            private $a;
            private $b;
            private $c;
            private $d;
            private $e;
            
            //membuat setter
            function seta($a) {
                $this->a = $a;
            }
            function setb($b){
                $this->b = $b;
            }
            function setc($c){
                $this->c = $c;
            }
            function setd($d){
                $this->d = $d;
            }
            function sete($e){
                $this->e = $e;
            }
            
            //membuat getter
            function geta() {
                return $this->a;
            }
            function getb() {
                return $this->b;
            }
            function getc() {
                return $this->c;
            }
            function getd() {
                return $this->d;
            }
            function gete() {
                return $this->e;
            }
        }    
        ?>
