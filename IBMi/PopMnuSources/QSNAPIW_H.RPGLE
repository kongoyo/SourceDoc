**Free
//
// Prototypes for DSM APIs
// -----------------------
// All DSM Windows API declarations added by Jesper Wachs, December 2018.
//
//
// Copyright (c) 2004 Scott C. Klement
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions
// are met:
// 1. Redistributions of source code must retain the above copyright
//    notice, this list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright
//    notice, this list of conditions and the following disclaimer in the
//    documentation and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
// ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPO
// ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTI
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
// OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
// HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRI
// LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WA
// OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
// SUCH DAMAGE.
//
/If Defined(QSNAPIW_H)
/Eof
/EndIf
/Define QSNAPIW_H

// Standard DSM APIs
// -----------------
Dcl-PR QsnClrBuf             Int(10:0) ExtProc('QsnClrBuf');
  BufHandle                 Int(10:0) Const;
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnCrtCmdBuf          Int(10:0) ExtProc('QsnCrtCmdBuf');
  InitSize                  Int(10:0) Const;
  IncrAmt                   Int(10:0) Const Options(*Omit);
  MaxSize                   Int(10:0) Const Options(*Omit);
  Handle                    Int(10:0) Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnCrtInpBuf          Int(10:0) ExtProc('QsnCrtInpBuf');
  BufSize                   Int(10:0) Const;
  IncrAmt                   Int(10:0) Const Options(*Omit);
  MaxSize                   Int(10:0) Const Options(*Omit);
  Handle                    Int(10:0) Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnDltBuf             Int(10:0) ExtProc('QsnDltBuf');
  BufHandle                 Int(10:0) Const;
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnDltEnv             Int(10:0) ExtProc('QsnDltEnv');
  Environment               Int(10:0);
  ErrorCode                Char(32767) Const Options(*Omit:
									*VarSize);
End-PR;

Dcl-PR QsnGetAID            Char(1) ExtProc('QsnGetAID');
  AIDChar                  Char(1) Options(*Omit);
  LowLvlEnvHnd              Int(10:0) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnGetCsrAdr          Int(10:0) ExtProc('QsnGetCsrAdr');
  CsrRow                    Int(10:0) Const Options(*Omit);
  CsrCol                    Int(10:0) Const Options(*Omit);
  LowLvlEnvHnd              Int(10:0) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnPutBuf             Int(10:0) ExtProc('QsnPutBuf');
  CmdBufHnd                 Int(10:0) Const;
  LowLvlEnvHnd              Int(10:0) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnPutGetBuf          Int(10:0) ExtProc('QsnPutGetBuf');
  CmdBufHandle              Int(10:0) Const;
  InpBufHandle              Int(10:0) Const;
  LowEnvHandle              Int(10:0) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnReadInp            Int(10:0) ExtProc('QsnReadInp');
  CC1                      Char(1) Const;
  CC2                      Char(1) Const;
  DataBytes                 Int(10:0) Options(*Omit);
  InpBufHandle              Int(10:0) Options(*Omit) Const;
  CmdBufHandle              Int(10:0) Options(*Omit) Const;
  LowEnvHandle              Int(10:0) Options(*Omit) Const;
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnRtvDta         Pointer ExtProc('QsnRtvDta');
  InpBufHandle              Int(10:0) Const;
  PtrToData             Pointer Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnRtvDtaLen          Int(10:0) ExtProc('QsnRtvDtaLen');
  InpBufHandle              Int(10:0) Const;
  DataLen                   Int(10:0) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnRtvMod             Int(10:0) ExtProc('QsnRtvMod');
  QsnDspMod                Char(1) Options(*Omit);
  QsnLowLvlEnv              Int(10:0) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnSetCsrAdr          Int(10:0) ExtProc('QsnSetCsrAdr');
  FldNbr                    Int(10:0) Const Options(*Omit);
  CsrRow                    Int(10:0) Const Options(*Omit);
  CsrCol                    Int(10:0) Const Options(*Omit);
  CmdBuf                    Int(10:0) Const Options(*Omit);
  LowLvlEnvHnd              Int(10:0) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnSetFld             Int(10:0) ExtProc('QsnSetFld');
  FieldID                   Int(10:0) Const Options(*Omit);
  FieldLen                  Int(10:0) Const Options(*Omit);
  Row                       Int(10:0) Const Options(*Omit);
  Column                    Int(10:0) Const Options(*Omit);
  FFW                      Char(2) Const Options(*Omit);
  FCW                      Char(2) Const
									Dim(32767)
							   Options(*Omit: *VarSize);
  NumOfFCW                  Int(10:0) Const Options(*Omit);
  MonoAttr                 Char(1) Const Options(*Omit);
  ColorAttr                Char(1) Const Options(*Omit);
  CmdBufHandle              Int(10:0) Const Options(*Omit);
  LowEnvHandle              Int(10:0) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnQry5250            Int(10:0) ExtProc('QsnQry5250');
  Qry5250Cap               Char(64) Options(*VarSize);
  Qry5250CapL               Int(10:0) Const;
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnWrtDta             Int(10:0) ExtProc('QsnWrtDta');
  Data                     Char(32767) Const Options(*VarSize);
  DataLen                   Int(10:0) Const;
  FieldID                   Int(10:0) Const Options(*Omit);
  Row                       Int(10:0) Const Options(*Omit);
  Column                    Int(10:0) Const Options(*Omit);
  StrMonoAttr              Char(1) Const Options(*Omit);
  EndMonoAttr              Char(1) Const Options(*Omit);
  StrColorAttr             Char(1) Const Options(*Omit);
  EndColorAttr             Char(1) Const Options(*Omit);
  CmdBufHandle              Int(10:0) Const Options(*Omit);
  LowEnvHandle              Int(10:0) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnWrtSFMaj           Int(10:0) ExtProc('QsnWrtSFMaj');
  MajStruc                 Char(30) Const Options(*VarSize);
  MajStrucLen               Int(10:0) Const;
  SFMajFldID                Int(10:0) Const Options(*Omit);
  SFMajRow                  Int(10:0) Const Options(*Omit);
  SFMajCol                  Int(10:0) Const Options(*Omit);
  SFMajCmdBuf               Int(10:0) Const Options(*Omit);
  SFLowLvlEnv               Int(10:0) Const Options(*Omit);
  SFErrorCode              Char(32767) Const Options(*Omit:
									*VarSize);
End-PR;

Dcl-PR QsnWrtSFMin           Int(10:0) ExtProc('QsnWrtSFMin');
  MinStruc                 Char(80) Const Options(*VarSize);
  MinStrucLen               Int(10:0) Const;
  SFMinCmdBuf               Int(10:0) Const;
  SFMinLowLvl               Int(10:0) Const Options(*Omit);
  SFErrorCode              Char(32767) Const Options(*Omit:
									*VarSize);
End-PR;
//
// Window DSM APIs
// ---------------
Dcl-PR QsnCrtWin             Int(10:0) ExtProc('QsnCrtWin');
  WinDesc                  Char(156) Const Options(*VarSize);
  WinDescL                  Int(10:0) Const;
  UsrExtInf                Char(32767) Const Options(*Omit:
									*VarSize);
  UsrExtInfL                Int(10:0) Const Options(*Omit);
  StartWindow              Char(1) Const Options(*Omit);
  LowLvEnvDes              Char(32767) Const Options(*Omit:
									*VarSize);
  LowLvEnvDesL              Int(10:0) Const Options(*Omit);
  WindowHnd                 Int(10:0) Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnEndWin             Int(10:0) ExtProc('QsnEndWin');
  WinHnd                    Int(10:0) Const;
  RestoreScn               Char(1) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnInzWinD            Int(10:0) ExtProc('QsnInzWinD');
  WinDesc                  Char(77) Const Options(*VarSize);
  WinDescLen                Int(10:0) Const;
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnRtvCurWin          Int(10:0) ExtProc('QsnRtvCurWin');
  CurWinHnd                 Int(10:0) Const;
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnSetCurWin          Int(10:0) ExtProc('QsnSetCurWin');
  WinHnd                    Int(10:0) Const;
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;

Dcl-PR QsnSetEnvWinMod       Int(10:0) ExtProc('QsnSetEnvWinMod');
  EnableWin                Char(1) Const;
  PrvWinModSet             Char(1) Options(*Omit);
  WinModDesc               Char(156) Options(*Omit: *VarSize);
  WinModDescL               Int(10:0) Const Options(*Omit);
  LowLvlEnvHnd              Int(10:0) Const Options(*Omit);
  ErrorCode                Char(32767) Options(*Omit: *VarSize);
End-PR;
//
// Standard DSM API structures
// ---------------------------
// Data structure for QsnQry5250 API.
//
Dcl-DS QsnQ5250;
	QsnQ5Ret Int(10:0);
	QsnQ5Avl Int(10:0);
	QsnQ5Stat Char(1);
	QsnQ5Wkstn BinDec(4:0);
	QsnQ5CLvl Char(3);
	QsnQ5R1 Char(16);
	QsnQ5WType Char(1);
	QsnQ5MType Char(4);
	QsnQ5Model Char(3);
	QsnQ5KbdID Char(1);
	QsnQ5EKbd Char(1);
	QsnQ5PcKbd Char(1);
	QsnQ5SNum Char(4);
	QsnQ5MaxIn BinDec(4:0);
	QsnQ5WSCSp Char(2);
	QsnQ5R2 Char(1);
	QsnQ5WSCB1 Char(1);
	QsnQ5WSCB2 Char(1);
	QsnQ5WSCB3 Char(1);
	QsnQ5WSCB4 Char(1);
	QsnQ5WSCB5 Char(1);
	QsnQ5R3 Char(5);
	QsnQ5Prt Char(1);
	QsnQ5R4 Char(1);
	QsnQ5GrdBf Char(1);
	QsnQ5R5 Char(9);
End-DS;
//
// Window DSM API structures
// -------------------------
// Data structures for QsnSetEnvWinMod API.
//
Dcl-DS QsnEnvWM;
	QsnEWAtrC Char(1);
	QsnEWULR Int(10:0);
	QsnEWULC Int(10:0);
	QsnEWNumR Int(10:0);
	QsnEWNumC Int(10:0);
End-DS;
//
//
//
Dcl-DS MJStruc;
	MJLen Int(5:0);
	MJClass Char(1);
	MJType Char(1);
	MJFlag1 Char(1);
	MJFlag2 Char(1);
	MJFlag3 Char(1);
	MJTPSlt Char(1);
	MJGUIDev Char(1);
	MJNWSwMne Char(1);
	MJNWSwoMne Char(1);
	MJRes1 Char(1);
	MJRes2 Char(1);
	MJTextSize Int(3:0);
	MJRows Int(3:0);
	MJCols Int(3:0);
	MJPad Int(3:0);
	MJNumSep Char(1);
	MJCounSltChr Char(1);
	MJMousCnlAID Char(1);
End-DS;
//
//
//
Dcl-DS MIStruc;
	MILen Int(3:0);
	MIType Char(1);
	MIFlag1 Char(1);
	MIFlag2 Char(1);
	MIFlag3 Char(1);
	MIValue Char(1);
	MIChoText Char(70);
End-DS;
//
// Data structures for QsnCrtWin and QsnChgWin APIs.
//
Dcl-DS QsnWinD;
	QsnWTopR Int(10:0);
	QsnWLeftC Int(10:0);
	QsnWNumR Int(10:0);
	QsnWNumC Int(10:0);
	QsnWMinR Int(10:0);
	QsnWMinC Int(10:0);
	QsnWMaxR Int(10:0);
	QsnWMaxC Int(10:0);
	QsnWFS Char(1);
	QsnWAtrM1 Char(1);
	QsnWAtrM2 Char(1);
	QsnWAtrM3 Char(1);
	QsnWAtrC1 Char(1);
	QsnWAtrC2 Char(1);
	QsnWAtrC3 Char(1);
	QsnWShowB Char(1);
	QsnWShowBA Char(1);
	QsnWShowLA Char(1);
	QsnWShowRA Char(1);
	QsnWMsgL Char(1);
	QsnWULCh Char(1);
	QsnWTopCh Char(1);
	QsnWURCh Char(1);
	QsnWLCh Char(1);
	QsnWRCh Char(1);
	QsnWLLCh Char(1);
	QsnWBotCh Char(1);
	QsnWLRCh Char(1);
	QsnWGUI Char(1);
	QsnWFlg1 Char(1);
	QsnWFlg2 Char(1);
	QsnWR1 Char(1);
	QsnWBdrF Char(1);
	QsnWTtlF Char(1);
	QsnWTAtrM Char(1);
	QsnWTAtrC Char(1);
	QsnWR2 Char(1);
	QsnWR3 Char(3);
	QsnWTtlO Int(10:0);
	QsnWTtlL Int(10:0);
	QsnWR4 Int(10:0);
	QsnWTtl Char(70);
End-DS;
//
// Standard DSM API constants
// --------------------------
// AID keys
//
Dcl-C QSN_F1 x'31';
Dcl-C QSN_F2 x'32';
Dcl-C QSN_F3 x'33';
Dcl-C QSN_F4 x'34';
Dcl-C QSN_F5 x'35';
Dcl-C QSN_F6 x'36';
Dcl-C QSN_F7 x'37';
Dcl-C QSN_F8 x'38';
Dcl-C QSN_F9 x'39';
Dcl-C QSN_F10 x'3A';
Dcl-C QSN_F11 x'3B';
Dcl-C QSN_F12 x'3C';
Dcl-C QSN_F13 x'B1';
Dcl-C QSN_F14 x'B2';
Dcl-C QSN_F15 x'B3';
Dcl-C QSN_F16 x'B4';
Dcl-C QSN_F17 x'B5';
Dcl-C QSN_F18 x'B6';
Dcl-C QSN_F19 x'B7';
Dcl-C QSN_F20 x'B8';
Dcl-C QSN_F21 x'B9';
Dcl-C QSN_F22 x'BA';
Dcl-C QSN_F23 x'BB';
Dcl-C QSN_F24 x'BC';
Dcl-C QSN_SLP x'3F';
Dcl-C QSN_FET x'50';
Dcl-C QSN_PA1 x'6C';
Dcl-C QSN_PA2 x'6E';
Dcl-C QSN_PA3 x'6B';
Dcl-C QSN_CLEAR x'BD';
Dcl-C QSN_ENTER x'F1';
Dcl-C QSN_HELP x'F3';
Dcl-C QSN_ROLLDOWN x'F4';
Dcl-C QSN_ROLLUP x'F5';
Dcl-C QSN_PAGEUP x'F4';
Dcl-C QSN_PAGEDOWN x'F5';
Dcl-C QSN_PRINT x'F6';
Dcl-C QSN_RECBS x'F8';

// Control Characters

Dcl-C QSN_CC1_NULL x'00';
Dcl-C QSN_CC1_LOCKBD x'20';
Dcl-C QSN_CC1_MDTNBY x'40';
Dcl-C QSN_CC1_MDTALL x'60';
Dcl-C QSN_CC1_CLRMOD x'80';
Dcl-C QSN_CC1_MDTNBY_CLRALL x'A0';
Dcl-C QSN_CC1_MDTNBY_CLRMOD x'C0';
Dcl-C QSN_CC1_MDTALL_CLRALL x'E0';

Dcl-C QSN_CC2_NULL x'00';
Dcl-C QSN_CC2_NO_IC x'40';
Dcl-C QSN_CC2_RST_CSR_BL x'20';
Dcl-C QSN_CC2_SET_CSR_BL x'10';
Dcl-C QSN_CC2_UNLOCKBD x'08';
Dcl-C QSN_CC2_ALARM x'04';
Dcl-C QSN_CC2_MSG_OFF x'02';
Dcl-C QSN_CC2_MSG_ON x'01';
//
// Field Format Words
//
Dcl-C QSN_NO_FFW x'0000';
Dcl-C QSN_FFW_BYPASS x'6000';
Dcl-C QSN_FFW_DUP x'5000';
Dcl-C QSN_FFW_MDT x'4800';
Dcl-C QSN_FFW_ALPHA_SHIFT x'4000';
Dcl-C QSN_FFW_ALPHA_ONLY x'4100';
Dcl-C QSN_FFW_NUM_SHIFT x'4200';
Dcl-C QSN_FFW_NUM_ONLY x'4300';
Dcl-C QSN_FFW_KATA x'4400';
Dcl-C QSN_FFW_DIGIT_ONLY x'4500';
Dcl-C QSN_FFW_IO x'4600';
Dcl-C QSN_FFW_SIGNED_NUMERIC x'4700';
Dcl-C QSN_FFW_AUTO_ENTER x'4080';
Dcl-C QSN_FFW_FER x'4040';
Dcl-C QSN_FFW_AUTO_FER x'4040';
Dcl-C QSN_FFW_MONOCASE x'4020';
Dcl-C QSN_FFW_AUTO_MONOCASE x'4020';
Dcl-C QSN_FFW_ME x'4008';
Dcl-C QSN_FFW_NOADJUST x'4000';
Dcl-C QSN_FFW_RA_ZERO x'4005';
Dcl-C QSN_FFW_RA_BLANK x'4006';
Dcl-C QSN_FFW_MF x'4007';

Dcl-C QSN_FCW_RESEQ x'8000';
Dcl-C QSN_FCW_MSR x'8101';
Dcl-C QSN_FCW_SLP x'8102';
Dcl-C QSN_FCW_MSR_SLP x'8103';
Dcl-C QSN_FCW_SLP_SA x'8106';
Dcl-C QSN_FCW_DBCS_ONLY x'8200';
Dcl-C QSN_FCW_DBCS_PURE x'8220';
Dcl-C QSN_FCW_DBCS_EITHER x'8240';
Dcl-C QSN_FCW_DBCS_OPEN x'8280';
Dcl-C QSN_FCW_DBCS_OPEN_CO x'82C0';
Dcl-C QSN_FCW_TRANSPARENT x'8400';
Dcl-C QSN_FCW_FET x'8501';
Dcl-C QSN_FCW_CONT_FIRST x'8601';
Dcl-C QSN_FCW_CONT_LAST x'8602';
Dcl-C QSN_FCW_CONT_MIDDLE x'8603';
Dcl-C QSN_FCW_CP x'8800';
Dcl-C QSN_FCW_HL x'8900';
Dcl-C QSN_FCW_PDS x'8A00';
Dcl-C QSN_FCW_MOD11 x'B140';
Dcl-C QSN_FCW_MOD10 x'B1A0';

Dcl-C QSN_READ_INP x'42';
Dcl-C QSN_READ_MDT x'52';
Dcl-C QSN_READ_IMM x'72';
Dcl-C QSN_READ_MDT_ALT x'82';
//
// Screen Attributes
//
Dcl-C QSN_NO_SA x'00';
Dcl-C QSN_SA_NORM x'20';
Dcl-C QSN_SA_CS x'30';
Dcl-C QSN_SA_BL x'28';
Dcl-C QSN_SA_UL x'24';
Dcl-C QSN_SA_HI x'22';
Dcl-C QSN_SA_RI x'21';
Dcl-C QSN_SA_ND x'27';

Dcl-C QSN_SA_GRN x'20';
Dcl-C QSN_SA_GRN_RI x'21';
Dcl-C QSN_SA_WHT x'22';
Dcl-C QSN_SA_WHT_RI x'23';
Dcl-C QSN_SA_GRN_UL x'24';
Dcl-C QSN_SA_GRN_UL_RI x'25';
Dcl-C QSN_SA_WHT_UL x'26';
Dcl-C QSN_SA_RED x'28';
Dcl-C QSN_SA_RED_RI x'29';
Dcl-C QSN_SA_RED_BL x'2A';
Dcl-C QSN_SA_RED_RI_BL x'2B';
Dcl-C QSN_SA_RED_UL x'2C';
Dcl-C QSN_SA_RED_UL_RI x'2D';
Dcl-C QSN_SA_RED_UL_BL x'2E';
Dcl-C QSN_SA_ND_2F x'2F';
Dcl-C QSN_SA_TRQ_CS x'30';
Dcl-C QSN_SA_TRQ_CS_RI x'31';
Dcl-C QSN_SA_YLW_CS x'32';
Dcl-C QSN_SA_YLW_CS_RI x'33';
Dcl-C QSN_SA_TRQ_UL x'34';
Dcl-C QSN_SA_TRQ_UL_RI x'35';
Dcl-C QSN_SA_YLW_UL x'36';
Dcl-C QSN_SA_ND_37 x'37';
Dcl-C QSN_SA_PNK x'38';
Dcl-C QSN_SA_PNK_RI x'39';
Dcl-C QSN_SA_BLU x'3A';
Dcl-C QSN_SA_BLU_RI x'3B';
Dcl-C QSN_SA_PNK_UL x'3C';
Dcl-C QSN_SA_PNK_UL_RI x'3D';
Dcl-C QSN_SA_BLU_UL x'3E';
Dcl-C QSN_SA_ND_3F x'3F';
