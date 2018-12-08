#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h> 
double convert(char *a){
	int n=strlen(a);
	double sum=0;
	for(int i=0;i<n;i++){
		sum=sum+(a[i]-48)*pow(10,n-i-1);          
	}
	return sum;
}
void perform(double sum[],char b[]){           
	int i,j;
	double result=0;
	int n=strlen(b);
	for(i=0;i<n;i++){
    	if(b[i]=='/'){
			sum[i+1]=sum[i]/sum[i+1];
			sum[i]=0;
		}
	}
	for(i=0;i<n;i++){
		if(b[i]=='*'){
			int k=i+1;
			while(sum[k]==0){
				k++;
			}
			sum[i]=sum[i]*sum[k];
			sum[k]=0;
		} 
	}
	for(i=0;i<n;i++){
		if(b[i]=='-'){
			int m=i+1;
			while(sum[m]==0){
				m++;
			}
			sum[i]=sum[i]-sum[m];
			sum[m]=0;
		}
	}
	for(i=0;i<=n;i++){
		result=result+sum[i];
	}
	printf("%.2lf\n",result);
}
int mainx()
{
    
	char function[100];
	int len1;
	gets(function);
	len1=strlen(function);
	int i,j=0,z=0;
	double sum[100]={0};
	char b[100]={'0'};
	for(i=0;i<len1;i++){
		if(function[i]>='0'&&function[i]<='9'){
		    b[j]=function[i];
			j++;
			if(function[i+1]<'0'||function[i+1]>'9'){
				sum[z]=convert(b);
				for(int m=0;m<j;m++){
					b[m]='\0';
				} 
				j=0;
				z++;	
			}		
		}
	}
	char sign[100]={'0'};
	int m=0;
	for(i=0;i<len1;i++){
		if(function[i]<'0'||function[i]>'9'){
			sign[m]=function[i];
			m++;
		}
	}
	perform(sum,sign);
    return 0;
}

int main(){
    //freopen("../../in/simple.data","r",stdin);
    while(1){
        mainx();
    }
}
