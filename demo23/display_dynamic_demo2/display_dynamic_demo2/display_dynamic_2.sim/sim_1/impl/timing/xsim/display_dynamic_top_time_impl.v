// Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2017.3 (win64) Build 2018833 Wed Oct  4 19:58:22 MDT 2017
// Date        : Mon Oct  3 22:48:25 2022
// Host        : DESKTOP-D12KSI8 running 64-bit major release  (build 9200)
// Command     : write_verilog -mode timesim -nolib -sdf_anno true -force -file {F:/Lab
//               center/VivadoProject/shumaguan2022/display_dynamic_2/display_dynamic_2.sim/sim_1/impl/timing/xsim/display_dynamic_top_time_impl.v}
// Design      : display_dynamic_top
// Purpose     : This verilog netlist is a timing simulation representation of the design and should not be modified or
//               synthesized. Please ensure that this netlist is used with the corresponding SDF file.
// Device      : xc7a50tcsg324-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps
`define XIL_TIMING

module clk_div
   (sel0,
    clr_key,
    clk_sys);
  output [3:0]sel0;
  input clr_key;
  input clk_sys;

  wire \clk_cnt[0]_i_2_n_0 ;
  wire \clk_cnt_reg[0]_i_1_n_0 ;
  wire \clk_cnt_reg[0]_i_1_n_4 ;
  wire \clk_cnt_reg[0]_i_1_n_5 ;
  wire \clk_cnt_reg[0]_i_1_n_6 ;
  wire \clk_cnt_reg[0]_i_1_n_7 ;
  wire \clk_cnt_reg[12]_i_1_n_0 ;
  wire \clk_cnt_reg[12]_i_1_n_4 ;
  wire \clk_cnt_reg[12]_i_1_n_5 ;
  wire \clk_cnt_reg[12]_i_1_n_6 ;
  wire \clk_cnt_reg[12]_i_1_n_7 ;
  wire \clk_cnt_reg[16]_i_1_n_0 ;
  wire \clk_cnt_reg[16]_i_1_n_4 ;
  wire \clk_cnt_reg[16]_i_1_n_5 ;
  wire \clk_cnt_reg[16]_i_1_n_6 ;
  wire \clk_cnt_reg[16]_i_1_n_7 ;
  wire \clk_cnt_reg[20]_i_1_n_0 ;
  wire \clk_cnt_reg[20]_i_1_n_4 ;
  wire \clk_cnt_reg[20]_i_1_n_5 ;
  wire \clk_cnt_reg[20]_i_1_n_6 ;
  wire \clk_cnt_reg[20]_i_1_n_7 ;
  wire \clk_cnt_reg[24]_i_1_n_0 ;
  wire \clk_cnt_reg[24]_i_1_n_4 ;
  wire \clk_cnt_reg[24]_i_1_n_5 ;
  wire \clk_cnt_reg[24]_i_1_n_6 ;
  wire \clk_cnt_reg[24]_i_1_n_7 ;
  wire \clk_cnt_reg[28]_i_1_n_6 ;
  wire \clk_cnt_reg[28]_i_1_n_7 ;
  wire \clk_cnt_reg[4]_i_1_n_0 ;
  wire \clk_cnt_reg[4]_i_1_n_4 ;
  wire \clk_cnt_reg[4]_i_1_n_5 ;
  wire \clk_cnt_reg[4]_i_1_n_6 ;
  wire \clk_cnt_reg[4]_i_1_n_7 ;
  wire \clk_cnt_reg[8]_i_1_n_0 ;
  wire \clk_cnt_reg[8]_i_1_n_4 ;
  wire \clk_cnt_reg[8]_i_1_n_5 ;
  wire \clk_cnt_reg[8]_i_1_n_6 ;
  wire \clk_cnt_reg[8]_i_1_n_7 ;
  wire \clk_cnt_reg_n_0_[0] ;
  wire \clk_cnt_reg_n_0_[10] ;
  wire \clk_cnt_reg_n_0_[11] ;
  wire \clk_cnt_reg_n_0_[12] ;
  wire \clk_cnt_reg_n_0_[13] ;
  wire \clk_cnt_reg_n_0_[14] ;
  wire \clk_cnt_reg_n_0_[15] ;
  wire \clk_cnt_reg_n_0_[16] ;
  wire \clk_cnt_reg_n_0_[17] ;
  wire \clk_cnt_reg_n_0_[18] ;
  wire \clk_cnt_reg_n_0_[19] ;
  wire \clk_cnt_reg_n_0_[1] ;
  wire \clk_cnt_reg_n_0_[20] ;
  wire \clk_cnt_reg_n_0_[21] ;
  wire \clk_cnt_reg_n_0_[22] ;
  wire \clk_cnt_reg_n_0_[23] ;
  wire \clk_cnt_reg_n_0_[24] ;
  wire \clk_cnt_reg_n_0_[25] ;
  wire \clk_cnt_reg_n_0_[2] ;
  wire \clk_cnt_reg_n_0_[3] ;
  wire \clk_cnt_reg_n_0_[4] ;
  wire \clk_cnt_reg_n_0_[5] ;
  wire \clk_cnt_reg_n_0_[6] ;
  wire \clk_cnt_reg_n_0_[7] ;
  wire \clk_cnt_reg_n_0_[8] ;
  wire \clk_cnt_reg_n_0_[9] ;
  wire clk_sys;
  wire clr_key;
  wire [3:0]sel0;
  wire [2:0]\NLW_clk_cnt_reg[0]_i_1_CO_UNCONNECTED ;
  wire [2:0]\NLW_clk_cnt_reg[12]_i_1_CO_UNCONNECTED ;
  wire [2:0]\NLW_clk_cnt_reg[16]_i_1_CO_UNCONNECTED ;
  wire [2:0]\NLW_clk_cnt_reg[20]_i_1_CO_UNCONNECTED ;
  wire [2:0]\NLW_clk_cnt_reg[24]_i_1_CO_UNCONNECTED ;
  wire [3:0]\NLW_clk_cnt_reg[28]_i_1_CO_UNCONNECTED ;
  wire [3:2]\NLW_clk_cnt_reg[28]_i_1_O_UNCONNECTED ;
  wire [2:0]\NLW_clk_cnt_reg[4]_i_1_CO_UNCONNECTED ;
  wire [2:0]\NLW_clk_cnt_reg[8]_i_1_CO_UNCONNECTED ;

  LUT1 #(
    .INIT(2'h1)) 
    \clk_cnt[0]_i_2 
       (.I0(\clk_cnt_reg_n_0_[0] ),
        .O(\clk_cnt[0]_i_2_n_0 ));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[0] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[0]_i_1_n_7 ),
        .Q(\clk_cnt_reg_n_0_[0] ),
        .R(clr_key));
  CARRY4 \clk_cnt_reg[0]_i_1 
       (.CI(1'b0),
        .CO({\clk_cnt_reg[0]_i_1_n_0 ,\NLW_clk_cnt_reg[0]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b1}),
        .O({\clk_cnt_reg[0]_i_1_n_4 ,\clk_cnt_reg[0]_i_1_n_5 ,\clk_cnt_reg[0]_i_1_n_6 ,\clk_cnt_reg[0]_i_1_n_7 }),
        .S({\clk_cnt_reg_n_0_[3] ,\clk_cnt_reg_n_0_[2] ,\clk_cnt_reg_n_0_[1] ,\clk_cnt[0]_i_2_n_0 }));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[10] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[8]_i_1_n_5 ),
        .Q(\clk_cnt_reg_n_0_[10] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[11] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[8]_i_1_n_4 ),
        .Q(\clk_cnt_reg_n_0_[11] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[12] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[12]_i_1_n_7 ),
        .Q(\clk_cnt_reg_n_0_[12] ),
        .R(clr_key));
  CARRY4 \clk_cnt_reg[12]_i_1 
       (.CI(\clk_cnt_reg[8]_i_1_n_0 ),
        .CO({\clk_cnt_reg[12]_i_1_n_0 ,\NLW_clk_cnt_reg[12]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\clk_cnt_reg[12]_i_1_n_4 ,\clk_cnt_reg[12]_i_1_n_5 ,\clk_cnt_reg[12]_i_1_n_6 ,\clk_cnt_reg[12]_i_1_n_7 }),
        .S({\clk_cnt_reg_n_0_[15] ,\clk_cnt_reg_n_0_[14] ,\clk_cnt_reg_n_0_[13] ,\clk_cnt_reg_n_0_[12] }));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[13] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[12]_i_1_n_6 ),
        .Q(\clk_cnt_reg_n_0_[13] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[14] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[12]_i_1_n_5 ),
        .Q(\clk_cnt_reg_n_0_[14] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[15] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[12]_i_1_n_4 ),
        .Q(\clk_cnt_reg_n_0_[15] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[16] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[16]_i_1_n_7 ),
        .Q(\clk_cnt_reg_n_0_[16] ),
        .R(clr_key));
  CARRY4 \clk_cnt_reg[16]_i_1 
       (.CI(\clk_cnt_reg[12]_i_1_n_0 ),
        .CO({\clk_cnt_reg[16]_i_1_n_0 ,\NLW_clk_cnt_reg[16]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\clk_cnt_reg[16]_i_1_n_4 ,\clk_cnt_reg[16]_i_1_n_5 ,\clk_cnt_reg[16]_i_1_n_6 ,\clk_cnt_reg[16]_i_1_n_7 }),
        .S({\clk_cnt_reg_n_0_[19] ,\clk_cnt_reg_n_0_[18] ,\clk_cnt_reg_n_0_[17] ,\clk_cnt_reg_n_0_[16] }));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[17] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[16]_i_1_n_6 ),
        .Q(\clk_cnt_reg_n_0_[17] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[18] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[16]_i_1_n_5 ),
        .Q(\clk_cnt_reg_n_0_[18] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[19] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[16]_i_1_n_4 ),
        .Q(\clk_cnt_reg_n_0_[19] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[1] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[0]_i_1_n_6 ),
        .Q(\clk_cnt_reg_n_0_[1] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[20] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[20]_i_1_n_7 ),
        .Q(\clk_cnt_reg_n_0_[20] ),
        .R(clr_key));
  CARRY4 \clk_cnt_reg[20]_i_1 
       (.CI(\clk_cnt_reg[16]_i_1_n_0 ),
        .CO({\clk_cnt_reg[20]_i_1_n_0 ,\NLW_clk_cnt_reg[20]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\clk_cnt_reg[20]_i_1_n_4 ,\clk_cnt_reg[20]_i_1_n_5 ,\clk_cnt_reg[20]_i_1_n_6 ,\clk_cnt_reg[20]_i_1_n_7 }),
        .S({\clk_cnt_reg_n_0_[23] ,\clk_cnt_reg_n_0_[22] ,\clk_cnt_reg_n_0_[21] ,\clk_cnt_reg_n_0_[20] }));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[21] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[20]_i_1_n_6 ),
        .Q(\clk_cnt_reg_n_0_[21] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[22] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[20]_i_1_n_5 ),
        .Q(\clk_cnt_reg_n_0_[22] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[23] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[20]_i_1_n_4 ),
        .Q(\clk_cnt_reg_n_0_[23] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[24] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[24]_i_1_n_7 ),
        .Q(\clk_cnt_reg_n_0_[24] ),
        .R(clr_key));
  CARRY4 \clk_cnt_reg[24]_i_1 
       (.CI(\clk_cnt_reg[20]_i_1_n_0 ),
        .CO({\clk_cnt_reg[24]_i_1_n_0 ,\NLW_clk_cnt_reg[24]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\clk_cnt_reg[24]_i_1_n_4 ,\clk_cnt_reg[24]_i_1_n_5 ,\clk_cnt_reg[24]_i_1_n_6 ,\clk_cnt_reg[24]_i_1_n_7 }),
        .S({sel0[1:0],\clk_cnt_reg_n_0_[25] ,\clk_cnt_reg_n_0_[24] }));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[25] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[24]_i_1_n_6 ),
        .Q(\clk_cnt_reg_n_0_[25] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[26] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[24]_i_1_n_5 ),
        .Q(sel0[0]),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[27] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[24]_i_1_n_4 ),
        .Q(sel0[1]),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[28] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[28]_i_1_n_7 ),
        .Q(sel0[2]),
        .R(clr_key));
  CARRY4 \clk_cnt_reg[28]_i_1 
       (.CI(\clk_cnt_reg[24]_i_1_n_0 ),
        .CO(\NLW_clk_cnt_reg[28]_i_1_CO_UNCONNECTED [3:0]),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\NLW_clk_cnt_reg[28]_i_1_O_UNCONNECTED [3:2],\clk_cnt_reg[28]_i_1_n_6 ,\clk_cnt_reg[28]_i_1_n_7 }),
        .S({1'b0,1'b0,sel0[3:2]}));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[29] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[28]_i_1_n_6 ),
        .Q(sel0[3]),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[2] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[0]_i_1_n_5 ),
        .Q(\clk_cnt_reg_n_0_[2] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[3] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[0]_i_1_n_4 ),
        .Q(\clk_cnt_reg_n_0_[3] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[4] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[4]_i_1_n_7 ),
        .Q(\clk_cnt_reg_n_0_[4] ),
        .R(clr_key));
  CARRY4 \clk_cnt_reg[4]_i_1 
       (.CI(\clk_cnt_reg[0]_i_1_n_0 ),
        .CO({\clk_cnt_reg[4]_i_1_n_0 ,\NLW_clk_cnt_reg[4]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\clk_cnt_reg[4]_i_1_n_4 ,\clk_cnt_reg[4]_i_1_n_5 ,\clk_cnt_reg[4]_i_1_n_6 ,\clk_cnt_reg[4]_i_1_n_7 }),
        .S({\clk_cnt_reg_n_0_[7] ,\clk_cnt_reg_n_0_[6] ,\clk_cnt_reg_n_0_[5] ,\clk_cnt_reg_n_0_[4] }));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[5] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[4]_i_1_n_6 ),
        .Q(\clk_cnt_reg_n_0_[5] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[6] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[4]_i_1_n_5 ),
        .Q(\clk_cnt_reg_n_0_[6] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[7] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[4]_i_1_n_4 ),
        .Q(\clk_cnt_reg_n_0_[7] ),
        .R(clr_key));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[8] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[8]_i_1_n_7 ),
        .Q(\clk_cnt_reg_n_0_[8] ),
        .R(clr_key));
  CARRY4 \clk_cnt_reg[8]_i_1 
       (.CI(\clk_cnt_reg[4]_i_1_n_0 ),
        .CO({\clk_cnt_reg[8]_i_1_n_0 ,\NLW_clk_cnt_reg[8]_i_1_CO_UNCONNECTED [2:0]}),
        .CYINIT(1'b0),
        .DI({1'b0,1'b0,1'b0,1'b0}),
        .O({\clk_cnt_reg[8]_i_1_n_4 ,\clk_cnt_reg[8]_i_1_n_5 ,\clk_cnt_reg[8]_i_1_n_6 ,\clk_cnt_reg[8]_i_1_n_7 }),
        .S({\clk_cnt_reg_n_0_[11] ,\clk_cnt_reg_n_0_[10] ,\clk_cnt_reg_n_0_[9] ,\clk_cnt_reg_n_0_[8] }));
  FDRE #(
    .INIT(1'b0)) 
    \clk_cnt_reg[9] 
       (.C(clk_sys),
        .CE(1'b1),
        .D(\clk_cnt_reg[8]_i_1_n_6 ),
        .Q(\clk_cnt_reg_n_0_[9] ),
        .R(clr_key));
endmodule

module display_ctrl
   (display_segment_OBUF,
    sel0);
  output [6:0]display_segment_OBUF;
  input [3:0]sel0;

  wire [6:0]display_segment_OBUF;
  wire [3:0]sel0;

  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT4 #(
    .INIT(16'hBFDA)) 
    \display_segment_OBUF[0]_inst_i_1 
       (.I0(sel0[3]),
        .I1(sel0[0]),
        .I2(sel0[2]),
        .I3(sel0[1]),
        .O(display_segment_OBUF[0]));
  (* SOFT_HLUTNM = "soft_lutpair0" *) 
  LUT4 #(
    .INIT(16'hAE6F)) 
    \display_segment_OBUF[1]_inst_i_1 
       (.I0(sel0[3]),
        .I1(sel0[2]),
        .I2(sel0[0]),
        .I3(sel0[1]),
        .O(display_segment_OBUF[1]));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT4 #(
    .INIT(16'hA8EF)) 
    \display_segment_OBUF[2]_inst_i_1 
       (.I0(sel0[3]),
        .I1(sel0[1]),
        .I2(sel0[2]),
        .I3(sel0[0]),
        .O(display_segment_OBUF[2]));
  (* SOFT_HLUTNM = "soft_lutpair1" *) 
  LUT4 #(
    .INIT(16'h3EDB)) 
    \display_segment_OBUF[3]_inst_i_1 
       (.I0(sel0[3]),
        .I1(sel0[2]),
        .I2(sel0[1]),
        .I3(sel0[0]),
        .O(display_segment_OBUF[3]));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT4 #(
    .INIT(16'h7F67)) 
    \display_segment_OBUF[4]_inst_i_1 
       (.I0(sel0[3]),
        .I1(sel0[2]),
        .I2(sel0[1]),
        .I3(sel0[0]),
        .O(display_segment_OBUF[4]));
  (* SOFT_HLUTNM = "soft_lutpair2" *) 
  LUT4 #(
    .INIT(16'h497F)) 
    \display_segment_OBUF[5]_inst_i_1 
       (.I0(sel0[3]),
        .I1(sel0[0]),
        .I2(sel0[1]),
        .I3(sel0[2]),
        .O(display_segment_OBUF[5]));
  LUT4 #(
    .INIT(16'hD6FB)) 
    \display_segment_OBUF[6]_inst_i_1 
       (.I0(sel0[3]),
        .I1(sel0[2]),
        .I2(sel0[1]),
        .I3(sel0[0]),
        .O(display_segment_OBUF[6]));
endmodule

(* ECO_CHECKSUM = "f8073c0e" *) 
(* NotValidForBitStream *)
module display_dynamic_top
   (clk_sys,
    clr_key,
    switch_bit,
    display_bit,
    display_segment);
  input clk_sys;
  input clr_key;
  input [3:0]switch_bit;
  output [3:0]display_bit;
  output [6:0]display_segment;

  wire clk_sys;
  wire clk_sys_IBUF;
  wire clk_sys_IBUF_BUFG;
  wire clr_key;
  wire clr_key_IBUF;
  wire [3:0]display_bit;
  wire [3:0]display_bit_OBUF;
  wire [6:0]display_segment;
  wire [6:0]display_segment_OBUF;
  wire [3:0]sel0;
  wire [3:0]switch_bit;

initial begin
 $sdf_annotate("display_dynamic_top_time_impl.sdf",,,,"tool_control");
end
  BUFG clk_sys_IBUF_BUFG_inst
       (.I(clk_sys_IBUF),
        .O(clk_sys_IBUF_BUFG));
  IBUF clk_sys_IBUF_inst
       (.I(clk_sys),
        .O(clk_sys_IBUF));
  IBUF clr_key_IBUF_inst
       (.I(clr_key),
        .O(clr_key_IBUF));
  OBUF \display_bit_OBUF[0]_inst 
       (.I(display_bit_OBUF[0]),
        .O(display_bit[0]));
  OBUF \display_bit_OBUF[1]_inst 
       (.I(display_bit_OBUF[1]),
        .O(display_bit[1]));
  OBUF \display_bit_OBUF[2]_inst 
       (.I(display_bit_OBUF[2]),
        .O(display_bit[2]));
  OBUF \display_bit_OBUF[3]_inst 
       (.I(display_bit_OBUF[3]),
        .O(display_bit[3]));
  OBUF \display_segment_OBUF[0]_inst 
       (.I(display_segment_OBUF[0]),
        .O(display_segment[0]));
  OBUF \display_segment_OBUF[1]_inst 
       (.I(display_segment_OBUF[1]),
        .O(display_segment[1]));
  OBUF \display_segment_OBUF[2]_inst 
       (.I(display_segment_OBUF[2]),
        .O(display_segment[2]));
  OBUF \display_segment_OBUF[3]_inst 
       (.I(display_segment_OBUF[3]),
        .O(display_segment[3]));
  OBUF \display_segment_OBUF[4]_inst 
       (.I(display_segment_OBUF[4]),
        .O(display_segment[4]));
  OBUF \display_segment_OBUF[5]_inst 
       (.I(display_segment_OBUF[5]),
        .O(display_segment[5]));
  OBUF \display_segment_OBUF[6]_inst 
       (.I(display_segment_OBUF[6]),
        .O(display_segment[6]));
  display_ctrl my_display_ctrl
       (.display_segment_OBUF(display_segment_OBUF),
        .sel0(sel0));
  clk_div myclk_div
       (.clk_sys(clk_sys_IBUF_BUFG),
        .clr_key(clr_key_IBUF),
        .sel0(sel0));
  IBUF \switch_bit_IBUF[0]_inst 
       (.I(switch_bit[0]),
        .O(display_bit_OBUF[0]));
  IBUF \switch_bit_IBUF[1]_inst 
       (.I(switch_bit[1]),
        .O(display_bit_OBUF[1]));
  IBUF \switch_bit_IBUF[2]_inst 
       (.I(switch_bit[2]),
        .O(display_bit_OBUF[2]));
  IBUF \switch_bit_IBUF[3]_inst 
       (.I(switch_bit[3]),
        .O(display_bit_OBUF[3]));
endmodule
`ifndef GLBL
`define GLBL
`timescale  1 ps / 1 ps

module glbl ();

    parameter ROC_WIDTH = 100000;
    parameter TOC_WIDTH = 0;

//--------   STARTUP Globals --------------
    wire GSR;
    wire GTS;
    wire GWE;
    wire PRLD;
    tri1 p_up_tmp;
    tri (weak1, strong0) PLL_LOCKG = p_up_tmp;

    wire PROGB_GLBL;
    wire CCLKO_GLBL;
    wire FCSBO_GLBL;
    wire [3:0] DO_GLBL;
    wire [3:0] DI_GLBL;
   
    reg GSR_int;
    reg GTS_int;
    reg PRLD_int;

//--------   JTAG Globals --------------
    wire JTAG_TDO_GLBL;
    wire JTAG_TCK_GLBL;
    wire JTAG_TDI_GLBL;
    wire JTAG_TMS_GLBL;
    wire JTAG_TRST_GLBL;

    reg JTAG_CAPTURE_GLBL;
    reg JTAG_RESET_GLBL;
    reg JTAG_SHIFT_GLBL;
    reg JTAG_UPDATE_GLBL;
    reg JTAG_RUNTEST_GLBL;

    reg JTAG_SEL1_GLBL = 0;
    reg JTAG_SEL2_GLBL = 0 ;
    reg JTAG_SEL3_GLBL = 0;
    reg JTAG_SEL4_GLBL = 0;

    reg JTAG_USER_TDO1_GLBL = 1'bz;
    reg JTAG_USER_TDO2_GLBL = 1'bz;
    reg JTAG_USER_TDO3_GLBL = 1'bz;
    reg JTAG_USER_TDO4_GLBL = 1'bz;

    assign (strong1, weak0) GSR = GSR_int;
    assign (strong1, weak0) GTS = GTS_int;
    assign (weak1, weak0) PRLD = PRLD_int;

    initial begin
	GSR_int = 1'b1;
	PRLD_int = 1'b1;
	#(ROC_WIDTH)
	GSR_int = 1'b0;
	PRLD_int = 1'b0;
    end

    initial begin
	GTS_int = 1'b1;
	#(TOC_WIDTH)
	GTS_int = 1'b0;
    end

endmodule
`endif
