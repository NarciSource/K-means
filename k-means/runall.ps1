$arr = @("cup","cute","potato")

For($i=0;$i -le 2; $i++)
{
    For($j=2;$j -le 10; $j++)
    {
        $name = $arr[$i]
        python .\src\python\run1.py .\data\input\$name.jpg $j 100
        python .\src\python\run1.py .\data\input\$name.png $j 100
    }
    mkdir .\data\output\$name\dat
    mkdir .\data\output\$name\img
    mv *.dat .\data\output\$name\dat
    mv *.jpg .\data\output\$name\img
    mv *.png .\data\output\$name\img
}
