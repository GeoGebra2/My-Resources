`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/02/2022 07:58:12 PM
// Design Name: 
// Module Name: display_ctrl
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
//数码管控制模块，通过拨码开关控制相应数码管的亮灭，同时显示指定的数字

module display_ctrl(
    input [3:0] sw_bit,
    input [3:0] dpy_num,
    output [3:0] dpy_bit,
    output reg [6:0] dpy_segment
    );
assign dpy_bit = sw_bit ;  //通过拨码开关控制相应数码管的位选，决定数码管亮灭
        always @(*)        
            begin  
                case(dpy_num)              //将要显示的字形和数码管显示对应
                    0:dpy_segment<=7'b1111110;  //字形0
                    1:dpy_segment<=7'b0110000;  //1
                    2:dpy_segment<=7'b1101101;  
                    3:dpy_segment<=7'b1111001;  
                    4:dpy_segment<=7'b0110011;  
                    5:dpy_segment<=7'b1011011;  
                    6:dpy_segment<=7'b1011111;  
                    7:dpy_segment<=7'b1110000;  
                    8:dpy_segment<=7'b1111111;  
                    9:dpy_segment<=7'b1111011;  
                    'hA:dpy_segment<=7'b1110111;  
                    'hB: dpy_segment<=7'b0011111;  
                    'hC: dpy_segment<=7'b1001110;  
                    'hD: dpy_segment<=7'b0111101;  
                    'hE: dpy_segment<=7'b1001111;  
                    'hF: dpy_segment<=7'b1000111;  
                    default: dpy_segment<=7'b1111110;  
                endcase  
            end 
endmodule
