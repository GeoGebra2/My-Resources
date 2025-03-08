`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/02/2022 09:08:03 PM
// Design Name: 
// Module Name: display_static_top
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

//4位数码管静态显示模块，通过位选开关控制某位数码管的亮灭，通过段选开关控制数码管显示的数字，4位数码管显示数字相同

module display_static_top(
    input  [3:0] switch_bit,        //4个拨码开关，用于控制数码管位选
    input  [3:0] switch_segment,    //4个拨码开关，用于控制数码管段选输出的数字0~F
    output [3:0] display_bit,       //数码管位选
    output reg [7:0] display_segment   //数码管段选，7 segment
    );
    assign display_bit = switch_bit ; //将拨码开关的状态赋值给数码管的位选 
    always @(*)     
        begin  
            case(switch_segment) //判断拨码开关4位二进制输出代表的十进制（十六进制）数字，verilog可以将二进制('b)与十进制(默认)、十六进制('h)自动转换
                0:display_segment<=7'b11111100; //当拨码开关状态为4'b0000时对应十进制数字0；7段数码管段选为7'b1111110时，显示的字形为“0”
                1:display_segment<=7'b01100001; //1 
                2:display_segment<=7'b11011010; //2
                3:display_segment<=7'b11110011; //3 
                4:display_segment<=7'b01100110; //4 
                5:display_segment<=7'b10110111; //5 
                6:display_segment<=7'b10111110; //6 
                7:display_segment<=7'b11100001; //7 
                8:display_segment<=7'b11111110; //8 
                9:display_segment<=7'b11110111; //9 
                'hA: display_segment<=7'b11101110; //拨码开关状态为4'b1010时对应十六进制数A；8段数码管段选为8'b11101110
                'hB: display_segment<=7'b00111111; //11,b
                'hC: display_segment<=7'b10011100; //12,C 
                'hD: display_segment<=7'b01111011; //13,d
                'hE: display_segment<=7'b10011110; //14,E 
                'hF: display_segment<=7'b10001111; //15,F  
                default: display_segment<=7'b11111100;  // 0
            endcase  
        end 
endmodule
