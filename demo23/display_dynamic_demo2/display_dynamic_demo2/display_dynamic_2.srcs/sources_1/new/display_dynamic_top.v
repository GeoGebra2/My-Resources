`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/02/2022 07:37:48 PM
// Design Name: 
// Module Name: display_dynamic_top
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
//4位数码管动态显示相同数字，拨码开关控制数码管亮灭，通过分频计数器动态改变显示的数，显示频率可调节。

//本模块为顶层模块，通过调用时钟分频模块和数码管控制模块实现功能

module display_dynamic_top(
    input clk_sys,   //100 MHz时钟源
    input clr_key,   //清零
    input [3:0] switch_bit,    //拨码开关，控制数码管位选
    output [3:0] display_bit,  //数码管位选
    output [6:0] display_segment   //数码管段选
    );

wire [31:0] clk_cnt_temp ; //中间变量，存储时钟源分频计数结果  
           
   clk_div my_clk_div(.clk(clk_sys),.clr(clr_key),.clk_cnt(clk_cnt_temp));   //例化时钟计数模块，获取当前计数
   display_ctrl my_display_ctrl(.sw_bit(switch_bit),.dpy_num(clk_cnt_temp[29:26]),.dpy_bit(display_bit),.dpy_segment(display_segment)) ; //例化数码管控制模块

endmodule
