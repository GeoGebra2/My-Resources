`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/02/2022 11:47:15 PM
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
//4位数码管动态显示4个不同数字，给4位数码管分配不同频率的时钟分频，实现正向计数效果，高频循环点亮数码管并利用人眼视觉暂留效果，达到4位数码管同时点亮的效果
//本模块为顶层模块，通过调用时钟分频计数模块、数码管控制模块、数码管扫描模块完成相关任务

module display_dynamic_top(
    input clk_sys,
    input clr_key,
    output [3:0] display_bit,
    output [6:0] display_segment
    );
    
    wire [38:0] clk_cnt_temp ;    //中间变量，存储时钟源计数结果
    wire [3:0] display_num_temp ; //中间变量，存储数码管显示数字
    
clk_div myclk_div(.clk(clk_sys),.clr(clr_key),.clk_cnt(clk_cnt_temp));   //时钟模块例化
display_scan mydisplay_scan(.clk_cnt(clk_cnt_temp),.dpy_bit(display_bit),.dpy_num(display_num_temp));//数码管扫描模块例化
display_ctrl mydisplay_ctrl(.dpy_num(display_num_temp),.dpy_segment(display_segment)) ; //数码管控制模块例化


endmodule
