**Free
//
// PopMnu_Pr
// ---------
// Prototype for function PopupMenu() that shows a popup menu and lets
// the user select an option.
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
Dcl-PR PopupMenu Packed(3:0);
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
End-PR;
//
// The procedure PopupMenu must be called with these parameters:
//
// PopupMenu(
//           location:  Controls where the popup menu is to be
//                      displayed. See constants for details.
//           row:       If location is pmLocationRowCol then set this
//                      to the row (1 - 27). Otherwise, set to zero.
//           col:       If location is pmLocationRowCol then set this
//                      to the col (1 - 132).Otherwise, set to zero.
//           border:    The type of border to display around the
//                      popup menu.
//           style:     The style of the menu.
//                      pmStyleClassic will display a option number
//                      in front of the option. An entry field to enter
//                      the option number is displayed. Selection is
//                      done by entering the number and pressing the
//                      ENTER key.
//                      pmStyleCursor will display the options centered
//                      in the window. Selection is done by moving the
//                      cursor to the option in question and pressing
//                      the ENTER key.
//                      pmStyleBtn will display each option as a push
//                      button either in GUI or Text mode, depending
//                      on the terminal (emulator) capabilities.
//                      Selection is done by clicking on the push
//                      button in question with the mouse or using the
//                      arrow keys and pressing the ENTER key.
//           rmvmenu:   Set to *On to remove the popup menu after
//                      the user have made a selection. Set to *Off
//                      to leave the popup menu on screen. This will
//                      require that caller redraw the screen to
//                      remove the popup menu.
//           title:     The title of the popup menu. Is displayed in
//                      top of the border of the popup menu. Can be
//                      set to *blanks.
//           header:    The header for the menu options. Is displayed
//                      at the top of the popup window above the
//                      menu items. Can be set to *blanks.
//           footer:    The footer for the menu options. Is displayed
//                      just below the menu options. Can be set to
//                      *blanks.
//           fkeytext:  Aline to be display with F-keys. The line will
//                      be displayed in blue colour.
//           options:   An array with 15 options. The options must be
//                      filled from the begining of the array.
//                      Not used options must be set to *blanks.
//           )
//
// Constants
// ---------
//
// pmLocation*
// -----------
// The place to display the menu.
//
// pmLocationCenter:
//
Dcl-C pmLocationCenter Const(1);
//
// pmLocationCursor:
//
Dcl-C pmLocationCursor Const(2);
//
// pmLocationRowCol:
//
Dcl-C pmLocationRowCol Const(3);
//
// pmStyle*
// --------
// The style of the menu.
//
// pmStyleClassic:
//
Dcl-C pmStyleClassic Const(1);
//
// pmStyleCursor:
//
Dcl-C pmStyleCursor Const(2);
//
// pmStylePushBtn:
//
Dcl-C pmStylePushBtn Const(3);
//
// pmBorder*
// ---------
// The border of the menu.
//
// pmBorderDefault:
//
Dcl-C pmBorderDefault Const(1);
//
// pmBorderReverseBlue:
//
Dcl-C pmBorderReverseBlue Const(2);
//
// pmBorderReverseGreen:
//
Dcl-C pmBorderReverseGreen Const(3);
//
// pmBorderAlert:
//
Dcl-C pmBorderAlert Const(4);
//
// pmResult*
// ---------
// pmResultAPIError:
//
Dcl-C pmResultAPIError Const(-7);
//
// pmResultLocationInvalid:
//
Dcl-C pmResultLocationInvalid Const(-6);
//
// pmResultRowInvalid:
//
Dcl-C pmResultRowInvalid Const(-5);
//
// pmResultColInvalid:
//
Dcl-C pmResultColInvalid Const(-4);
//
// pmResultStyleInvalid:
//
Dcl-C pmResultStyleInvalid Const(-3);
//
// pmResultBorderInvalid:
//
Dcl-C pmResultBorderInvalid Const(-2);
//
// pmResultNoItems:
//
Dcl-C pmResultNoItems Const(-1);
//
// pmResultNoSelection:
//
Dcl-C pmResultNoSelection Const(0);
