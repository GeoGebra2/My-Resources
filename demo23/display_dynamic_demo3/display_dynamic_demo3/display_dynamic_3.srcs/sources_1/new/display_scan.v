`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/03/2022 12:38:04 AM
// Design Name: 
// Module Name: display_scan
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
//数码管扫描模块，从时钟分频计数器中选择连续的16位，分别赋给4位数码管，实现正向计数效果

module display_scan(
    input [38:0] clk_cnt,
    output reg [3:0] dpy_bit,
    output reg [3:0] dpy_num
    );
    
    always@(*) 
        case(clk_cnt[17:16]) //选择时钟计数器中的两位，循环点亮4位数码管，通常人眼可识别的单色刷新频率为60 Hz，因此全部数码管扫描一遍的时间应至少小于10ms（100 Hz）。
            0:  begin dpy_num <= clk_cnt[26:23];  dpy_bit <= 4'b0001; end //数码管1有效，且显示数值为最低4位，数字变化速度最快，人眼余辉效应:20-50ms 
            1:  begin dpy_num <= clk_cnt[30:27];  dpy_bit <= 4'b0010; end //数码管2有效，且显示数值为次低4位  
            2:  begin dpy_num <= clk_cnt[34:31];  dpy_bit <= 4'b0100; end //数码管3有效，且显示数值为次高4位  
            3:  begin dpy_num <= clk_cnt[38:35];  dpy_bit <= 4'b1000; end //数码管4有效，且显示数值为最高4位  
        endcase   

endmodule
