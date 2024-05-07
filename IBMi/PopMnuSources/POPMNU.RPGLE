**Free
Ctl-Opt NoMain BndDir('QC2LE');
//
// PopMnu
// ------
// Function to display a popup menu where the user can select an
// option. The option number is then returned to caller.
//
// Jesper Wachs, Version 1, December 2018.
//
// The source member are delivered 'as is'.
//
// Neither Jesper Wachs nor anyone else who has been involved in
// the creation, production or delivery of this product shall be
// liable for any direct, indirect, consequential or incidental
// damages (including damages for loss of business profits,
// business interruption, loss of business information, and the
// like) arising out of the use or inability to use such product
// even if Jesper Wachs has been advised of the possibility of
// such damages.
//
// Copymember for exported functions.
// ----------------------------------
/copy qrpglesrc,popmnu_pr
//
// Copymember(s) for imported functions.
// -------------------------------------
/copy qrpglesrc,qsnapiw_h
//
// Prototypes for local functions.
// -------------------------------
Dcl-PR CalcMenuSize Packed(3:0);
  iStyle Packed(3:0) Const;
  iGUISupport Ind Const;
  iTitle Char(74) Const;
  iHeader Char(74) Const;
  iFooter Char(74) Const;
  iFKeysText Char(74) Const;
  iOptions Char(74) Const Dim(15);
  oMaxLen Packed(3:0);
  oNbrElm Packed(3:0);
  oMaxElmLen Packed(3:0);
  oNbrLin Packed(3:0);
End-PR;

Dcl-PR CreatePopupWindow Int(10:0);
  iRow Packed(3:0) Const;
  iCol Packed(3:0) Const;
  iNbrRow Packed(3:0) Const;
  iNbrCol Packed(3:0) Const;
  iNbrElm Packed(3:0) Const;
  iBorder Packed(3:0) Const;
  iStyle Packed(3:0) Const;
  iTitle VarChar(70) Value;
  iHeader VarChar(70) Value;
  iFooter VarChar(70) Value;
  iFKeyText VarChar(70) Value;
  ohCmdBuf Int(10:0);
  ohInpBuf Int(10:0);
  ohWin Int(10:0);
End-PR;

Dcl-PR GetScreenSize;
  oRows Packed(3:0);
  oCols Packed(3:0);
End-PR;

Dcl-PR OptionsAsClassic Int(10:0);
  ihCmdBuf Int(10:0) Const;
  ihInpBuf Int(10:0) Const;
  ihWin Int(10:0) Const;
  iNbrElm Packed(3:0) Const;
  iOptions Char(70) Const Dim(15);
  iHdrLen Packed(3:0) Const;
  iFtrLen Packed(3:0) Const;
  oSltOpt Packed(3:0);
End-PR;

Dcl-PR OptionsAsCursor Int(10:0);
  ihCmdBuf Int(10:0) Const;
  ihInpBuf Int(10:0) Const;
  ihWin Int(10:0) Const;
  iNbrElm Packed(3:0) Const;
  iOptions Char(70) Const Dim(15);
  iHdrLen Packed(3:0) Const;
  iFtrLen Packed(3:0) Const;
  oSltOpt Packed(3:0);
End-PR;

Dcl-PR OptionsAsPushBtnChar Int(10:0);
  ihCmdBuf Int(10:0) Const;
  ihInpBuf Int(10:0) Const;
  ihWin Int(10:0) Const;
  iNbrElm Packed(3:0) Const;
  iOptions Char(70) Const Dim(15);
  iHdrLen Packed(3:0) Const;
  iMaxLen Packed(3:0) Const;
  iMaxElmLen Packed(3:0) Const;
  iRow Packed(3:0) Const;
  oSltOpt Packed(3:0);
End-PR;

Dcl-PR OptionsAsPushBtnGUI Int(10:0);
  ihCmdBuf Int(10:0) Const;
  ihInpBuf Int(10:0) Const;
  ihWin Int(10:0) Const;
  iNbrElm Packed(3:0) Const;
  iOptions Char(70) Const Dim(15);
  iHdrLen Packed(3:0) Const;
  iMaxLen Packed(3:0) Const;
  iMaxElmLen Packed(3:0) Const;
  iRow Packed(3:0) Const;
  oSltOpt Packed(3:0);
 End-PR;

Dcl-PR ValidateParms Packed(3:0);
  iLocation Packed(3:0) Const;
  iRow Packed(3:0) Const;
  iCol Packed(3:0) Const;
  iBorder Packed(3:0) Const;
  iStyle Packed(3:0) Const;
  iOptions Char(70) Const Dim(15);
End-PR;
//
// Exported funtions.
// ------------------

// PopupMenu
// ---------
//
Dcl-Proc PopupMenu Export;
  Dcl-PI PopupMenu Packed(3:0);
    iLocation Packed(3:0) Const;
    iRow Packed(3:0) Const;
    iCol Packed(3:0) Const;
    iBorder Packed(3:0) Const;
    iStyle Packed(3:0) Const;
    iRmvMenu Ind Const;
    iTitle Char(70) Const;
    iHeader Char(70) Const;
    iFooter Char(70) Const;
    iFKeyText Char(70) Const;
    iOptions Char(70) Const Dim(15);
  End-PI;

  // Local work fields.

  Dcl-S Row                 Packed(3:0);
  Dcl-S Col                 Packed(3:0);
  Dcl-S CsrCol                 Int(10:0);
  Dcl-S CsrRow                 Int(10:0);
  Dcl-S GUISupport             Ind;
  Dcl-S hCmdBuf                Int(10:0);
  Dcl-S hInpBuf                Int(10:0);
  Dcl-S hWin                   Int(10:0);
  Dcl-S SltOpt              Packed(3:0);
  Dcl-S RowMax              Packed(3:0);
  Dcl-S ColMax              Packed(3:0);
  Dcl-S MaxElmLen           Packed(3:0);
  Dcl-S MaxLen              Packed(3:0);
  Dcl-S NbrElm              Packed(3:0);
  Dcl-S NbrLin              Packed(3:0);
  Dcl-S RtnCode             Packed(3:0);
  Dcl-S Res                    Int(10:0);

  // Validate input parms

  RtnCode = ValidateParms(iLocation:
       iRow:
       iCol:
       iBorder:
       iStyle:
       iOptions);
  If RtnCode = *Zeros;

  // Check if GUI is supported

  CallP QsnQry5250(QsnQ5250: %Size(QsnQ5250): *Omit);

  If %BitAnd(QsnQ5wscb5: x'02') = x'02';
    GUISupport = *On;
  Else;
    GuiSupport = *Off;
  EndIf;

  // Based on input values, calculate the size of the popup menu.

  RtnCode = CalcMenuSize(iStyle:
    GUISupport:
    iTitle:
    iHeader:
    iFooter:
    iFKeyText:
    iOptions:
    MaxLen:
    NbrElm:
    MaxElmLen:
    NbrLin);
  If RtnCode = *Zeros;

    // This section sets the row and column of where to display the
    // popup menu.

    CallP GetScreenSize(RowMax: ColMax);

    // Adjust the popup menu based on the location to display it.

    Select;

      // Display the popup menu at Row, Col for the top left corner.

      When iLocation = pmLocationRowCol;
        Row = iRow;
        Col = iCol;

      // Display the popup menu at the Row, Col where the cursor is
      // currently positioned.

      When iLocation = pmLocationCursor;

        // Disable Window Mode

        RtnCode = QsnSetEnvWinMod('0':
             *Omit:
             *Omit:
             *Omit:
             *Omit:
             *Omit);

        // Get Cursor Address

        If RtnCode = *Zeros;
           RtnCode = QsnGetCsrAdr(CsrRow:
                CsrCol:
                *Omit:
                *Omit);
           Row = CsrRow + 1;
           Col = CsrCol;
        EndIf;

        If RtnCode <> *Zeros;
          RtnCode = pmResultAPIError;
        EndIf;

      // Display the popup menu at the center of the screen, taking
      // into consideration if the screen is in 24x80 or 27x132 mode.

      When iLocation = pmLocationCenter;
        Row = (RowMax - NbrLin - 0) / 2;
        Col = (ColMax - MaxLen - 3) / 2;
    EndSl;

    If RtnCode = *Zeros;
      If Row + NbrLin + 1 > RowMax;
        Row = RowMax - 1 - NbrLin;
      EndIf;
      If Col + MaxLen + 5 > ColMax;
        Col = ColMax - 5 - MaxLen;
      EndIf;

      // Build the menu window.

      RtnCode = CreatePopupWindow(Row:
                                  Col:
                                  NbrLin:
                                  MaxLen:
                                  NbrElm:
                                  iBorder:
                                  iStyle:
                                  iTitle:
                                  iHeader:
                                  iFooter:
                                  iFKeyText:
                                  hCmdBuf:
                                  hInpBuf:
                                  hWin);
       If RtnCode = *Zeros;

      // This section makes adjustmens based on the style to use for
      // the menu.

      // Add options depending on the menu type

              Select;

                    // Classic style: Menu options and a field to enter the sele

                 When iStyle = pmStyleClassic;
                    RtnCode = OptionsAsClassic(hCmdBuf:
                         hInpBuf:
                         hWin:
                         NbrElm:
                         iOptions:
                         %Len(%TrimR(iHeader)):
                         %Len(%TrimR(iFooter)):
                         SltOpt
                         );
                    If RtnCode = *Zeros;
                       RtnCode = SltOpt;
                    EndIf;

                    // Cursor style: User must move the cursor to the selection
                    //               ENTER.

                 When iStyle = pmStyleCursor;
                    RtnCode = OptionsAsCursor(hCmdBuf:
                         hInpBuf:
                         hWin:
                         NbrElm:
                         iOptions:
                         %Len(%TrimR(iHeader)):
                         Row:
                         SltOpt
                         );
                    If RtnCode = *Zeros;
                       RtnCode = SltOpt;
                    EndIf;

                    // Push Button style: Each menu item is a push button. The u
                    //                    click on the button to select the item

                 When iStyle = pmStylePushBtn;

                    If GUISupport = *Off;
                       RtnCode = OptionsAsPushBtnChar(hCmdBuf:
                            hInpBuf:
                            hWin:
                            NbrElm:
                            iOptions:
                            %Len(%TrimR(iHeader)):
                            MaxLen:
                            MaxElmLen:
                            Row:
                            SltOpt
                            );
                       If RtnCode = *Zeros;
                          RtnCode = SltOpt;
                       EndIf;
                    Else;

                       // Display char push buttons

                       RtnCode = OptionsAsPushBtnGUI(hCmdBuf:
                            hInpBuf:
                            hWin:
                            NbrElm:
                            iOptions:
                            %Len(%TrimR(iHeader)):
                            MaxLen:
                            MaxElmLen:
                            Row:
                            SltOpt
                            );
                    EndIf;
                    If RtnCode = *Zeros;
                       RtnCode = SltOpt;
                    EndIf;

              EndSl;

           EndIf;
        EndIf;
     EndIf;

     // Delete Command Buffer

    If hCmdBuf <> *Zeros;
      CallP QsnDltBuf(hCmdBuf: *Omit);
    EndIf;

     // Delete Input Buffer

    If hInpBuf <> *Zeros;
      CallP QsnDltBuf(hInpBuf: *Omit);
    EndIf;

     // End Window

    If hWin <> *Zeros;
      CallP QsnEndWin(hWin: iRmvMenu: *Omit);
    EndIf;

     // Delete environment

    If hWin <> *Zeros;
      CallP QsnDltEnv(hWin: *Omit);
    EndIf;
  EndIf;

  Return RtnCode;

End-Proc PopupMenu;
//
// Internal functions.
// -------------------

// CalcMenuSize
// ------------
// Calculates the height and width of the popup menu, based on the
// number of items and the width of each item.

Dcl-Proc CalcMenuSize;
Dcl-PI CalcMenuSize Packed(3:0);
  iStyle Packed(3:0) Const;
  iGUISupport Ind Const;
  Title Char(74) Const;
  Header Char(74) Const;
  Footer Char(74) Const;
  FKeyText Char(74) Const;
  Options Char(74) Const Dim(15);
  MaxLen Packed(3:0);
  NbrElm Packed(3:0);
  oMaxElmLen Packed(3:0);
  NbrLin Packed(3:0);
End-PI;

  // Local work fields.

  Dcl-S ElmLen Packed(3:0);
  Dcl-S Idx Packed(3:0);
  Dcl-S MaxOptLen Packed(3:0);

  NbrLin = *Zeros;

      MaxLen = %Len(%TrimR(Title));

      // If there is a Header text, then make room for it.

      ElmLen = %Len(%TrimR(Header));
      If ElmLen > *Zeros;
         NbrLin = NbrLin + 2;
      EndIf;
      If ElmLen > MaxLen;
         MaxLen = ElmLen;
      EndIf;

      // If there is a Footer text, then make room for it.

      ElmLen = %Len(%TrimR(Footer));
      If ElmLen > *Zeros;
         NbrLin = NbrLin + 1;
         If ElmLen > MaxLen;
            MaxLen = ElmLen;
         EndIf;
      EndIf;

      // If there is a FKey text, then make room for it.

      ElmLen = %Len(%TrimR(FKeyText));
      If ElmLen > *Zeros;
         NbrLin = NbrLin + 1;
      EndIf;
      If ElmLen > MaxLen;
         MaxLen = ElmLen;
      EndIf;

      NbrElm = %Elem(Options);
      MaxOptLen = *Zeros;

      // Find longest element

      For Idx = 1 to %Elem(Options);

         If Options(Idx) = *Blanks;
            NbrElm = Idx - 1;
            Leave;
         EndIf;

         ElmLen = %Len(%TrimR(Options(Idx)));
         If ElmLen > MaxOptLen;
            MaxOptLen = ElmLen;
         EndIf;

      EndFor;

      If NbrElm > *Zeros;

         oMaxElmLen = MaxOptLen;

         // Make adjustments based on the style.

         Select;

            // Classic style: If more than 9 items, make sure they are aligned.

            When iStyle = pmStyleClassic;
               NbrLin = NbrLin + 2;
               If NbrElm >= 10;
                  MaxOptLen = MaxOptLen + 4;
               Else;
                  MaxOptLen = MaxOptLen + 3;
               EndIf;
               If MaxOptLen > MaxLen;
                  MaxLen = MaxOptLen;
               EndIf;

            // Cursor style: Make more space.

            When iStyle = pmStyleCursor;
               NbrLin = NbrLin + 1;
               If MaxOptLen > MaxLen;
                  MaxLen = MaxOptLen;
               EndIf;

            // Push Button style: Make more space and make menu wide enough.

            When iStyle = pmStylePushBtn;
              NbrLin = NbrLin + 1;
              If iGUISupport = *Off;
                MaxOptLen = MaxOptLen + 2;
              Else;
                MaxOptLen = MaxOptLen + 3;
              EndIf;
              If MaxOptLen > MaxLen;
                MaxLen = MaxOptLen;
              EndIf;
         EndSl;

         // Make sure height and width are within limits.

         NbrLin = NbrLin + NbrElm;
         If NbrLin > 20;
            NbrLin = 20;
         EndIf;
         If MaxLen > 74;
            MaxLen = 74;
         EndIf;

         Return *Zeros;
      Else;
         Return pmResultNoItems;
      EndIf;

End-Proc CalcMenuSize;
//
// CreatePopupWindow
// -----------------
// Creates the popup window by filling the required commands into
// the command buffer.

Dcl-Proc CreatePopupWindow;
Dcl-PI CreatePopupWindow     Int(10:0);
  iRow                   Packed(3:0) Const;
  iCol                   Packed(3:0) Const;
  iNbrRow                Packed(3:0) Const;
  iNbrCol                Packed(3:0) Const;
  iNbrElm                Packed(3:0) Const;
  iBorder                Packed(3:0) Const;
  iStyle                 Packed(3:0) Const;
  iTitle                VarChar(70) Value;
  iHeader               VarChar(70) Value;
  iFooter               VarChar(70) Value;
  iFKeyText             VarChar(70) Value;
  ohCmdBuf                  Int(10:0);
  ohInpBuf                  Int(10:0);
  ohWin                     Int(10:0);
End-PI;

   // Local work fields.

   Dcl-S Res                    Int(10:0);
   Dcl-S StartCol               Int(10:0);
   Dcl-S StartLin               Int(10:0);
   Dcl-S WinDLen                Int(10:0);

      iTitle = %Trim(iTitle);
      iHeader = %Trim(iHeader);
      iFooter = %Trim(iFooter);
      iFKeyText = %Trim(iFKeyText);

      // Default Windows Description

      WinDLen = %Size(QsnWinD);
      QsnWinD = *Allx'00';
      Res = QsnInzWinD(QsnWinD:
           WinDLen:
           *Omit);
      If Res >= *Zeros;

         // Create command buffer

         ohCmdBuf = QsnCrtCmdBuf(300:
              20:
              0:
              *Omit:
              *Omit);

         // Create input buffer

         ohInpBuf = QsnCrtInpBuf(200:
              50:
              0:
              *Omit:
              *Omit);

         // Clear buffers

         Res = QsnClrBuf(ohCmdBuf:
              *Omit);
         If Res >= *Zeros;
            Res = QsnClrBuf(ohInpBuf:
                 *Omit);

            // Create a window

            // Set creation parms.

            QsnWTopR = iRow;
            QsnWLeftC = iCol;
            QsnWNumR = iNbrRow;
            QsnWNumC = iNbrCol;
            QsnWMinR = iNbrRow;
            QsnWMinC = iNbrCol;
            QsnWMaxR = iNbrRow;
            QsnWMaxC = iNbrCol;

            // Set attributes and colours based on border type.

            Select;

                  // Default border

               When iBorder = pmBorderDefault;
                  QsnWTAtrC = QSN_SA_BLU_RI;
                  QsnWTAtrM = QSN_SA_RI;

                  // Reverse blue border

               When iBorder = pmBorderReverseBlue;
                  QsnWGUI =  *Off;
                  QsnWULCh = *Blank;
                  QsnWTopCh= *Blank;
                  QsnWURCh = *Blank;
                  QsnWLCh = *Blank;
                  QsnWRCh = *Blank;
                  QsnWLLCh = *Blank;
                  QsnWBotCh = *Blank;
                  QsnWLRCh = *Blank;
                  QsnWAtrC2 = QSN_SA_BLU_RI;
                  QsnWTAtrC = x'00';
                  QsnWAtrM2 = QSN_SA_RI;
                  QsnWTAtrM = x'00';

                  // Reserve green broder

               When iBorder = pmBorderReverseGreen;
                  QsnWGUI =  *Off;
                  QsnWULCh = *Blank;
                  QsnWTopCh= *Blank;
                  QsnWURCh = *Blank;
                  QsnWLCh = *Blank;
                  QsnWRCh = *Blank;
                  QsnWLLCh = *Blank;
                  QsnWBotCh = *Blank;
                  QsnWLRCh = *Blank;
                  QsnWAtrC2 = QSN_SA_GRN_RI;
                  QsnWTAtrC = x'00';
                  QsnWAtrM2 = QSN_SA_RI;
                  QsnWTAtrM = x'00';

                  // Alert border

               When iBorder = pmBorderAlert;
                  QsnWGUI =  *Off;
                  QsnWULCh = *Blank;
                  QsnWTopCh= *Blank;
                  QsnWURCh = *Blank;
                  QsnWLCh = *Blank;
                  QsnWRCh = *Blank;
                  QsnWLLCh = *Blank;
                  QsnWBotCh = *Blank;
                  QsnWLRCh = *Blank;
                  QsnWAtrC2 = QSN_SA_RED_RI;
                  QsnWTAtrC = x'00';
                  QsnWAtrM2 = QSN_SA_RI;
                  QsnWTAtrM = x'00';
            EndSl;

            If iTitle > *Blanks;
               QsnWTtlO = 76;
               QsnWTtl  = iTitle;
               QsnWTtlL = %Len(iTitle);
            EndIf;

            ohWin = QsnCrtWin(QsnWinD:
                 WinDLen:
                 *Omit:
                 *Omit:
                 *Omit:
                 *Omit:
                 *Omit:
                 *Omit:
                 *Omit);

            // Set Current window

            Res = QsnSetCurWin(ohWin:
                 *Omit);

            // Set Environment Window Mode

            QsnEWAtrC = '1';
            QsnEWULR = QsnWTopR;
            QsnEWULC = QsnWLeftC;
            QsnEWNumR = QsnWNumR;
            QsnEWNumC = QsnWNumC + 2;

            Res = QsnSetEnvWinMod('1':
                 *Omit:
                 QsnEnvWM:
                 %Size(QsnEnvWM):
                 *Omit:
                 *Omit);
         EndIf;
      EndIf;

      If Res = *Zeros;

      // Starting point for constants

      StartLin = *Zeros;

      // Write Header text

      If iHeader > *Blanks;
         StartLin = StartLin + 1;
         StartCol = ((iNbrCol - %Len(iHeader))
              / 2) + 2;
         Res = QsnWrtDta(iHeader:
              %Len(iHeader):
              *Omit:
              StartLin:
              StartCol:
              QSN_SA_HI:
              *Omit:
              QSN_SA_HI:
              *Omit:
              ohCmdBuf:
              *Omit:
              *Omit);
         StartLin = StartLin + 1;
      EndIf;

      If Res = *Zeros;

      // Adjust for number of element in menu

      StartLin = StartLin + iNbrElm + 1;

      // Write footer

      If iFooter > *Blanks;
         StartLin = StartLin + 1;
         Res = QsnWrtDta(iFooter:
              %Len(iFooter):
              *Omit:
              StartLin:
              2:
              QSN_SA_NORM:
              *Omit:
              QSN_SA_NORM:
              *Omit:
              ohCmdBuf:
              *Omit:
              *Omit);
         If iStyle = pmStyleClassic;
            StartLin = StartLin + 1;
         EndIf;
      EndIf;

      If Res = *Zeros;

      // Write F-Key text

      If iFKeyText > *Blanks;
         StartLin = StartLin + 1;
         Res = QsnWrtDta(iFKeyText:
              %Len(iFKeyText):
              *Omit:
              StartLin:
              2:
              QSN_SA_NORM:
              *Omit:
              QSN_SA_BLU:
              *Omit:
              ohCmdBuf:
              *Omit:
              *Omit);
      EndIf;
      EndIf;
    EndIf;
    EndIf;

  If Res <> *Zeros;
    Res = pmResultAPIError;
  EndIf;

  Return Res;

End-Proc CreatePopupWindow;
//
// GetScreenSize
// ----------------
// Returns the size of the screen.

Dcl-Proc GetScreenSize;
Dcl-PI GetScreenSize;
  oRows                Packed(3:0);
  oCols                Packed(3:0);
End-PI;

   Dcl-C C24ROWS                   Const(24);
   Dcl-C C80COLS                   Const(80);
   Dcl-C C27ROWS                   Const(27);
   Dcl-C C132COLS                  Const(132);
   Dcl-C C24X80MODE                Const('3');
   Dcl-C C27X132MODE               Const('4');

   // Local work fields.

   Dcl-S wDspMode              Char(1);

      CallP QsnRtvMod(wDspMode:
             *Omit:
             *Omit);

      Select;

         When wDspMode = c24x80Mode;
            oRows = c24Rows;
            oCols = c80Cols;

         When wDspMode = c27x132Mode;
            oRows = c27Rows;
            oCols = c132Cols;

            // This should not be possible.

         Other;
            oRows = -1;
            oCols = -1;
      EndSl;

      Return;

End-Proc GetScreenSize;
//
// OptionsAsClassic
// ----------------
// Build the menu items as classic menu options and add an entry field.

Dcl-Proc OptionsAsClassic;
Dcl-PI OptionsAsClassic      Int(10:0);
  ihCmdBuf                  Int(10:0) Const;
  ihInpBuf                  Int(10:0) Const;
  ihWin                     Int(10:0) Const;
  iNbrElm                Packed(3:0) Const;
  iOptions                 Char(70) Const Dim(15);
  iHdrLen                Packed(3:0) Const;
  iFtrLen                Packed(3:0) Const;
  oSltOpt                Packed(3:0);
End-PI;

   // Local work fields.

   Dcl-S Answer                Char(2);
   Dcl-S FldLen              Packed(1:0);
   Dcl-S Idx                 Packed(3:0);
   Dcl-S InpFldLin           Packed(3:0);
   Dcl-S Len                 Packed(9:0);
   Dcl-S Offset              Packed(3:0);
   Dcl-S OneChar               Char(1);
   Dcl-S pInputData         Pointer;
   Dcl-S Res                    Int(10:0);
   Dcl-S TempString         VarChar(70);
   Dcl-S TwoDigits            Zoned(2:0);

   Dcl-DS InputData                Based(pInputData);
      Row                      Uns(3:0);
      Col                      Uns(3:0);
      AID                      Char(1);
      Field                    Char(500);
   End-DS;

   // DS for converting char to numeric

   Dcl-DS *N;
      TheChar                  Char(1) Pos(1);
      TheNum                  Zoned(1:0) Pos(1);
   End-DS;

      oSltOpt = *Zeros;

      // Dertermine where to start the list of items.

      If iHdrLen > *Zeros;
         Offset = 2;
         InpFldLin = 4;
      Else;
         Offset = *Zeros;
         InpFldLin = 2;
      EndIf;

      // Adjust if a footer is entered.

      If iFtrLen > *Zeros;
         InpFldLin = InpFldLin + 1;
      EndIf;

      InpFldLin = InpFldLin + iNbrElm;

      // Write each item, preceeded by the item nbr, to the window.

      For Idx = 1 to iNbrElm;
         TwoDigits = Idx;
         TempString = %EditC(TwoDigits: '4');
         If iNbrElm < 10;
            TempString = %TrimL(TempString);
         EndIf;
         TempString = TempString + '. ' +
              %Trim(iOptions(Idx));

         // Write option to buffer

         Res = QsnWrtDta(TempString:
              %Len(TempString):
              *Omit:
              Idx + Offset:
              2:
              QSN_SA_NORM:
              *Omit:
              QSN_SA_NORM:
              *Omit:
              ihCmdBuf:
              *Omit:
              *Omit);

      EndFor;

      // Add Input field for selection

      Res = QsnWrtDta('===>':
           4:
           *Omit:
           InpFldLin:
           2:
           *Omit:
           *Omit:
           *Omit:
           *Omit:
           ihCmdBuf:
           *Omit:
           *Omit);

      // Loop until valid input

      DoU AID = Qsn_Enter Or
      AID = Qsn_F3 Or
      AID = Qsn_F12;

         // Set Field

         If iNbrElm < 10;
            FldLen = 1;
         Else;
            FldLen = 2;
         EndIf;

         Res = QsnSetFld(1:
              FldLen:
              InpFldLin:
              7:
              QSN_FFW_NUM_ONLY +
              QSN_FFW_MDT:
              *Omit:
              0:
              QSN_SA_UL:
              QSN_SA_GRN_UL:
              ihCmdBuf:
              *Omit:
              *Omit);

         // Read Input

         Res = QsnReadInp(QSN_CC1_NULL:
              QSN_CC2_NO_IC:
              *Omit:
              *Omit:
              ihCmdBuf:
              *Omit:
              *Omit);

         // Put and Get Buffer

         Res = QsnPutGetBuf(ihCmdBuf:
              ihInpBuf:
              *Omit:
              *Omit);

         // Retrieve current window

         Res = QsnRtvCurWin(ihWin:
              *Omit);
         If Res > *Zeros;
            Res = *Zeros;
         EndIf;

         // Get input data

         pInputData = QsnRtvDta(ihInpBuf:
              *Omit:
              *Omit);
         Select;

               // ENTER key pressed.

            When AID = Qsn_Enter;

               // Extract field data

               Len = QsnRtvDtaLen(ihInpBuf:
                    *Omit:
                    *Omit) -
                    %Size(Row) -
                    %Size(Col) -
                    %Size(AId);
               If Len > *Zeros;
                  Answer = %Trim(%SubSt(Field: 1: Len));

                  // Scrup data out

                  OneChar = %Subst(Answer: 1: 1);
                  If OneChar >= '0' And
                  OneChar <= '9';
                     TheChar = OneChar;
                     oSltOpt = TheNum;
                  EndIf;

                  OneChar = %Subst(Answer: 2: 1);
                  If OneChar >= '0' And
                  OneChar <= '9';
                     oSltOpt = oSltOpt * 10;
                     TheChar = OneChar;
                     oSltOpt = oSltOpt + TheNum;
                  EndIf;

                  If oSltOpt = *Zeros Or
                  oSltOpt > iNbrElm;
                     AID = *Allx'00';

                     // Clear buffers

                     Res = QsnClrBuf(ihCmdBuf:
                          *Omit);
                     If Res >= *Zeros;
                        Res = QsnClrBuf(ihInpBuf:
                             *Omit);
                     EndIf;
                  EndIf;
               EndIf;

               // F3 or F12 key pressed.

            When AID = Qsn_F3 Or AID = Qsn_F12;

               // Do not do anything, as this will terminate the loop.

            Other;
               AID = *Allx'00';

               // Clear buffers

               Res = QsnClrBuf(ihCmdBuf:
                    *Omit);
               If Res >= *Zeros;
                  Res = QsnClrBuf(ihInpBuf:
                       *Omit);
               EndIf;
         EndSl;
      EndDo;

  If Res = -1;
    Res = pmResultAPIError;
  EndIf;

  Return Res;

End-Proc OptionsAsClassic;
//
// OptionsAsCursor
// ---------------
// Build the menu items for selection by moving the cursor.

Dcl-Proc OptionsAsCursor;
Dcl-PI OptionsAsCursor       Int(10:0);
  ihCmdBuf                  Int(10:0) Const;
  ihInpBuf                  Int(10:0) Const;
  ihWin                     Int(10:0) Const;
  iNbrElm                Packed(3:0) Const;
  iOptions                 Char(70) Const Dim(15);
  iHdrLen                Packed(3:0) Const;
  iFtrLen                Packed(3:0) Const;
  oSltOpt                Packed(3:0);
End-PI;

   // Local work fields.

   Dcl-S Idx                 Packed(3:0);
   Dcl-S Offset              Packed(3:0);
   Dcl-S pInputData         Pointer;
   Dcl-S Res                    Int(10:0);
   Dcl-S TempString         VarChar(70);

   Dcl-DS InputData                Based(pInputData);
      Row                      Uns(3:0);
      Col                      Uns(3:0);
      AID                      Char(1);
      Field                    Char(500);
   End-DS;

      oSltOpt = *Zeros;

      If iHdrLen > *Zeros;
         Offset = 2;
      Else;
         Offset = *Zeros;
      EndIf;

      // Write each option to the window.

      For Idx = 1 to iNbrElm;
         TempString = %Trim(iOptions(Idx));

         // Write option to buffer

         Res = QsnWrtDta(TempString:
              %Len(TempString):
              *Omit:
              Idx + Offset:
              2:
              QSN_SA_NORM:
              *Omit:
              QSN_SA_NORM:
              *Omit:
              ihCmdBuf:
              *Omit:
              *Omit);

      EndFor;

      // Loop until valid input

      DoU AID = Qsn_Enter Or
      AID = Qsn_F3 Or
      AID = Qsn_F12;

         // Set the cursor position

         Res = QsnSetCsrAdr(*Omit:
              1 + Offset:
              2:
              ihCmdBuf:
              *Omit:
              *Omit);

         // Read Input

         Res = QsnReadInp(QSN_CC1_NULL:
              QSN_CC2_NO_IC:
              *Omit:
              *Omit:
              ihCmdBuf:
              *Omit:
              *Omit);

         // Put and Get Buffer

         Res = QsnPutGetBuf(ihCmdBuf:
              ihInpBuf:
              *Omit:
              *Omit);

         // Retrieve current window

         Res = QsnRtvCurWin(ihWin:
              *Omit);
         If Res > *Zeros;
            Res = *Zeros;
         EndIf;

         // Get input data

         pInputData = QsnRtvDta(ihInpBuf:
              *Omit:
              *Omit);
         Select;

               // ENTER key pressed.

            When AID = Qsn_Enter;

               // Calculate the selected line

               oSltOpt = Row - iFtrLen - Offset;

               If oSltOpt < 1 Or
               oSltOpt > iNbrElm;
                  AID = *Allx'00';

                  // Clear buffers

                  Res = QsnClrBuf(ihCmdBuf:
                       *Omit);
                  If Res >= *Zeros;
                     Res = QsnClrBuf(ihInpBuf:
                          *Omit);
                  EndIf;
               EndIf;

               // F3 or F12 key pressed.

            When AID = Qsn_F3 Or AID = Qsn_F12;

               // Do not do anything, as this will terminate the loop.

            Other;
               AID = *Allx'00';

               // Clear buffers

               Res = QsnClrBuf(ihCmdBuf:
                    *Omit);
               If Res >= *Zeros;
                  Res = QsnClrBuf(ihInpBuf:
                       *Omit);
               EndIf;
         EndSl;
      EndDo;

  If Res = -1;
    Res = pmResultAPIError;
  EndIf;

  Return Res;

End-Proc OptionsAsCursor;
//
// OptionsAsPushBtnChar
// --------------------
// Build the menu items as push buttons, in char format for non-GUI
// terminals.

Dcl-Proc OptionsAsPushBtnChar;
Dcl-PI OptionsAsPushBtnChar  Int(10:0);
  ihCmdBuf                  Int(10:0) Const;
  ihInpBuf                  Int(10:0) Const;
  ihWin                     Int(10:0) Const;
  iNbrElm                Packed(3:0) Const;
  iOptions                 Char(70) Const Dim(15);
  iHdrLen                Packed(3:0) Const;
  iMaxLen                Packed(3:0) Const;
  iMaxElmLen             Packed(3:0) Const;
  iRow                   Packed(3:0) Const;
  oSltOpt                Packed(3:0);
End-PI;

   // Local work fields.

   Dcl-S FieldXPos           Packed(3:0);
   Dcl-S Idx                 Packed(3:0);
   Dcl-S Offset              Packed(3:0);
   Dcl-S PadSpaces           Packed(3:0);
   Dcl-S pInputData         Pointer;
   Dcl-S Res                    Int(10:0);
   Dcl-S Spaces                Char(75) Inz(*Blanks);
   Dcl-S TempString         VarChar(70);

   Dcl-DS InputData                Based(pInputData);
      Row                      Uns(3:0);
      Col                      Uns(3:0);
      AID                      Char(1);
      Field                    Char(500);
   End-DS;

      oSltOpt = *Zeros;

      // Calculate pushbutton start pos

      FieldXPos = (iMaxLen - iMaxElmLen) / 2;
      FieldXPos = FieldXPos + 2;

      // Compensate starting line if no Header

      If iHdrLen > *Zeros;
         Offset = 2;
      Else;
         Offset = *Zeros;
      EndIf;

      // Loop though the items and draw them

      For Idx = 1 to iNbrElm;
         TempString = '<' + %Trim(iOptions(Idx));
         PadSpaces = iMaxElmLen -
              %Len(TempString) + 1;
         If PadSpaces > *Zeros;
            TempString = TempString + %SubSt(
                 Spaces:
                 1:
                 PadSpaces);
         EndIf;
         TempString = TempString + '>';

         // Input field to allow for cursor to shift between pushbuttons

         Res = QsnSetFld(Idx:
              1:
              Idx + Offset:
              FieldXPos:
              QSN_FFW_IO:
              *Omit:
              0:
              QSN_SA_NORM:
              *Omit:
              ihCmdBuf:
              *Omit:
              *Omit);

         // Write option to buffer

         Res = QsnWrtDta(TempString:
              %Len(TempString):
              *Omit:
              Idx + Offset:
              FieldXPos - 1:
              QSN_SA_NORM:
              *Omit:
              QSN_SA_NORM:
              *Omit:
              ihCmdBuf:
              *Omit:
              *Omit);
      EndFor;

      // Set the cursor position

      Res = QsnSetCsrAdr(1:
           *Omit:
           *Omit:
           ihCmdBuf:
           *Omit:
           *Omit);

      // Loop until valid input

      DoU AID = Qsn_Enter Or
      AID = Qsn_F3 Or
      AID = Qsn_F12;

         // Read Input

         Res = QsnReadInp(QSN_CC1_NULL:
              QSN_CC2_NO_IC:
              *Omit:
              *Omit:
              ihCmdBuf:
              *Omit:
              *Omit);

         // Put and Get Buffer

         Res = QsnPutGetBuf(ihCmdBuf:
              ihInpBuf:
              *Omit:
              *Omit);

         // Retrieve current window

         Res = QsnRtvCurWin(ihWin:
              *Omit);
         If Res > *Zeros;
            Res = *Zeros;
         EndIf;

         // Get input data

         pInputData = QsnRtvDta(ihInpBuf:
              *Omit:
              *Omit);
         Select;

               // ENTER key pressed.

            When AID = Qsn_Enter;

               // Calculate the selected pushbutton

               oSltOpt = Row - iRow - Offset;

               If oSltOpt < 1 Or
               oSltOpt > iNbrElm;
                  AID = *Allx'00';

                  // Clear buffers

                  Res = QsnClrBuf(ihCmdBuf:
                       *Omit);
                  If Res >= *Zeros;
                     Res = QsnClrBuf(ihInpBuf:
                          *Omit);
                  EndIf;
               EndIf;

               // F3 or F12 key pressed.

            When AID = Qsn_F3 Or AID = Qsn_F12;

               // Do not do anything, as this will terminate the loop.

            Other;
               AID = *Allx'00';

               // Clear buffers

               Res = QsnClrBuf(ihCmdBuf:
                    *Omit);
               If Res >= *Zeros;
                  Res = QsnClrBuf(ihInpBuf:
                       *Omit);
               EndIf;
         EndSl;
      EndDo;

  If Res = -1;
    Res = pmResultAPIError;
  EndIf;

  Return Res;

End-Proc OptionsAsPushBtnChar;
//
// OptionsAsPushBtnGUI
// -------------------
// Build the menu items as GUI push buttons.

Dcl-Proc OptionsAsPushBtnGUI;
Dcl-PI OptionsAsPushBtnGUI   Int(10:0);
  ihCmdBuf                  Int(10:0) Const;
  ihInpBuf                  Int(10:0) Const;
  ihWin                     Int(10:0) Const;
  iNbrElm                Packed(3:0) Const;
  iOptions                 Char(70) Const Dim(15);
  iHdrLen                Packed(3:0) Const;
  iMaxLen                Packed(3:0) Const;
  iMaxElmLen             Packed(3:0) Const;
  iRow                   Packed(3:0) Const;
  oSltOpt                Packed(3:0);
End-PI;

// Local work fileds.

   Dcl-S FieldXPos           Packed(3:0);
   Dcl-S Idx                  Zoned(2:0);
   Dcl-S Offset              Packed(3:0);
   Dcl-S PadSpaces           Packed(3:0);
   Dcl-S pInputData         Pointer;
   Dcl-S Res                    Int(10:0);
   Dcl-S Spaces                Char(75) Inz(*Blanks);
   Dcl-S TempString         VarChar(70);

   Dcl-DS InputData                Based(pInputData);
      Row                      Uns(3:0);
      Col                      Uns(3:0);
      AID                      Char(1);
      Field                    Char(500);
   End-DS;

      oSltOpt = *Zeros;

      // Calculate pushbutton start pos

      FieldXPos = (iMaxLen - iMaxElmLen) / 2;

      // Compensate starting line if no Header

      If iHdrLen > *Zeros;
         Offset = 3;
      Else;
         Offset = 1;
      EndIf;

      // Fill the Major Structure

      MJLen = %Size(MJStruc);
      MJClass = x'D9';
      MJType = x'50';
      MJFlag1 = x'04';
      MJFlag2 = x'14';
      MJFlag3 = x'00';
      // Push buttons
      MJTPSlt = x'41';
      MJGUIDev = x'20';
      MJNWSwMne = x'30';
      MJNWSwoMne = x'30';
      MJRes1 = x'00';
      MJRes2 = x'00';
      MJTextSize = iMaxElmLen + 2;
      MJRows = iNbrElm;
      MJCols = 1;
      MJPad = 0;
      MJNumSep = '0';
      MJCounSltChr = '/';
      MJMousCnlAID = x'00';

      Res = QsnWrtSFMaj(MJStruc:
           %Size(MJStruc):
           *Omit:
           Offset:
           FieldXPos:
           ihCmdBuf:
           *Omit:
           *Omit);

      // Fill the Minor Structure

      MIType = x'10';
      MIFlag1 = x'01';
      MIFlag2 = x'00';
      MIFlag3 = x'e0';

      // Loop though the options and draw them

      For Idx = 1 to iNbrElm;

         // Fill the individual part of Minor Structure

         MIValue = '1';
         MIChoText = %Trim(iOptions(Idx));
         MILen = %Size(MIStruc) - %Size(MIChoText)
              + %Len(%Trim(iOptions(Idx)));

         Res = QsnWrtSFMin(MIStruc:
              MILen:
              ihCmdBuf:
              *Omit:
              *Omit);
      EndFor;

      // Loop until valid input

      DoU AID = Qsn_Enter Or
      AID = Qsn_F3 Or
      AID = Qsn_F12;

         // Read Input

         Res = QsnReadInp(QSN_CC1_NULL:
              QSN_CC2_NO_IC:
              *Omit:
              *Omit:
              ihCmdBuf:
              *Omit:
              *Omit);

         // Put and Get Buffer

         Res = QsnPutGetBuf(ihCmdBuf:
              ihInpBuf:
              *Omit:
              *Omit);

         // Retrieve current window

         Res = QsnRtvCurWin(ihWin:
              *Omit);
         If Res > *Zeros;
            Res = *Zeros;
         EndIf;

         // Get input data

         pInputData = QsnRtvDta(ihInpBuf:
              *Omit:
              *Omit);
         Select;

               // ENTER key pressed.

            When AID = Qsn_Enter;

               // Calculate the selected pushbutton

               oSltOpt = Row - iRow - Offset + 1;

               If oSltOpt < 1 Or
               oSltOpt > iNbrElm;
                  AID = *Allx'00';

                  // Clear buffers

                  Res = QsnClrBuf(ihCmdBuf:
                       *Omit);
                  If Res >= *Zeros;
                     Res = QsnClrBuf(ihInpBuf:
                          *Omit);
                  EndIf;
               EndIf;

               // F3 or F12 key pressed.

            When AID = Qsn_F3 Or AID = Qsn_F12;

               // Do not do anything, as this will terminate the loop.

            Other;
               AID = *Allx'00';

               // Clear buffers

               Res = QsnClrBuf(ihCmdBuf:
                    *Omit);
               If Res >= *Zeros;
                  Res = QsnClrBuf(ihInpBuf:
                       *Omit);
               EndIf;
         EndSl;
      EndDo;

  If Res = -1;
    Res = pmResultAPIError;
  EndIf;

  Return Res;

End-Proc OptionsAsPushBtnGUI;
//
// ValidateParms
// -------------
// Validates that the input parms are within limits.

Dcl-Proc ValidateParms;
Dcl-PI ValidateParms      Packed(3:0);
  iLocation              Packed(3:0) Const;
  iRow                   Packed(3:0) Const;
  iCol                   Packed(3:0) Const;
  iBorder                Packed(3:0) Const;
  iStyle                 Packed(3:0) Const;
  iOptions                 Char(70) Const Dim(15);
End-PI;

  // Local work fields.

  Dcl-S RtnCode Packed(3:0) Inz(*Zeros);

  Select;

    // Location

    When iLocation < pmLocationCenter Or
         iLocation > pmLocationRowCol;
      RtnCode = pmResultLocationInvalid;

    // Row

    When iRow < *Zeros Or
         iRow > 27;
      RtnCode = pmResultRowInvalid;

    // Col

    When iCol < *Zeros Or
         iCol > 132;
      RtnCode = pmResultColInvalid;

    // Style

    When iStyle < pmStyleClassic Or
         iStyle > pmStylePushBtn;
      RtnCode = pmResultStyleInvalid;

    // Border

    When iBorder < pmBorderDefault Or
         iBorder > pmBorderAlert;
      RtnCode = pmResultBorderInvalid;

    // Options

    When iOptions(1) = *Blanks;
      RtnCode = pmResultNoItems;
  EndSl;

  Return RtnCode;

End-Proc ValidateParms;
