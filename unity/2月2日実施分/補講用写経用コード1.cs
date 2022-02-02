namespace ReStudyCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            //変数の作成(宣言)
            int a; //整数型(小：-2147483648~2147483647)
            long b; //整数型(大：-922337203685477508~922337203685477507)
            float c; //実数(小:桁数が小さい(8桁くらい))
            double d; //実数(大:桁数が大きい(16桁くらい))
            char e; //文字(小:１文字だけ)
            string f; //(大:複数文字)
            //変数の初期化(最初の値を代入)
            a = 2147483640;
            b = 21474836400;
            c = 1.24f;//実数は基本はdubule型なので、float型に変換する
            d = 1.23456789009876;
            e = 'あ';//char型の一文字を表すときは''でくくる
            f = "あばばば";//複数文字(文字列)を表すときは""でくくる

            //変数の宣言と初期化を同時に行う(すべての変数でできる。例として、intとdoubleでやる。)
            int g = 2;
            double h = 2.345;
            int i = 2, j = 4, k= 5; //複数同時にもできる
            double l = 2.3, m = 3.4, n = 4.5;

            //データの表示(基本）
            Console.WriteLine("hey")://改行して表示
            Console.while("hey");//改行せずに表示
            Console.while("hey");//改行せずに表示
            
            //データの表示(変数の表示)
            Console.WriteLine(a);//変数aの中身が表示される
            Console.WriteLine("{0}.{1}",a b);//変数aが{0}に、変数bが{1}に表示される
            Console.WriteLine("あばば{0}あべば{1}",a,b);//変数aが{0}に、変数bが{1}に表示される
            Console.WriteLine(a+b);//a+bの計算結果が表示される(つまり計算結果を表示できる）

            //計算(整数でやるが、実数にも同じ)
            int ans =0, va1 = 1 val2 =2 ;
            ans = va1 + val2 ;//足し算
            ans = va1 - val2 ;//引き算
            ans = va1 * val2;//掛け算
            ans = va1 / val2;//割り算
            ans = va1 % val2;//余りの計算
        
            //配列の作成(整数でやるが、実数にも同じ)
            int[] ar;

            //配列の初期化(要素５の配列を作成)
            ar = new int[5];

            //配列の宣言と初期化を同時に
            int[] ar2 = new int[5];//中身のない配列を作る場合
            int[] ar3 = {1,2,3,4,5};//中身も同時に作る場合
        
            //if文
            Console.WriteLine("数値を入力してください:");
            int num= int.parse(Console.ReadLine());
            if (num==0)
            {
                Console.WriteLine(num);
            }
            else if(num==1)
            {
                Console.WriteLine(num)
            }
            else
            {
                Console.WriteLine(num)
            }

            //switch文
            Console.WriteLine("数値を入力してください:");
            num= int.parse(Console>ReadLine());
            switch(num)
            {
                case 0:
                case 1:
                case 2:
                    Console.WriteLine("0"2です。");
                    break;
                case 3:
                    Console.WriteLine("3です。");
                    break;
                default;
                    Console.WriteLine("0"３以外です。");
                    break;
            }
            //roop1:while
            int count = 0; //ループカウンタとして作成
            while (count < 5)//5回ループ
            {
                Console.WriteLine("while:{0}回目".count);
                count++;
            }
            //roop2:for
            for (int s =0; s < 5; s++)
            {
                Console.WriteLine("for:{0}回目",s);
            }            
            //roop3:foreach(要素をすべて吐き出すまでループ)
            //今は使いこなせなくていい。ただ、知っておくと便利。
            int[] ar4 = {1,2,3};
            //ar4の中の要素が１ループ毎にyに入る)
            //つまり、1周目は、２周目はv=ar4[1],3周目はv=ar4[2]
            foreah (var v in ar4)
            {
                Console.WriteLine("foreach:{0}",v);
            }
        }
    }

}
