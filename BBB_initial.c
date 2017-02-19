#include "stdio.h"
#include"stdlib.h"
#include"string.h"

#define GPIO_DIR "/sys/class/gpio/"
#define GPIO_WRITE "out"
#define GPIO_READ "in"


int no_gpio_int;
int date_gpio_int;


int write_gpio(int w_no_gpio_int,int value)
{	

	char no_gpio_str[3];
	char gpio_value_add_str[50];
	char gpio_mode_add_str[50];
	char gpio_mode_str[4];
	char gpio_value_str[2];

	FILE *stream = NULL;

	//change into date mode into string for function to use
	
	printf("try to change date mode\n");
	sprintf(gpio_mode_add_str,GPIO_DIR"gpio%d/direction",w_no_gpio_int);
	sprintf(gpio_value_str,"%d",value);		
	sprintf(gpio_value_add_str,GPIO_DIR"gpio%d/value",w_no_gpio_int);
	printf("date mode change success\n");	

	//set gpio mode if not avaliable initial gpio and set mode
	stream = fopen(gpio_mode_add_str,"r+");
		
    sprintf(no_gpio_str,"%d",w_no_gpio_int);

    stream = fopen(GPIO_DIR"export","w");
    fwrite(no_gpio_str,sizeof(char),2,stream);
    fclose(stream);

    printf("initial finish, try to read mode again\n");
    stream = fopen(gpio_mode_add_str,"r+");




	//change mode

    fwrite(GPIO_WRITE,sizeof(char),3,stream);
    printf("change finish\n");
	fclose(stream);
	

	//write value
	printf("try to write date\n");
	stream = fopen(gpio_value_add_str,"r+");
	fwrite(gpio_value_str,sizeof(char),2,stream);
	fclose(stream);
	printf("date write finish\n\n\n");

	return 0;

}



//return value is the value that read by  gpio 
int read_gpio(int w_no_gpio_int)
{	
	
	int gpio_value_int;
	char no_gpio_str[3];
	char gpio_value_add_str[50];
	char gpio_value_str[2];
	char gpio_mode_add_str[50];
	char gpio_mode_str[4];

	FILE *stream = NULL;

	//change date mode into string for function to use
	
	printf("try to change date mode\n");
	sprintf(gpio_mode_add_str,GPIO_DIR"gpio%d/direction",w_no_gpio_int);
	sprintf(gpio_value_add_str,GPIO_DIR"gpio%d/value",w_no_gpio_int);
	printf("date mode change finish\n");

	//set gpio mode if not avaliable initial gpio and set mode
	
	stream = fopen(gpio_mode_add_str,"r+");
	fscanf(stream,"%s",gpio_mode_str);
	printf("gpio mode is %s",gpio_mode_str);
	fclose(stream);
	

	//read value
	stream = fopen(gpio_value_add_str,"r");
	fscanf(stream,"%s",gpio_value_str);
    printf("gpio value is %s",gpio_value_str);
	fclose(stream);
	printf("read finish\n\n\n");
    return 0;

}

void adc_install(void)
{
    FILE *stream = NULL;

    stream=fopen("/sys/devices/bone_capemgr.9/slots","w");
    fwrite("BB-ADC",sizeof(int),6,stream);
    fclose(stream);
}


int main()
{
    write_gpio(66,0);
    read_gpio(66);
    
    write_gpio(67,0);
    read_gpio(67);
    
    write_gpio(69,0);
    read_gpio(69);
    
    write_gpio(68,0);
    read_gpio(68);
    
    write_gpio(45,0);
    read_gpio(45);
    
    adc_install();
    
}
