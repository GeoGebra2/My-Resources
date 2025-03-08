`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/02/2022 07:45:35 PM
// Design Name: 
// Module Name: clk_div
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module clk_div(   //分频模块
    input clk,    //系统时钟，100 MHz
    input clr,
    output reg [31:0] clk_cnt   
    );
    always@(posedge clk) //100MHz时钟频率下的每一上升沿  
         begin  
             if(clr)       //若清零按键按下，clr=1   
                 clk_cnt = 0 ; //计数变量清零  
             else  
                 clk_cnt = clk_cnt + 1 ; //否则，正常计数  
         end  
endmodule
