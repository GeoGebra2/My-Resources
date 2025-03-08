`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10/02/2022 11:53:17 PM
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


module display_ctrl(
    input [3:0] dpy_num,
    output reg [6:0] dpy_segment
    );

    always @(*)        
        begin  
            case(dpy_num)              
                0:dpy_segment<=7'b1111110;  //×ÖÐÎ0
                1:dpy_segment<=7'b0110000;  //×ÖÐÎ1
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
                default: dpy_segment<=7'b1111110;  //×ÖÐÎ0
            endcase  
        end      
endmodule
