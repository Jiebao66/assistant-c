### 计算器程序代码设计要求

1. 将计算器的代码封装成一个函数。
2. 支持多组测试数据。
3. 重定向输入流和输出流到文件。

#### 下面详细阐述要求

1. 将计算器的代码封装成一个函数。在main()函数里面调用该函数。

   看下面的代码

~~~C
void cal(){
	char s[200];
	gets(s);
	printf("答案\n");
}
int main(){
    for(int i = 1; i<=10; i++){
	    cal();    
    }
    return 0;	
}
~~~

2. 支持多组测试数据。

   在上面的代码可以看出来，cal 函数执行了10次。也就是能输入10行计算式，输出10行结果。

3. 重定向输入流和输出流到文件。

   重定向语句的函数定义：

   ~~~C
   // <stdio.h> 头文件包含该函数的定义
   FILE *freopen( const char *filename, const char *mode,FILE *stream );
   ~~~

   重定向输入：

   ​	键盘输入（标准输入 stdin）到文件 data.in

   ~~~C
   //data.in是重定向后的位置，stdin是标准输入即键盘输入,"r"是“只读”模式
   freopen("data.in","r",stdin);
   ~~~

   重定向输出:

   ​	命令行输出（标准输出stdout)到文件data.out

   ~~~C
   // data.out 是重定向后的位置，stdout为标准输出，"w"为"只写"模式
   freopen("data.out","w",stdout);
   ~~~

   在计算器代码中，重定向的代码可以这么写。

   ~~~C
   int quit = 0;
   void cal(){
   	char s[200];
   	if(gets(s)!=NULL){
           printf("答案\n");
   	}
   	else{
           quit = 1;
   	}		
   }
   int main(){
   	freopen("data.out","w",stdout);
   	freopen("data.in","r",stdin);
   	while(quit!=1){
           cal();
   	}
   	return 0;	
   }
   ~~~

   很容易看出代码从 "data.in" 文件读入测试数据，将结果输出在 "data.out" 文件。cal()函数将执行到文件末尾时结束。



#### 加餐，感兴趣的请享用

#### 花式玩法（与计算器程序无关）

​	无论是工程上的编程还是学术上的编程，文件操作都会经常被用到。

​	比如你们在大二上要修的《计算机网络和通信》这门课，完成编程作业时，也会用到文件操作。或者做工程项目，比如写个APP（虽然我还没写过），写个好玩的游戏（去年写过一个）。或者学术研究上，做科学计算，从文件读入大量数据，输出大量数据到文件里。

​	所以大家编程熟练一下文件操作鸭。

​	给你们一个好玩的场景：你的电脑上有些比较重要的文件，比如（日记？情书？价值连城的商业计划？独一无二的学术创作？）你想单独对这些文件加密，怎么办呢？从网上下载一个加密软件？多无挑战性呀！干脆自己随手糊一个！

>Hello everyone in IDT
>
>I'm primelee, assistant  in your coding lesson
>
>How nice it is that I meet you guys in this year.
>
>Hope your coding skill is promoted  after this semester.
>
>Sincerely from primelee

现在随手糊一份代码加密它！

~~~python
#encrypt.py 加密的脚本
#简单的加算法, y = f(ascii(x)+10)
fr = open('raw.txt','r')
fw = open('mimi.txt','w')
for line in fr:
    ac = ''
    for i in line:
        ac += chr(ord(i)+10)
    fw.write(ac)
~~~



~~~python
#decrypt.py 解密脚本
#解密算法，加密的逆运算 : y = f(ascii(x)-10)
fr = open('mimi.txt','r')
fw = open('raw.txt','w')
for line in fr:
    ac = ''
    for i in line:
        ac += chr(ord(i)-10)
    fw.write(ac)
~~~



~~~shell
python encrypt.py
~~~

加密后，生成的文件内容是:

>Rovvy*o?o|?yxo*sx*SN^S1w*z|swovoo*sx*?y|*mynsxq*vo}}yxRy?*xsmo*s~*s}*~rk~*S*woo~*?y*q?}*sx*~rs}*?ok|8Ryzo*?y|*mynsxq*}usvv*s}*z|ywy~on**kp~o|*~rs}*}owo}~o|8]sxmo|ov?*p|yw*z|swovoo

~~~shell
 python decrypt.py 
~~~



解密后，生成的文件内容是：

>Hello everyone in IDT
>
>I'm primelee in your coding lesson
>
>How nice it is that I meet you guys in this year.
>
>Hope your coding skill is promoted  after this semester.
>
>Sincerely from primelee



这个加密的程序非常简单，就拿来对文件操作练练手。

真正的加密程序肯定不会这么简单，要考虑文件的编码，加密算法的复杂度等。

### 路漫漫其修远兮，好好探索吧。

