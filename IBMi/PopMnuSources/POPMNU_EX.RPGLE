**Free
//
// PopMnu_Ex
// ---------
// Example program for the PopupMenu() function.
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
// Copymember for imported functions.
// ----------------------------------
/copy qrpglesrc,PopMnu_Pr

// Variables

Dcl-S Msg                   Char(20);
Dcl-S Row                 Packed(3:0);
Dcl-S Col                 Packed(3:0);
Dcl-S Location            Packed(3:0);
Dcl-S Style               Packed(3:0);
Dcl-S Border              Packed(3:0) Inz(pmBorderDefault);
Dcl-S RmvMenu Ind Inz(*Off);
Dcl-S Title                 Char(50);
Dcl-S Header                Char(50);
Dcl-S Footer                Char(50);
Dcl-S FKeyText              Char(50);
Dcl-S Options               Char(50) Dim(15);
Dcl-S Res                    Int(10:0);
Dcl-S Res2                   Int(10:0);

DoU Res = 0;
  Location = pmLocationRowCol;
  Row = 4;
  Col = 10;
  Border = pmBorderDefault;
  Style = pmStylePushBtn;

  Title = 'Popup Menu';
  Header = 'This is the header';
  Footer = 'This is the footer';
  FKeyText = 'ENTER=Select F3=Exit';
  Options(1) = 'Locations';
  Options(2) = 'Styles';
  Options(3) = 'Borders';
  Options(4) = 'Demo menu';

  Res = PopupMenu(Location:
                  Row:
                  Col:
                  Border:
                  Style:
                  RmvMenu:
                  Title:
                  Header:
                  Footer:
                  FKeyText:
                  Options);

  Select;

    // Locations

    When Res = 1;
      Location = pmLocationRowCol;
      Row = 6;
      Col = 15;
      Border = pmBorderDefault;
      Style = pmStylePushBtn;

      Title = 'Locations';
      Header = 'Select a Location';
      FKeyText = 'ENTER=Select F3=Exit';
      Options(1) = 'At 3 x 45';
      Options(2) = 'Center of screen';
      Options(3) = 'At cursor location';
      Options(4) = '';

      Res = PopupMenu(Location:
                      Row:
                      Col:
                      Border:
                      Style:
                      RmvMenu:
                      Title:
                      Header:
                      Footer:
                      FKeyText:
                      Options);

      Select;

        When Res = 1;
          Location = pmLocationRowCol;
          Row = 3;
          Col = 45;

        When Res = 2;
          Location = pmLocationCenter;

        When Res = 3;
          Location = pmLocationCursor;
      EndSl;

      If Res >= 1 and Res <= 3;
        Title = 'Locations';
        Header = 'Selected loc';
        FKeyText = 'ENTER=Select F3=Exit';
        Options(1) = 'Some option';
        Options(2) = 'Some option';
        Options(3) = 'Some option';
        Options(4) = 'Some option';

        Res2 = PopupMenu(Location:
                         Row:
                         Col:
                         Border:
                         Style:
                         *On:
                         Title:
                         Header:
                         Footer:
                         FKeyText:
                         Options);
      EndIf;

    // Styles

    When Res = 2;
      Location = pmLocationRowCol;
      Row = 6;
      Col = 15;
      Border = pmBorderDefault;
      Style = pmStylePushBtn;

      Title = 'Styles';
      Header = 'Select a Style';
      FKeyText = 'ENTER=Select F3=Exit';
      Options(1) = 'Classic';
      Options(2) = 'Cursor selection';
      Options(3) = 'Push buttons';
      Options(4) = '';

      Res = PopupMenu(Location:
                      Row:
                      Col:
                      Border:
                      Style:
                      RmvMenu:
                      Title:
                      Header:
                      Footer:
                      FKeyText:
                      Options);
      Select;

        When Res = 1;
           Style = pmStyleClassic;

        When Res = 2;
           Style = pmStyleCursor;

        When Res = 3;
           Style = pmStylePushBtn;
      EndSl;

      If Res >= 1 And Res <= 3;
        Location = pmLocationCenter;
        Title = 'Styles';
        Header = 'Selected style';
        FKeyText = 'ENTER=Select F3=Exit';
        Options(1) = 'Some option';
        Options(2) = 'Some option';
        Options(3) = 'Some option';
        Options(4) = 'Some option';

        Res2 = PopupMenu(Location:
                         Row:
                         Col:
                         Border:
                         Style:
                         *On:
                         Title:
                         Header:
                         Footer:
                         FKeyText:
                         Options);
        If Res2 >= 1 and Res2 <= 4;
           Msg = 'You selected: ' + %Char(Res2);
           Dsply Msg;
        EndIf;
      EndIf;

      // Borders

      When Res = 3;
        Location = pmLocationRowCol;
        Row = 6;
        Col = 15;
        Border = pmBorderDefault;
        Style = pmStylePushBtn;

        Title = 'Borders';
        Header = 'Select a Border';
        FKeyText = 'ENTER=Select F3=Exit';
        Options(1) = 'Default';
        Options(2) = 'Reverse Blue';
        Options(3) = 'Reverse Green';
        Options(4) = 'Alert';

        Res = PopupMenu(Location:
                        Row:
                        Col:
                        Border:
                        Style:
                        RmvMenu:
                        Title:
                        Header:
                        Footer:
                        FKeyText:
                        Options);
        Select;
          When Res = 1;
            Border = pmBorderDefault;

          When Res = 2;
            Border = pmBorderReverseBlue;

          When Res = 3;
            Border = pmBorderReverseGreen;

          When Res = 4;
            Border = pmBorderAlert;
          EndSl;

          If Res >= 1 And Res <= 4;
            Location = pmLocationCenter;
            Title = 'Borders';
            Header = 'Selected border';
            FKeyText = 'ENTER=Select F3=Exit';
            Options(1) = 'Some option';
            Options(2) = 'Some option';
            Options(3) = 'Some option';
            Options(4) = 'Some option';

            Res2 = PopupMenu(Location:
                             Row:
                             Col:
                             Border:
                             Style:
                             *On:
                             Title:
                             Header:
                             Footer:
                             FKeyText:
                             Options);
          EndIf;

      // Demo menu

      When Res = 4;
        Location = pmLocationCenter;
        Style = pmStylePushBtn;
        Border = pmBorderDefault;

        Title = 'Work Management';
        Header = 'Select option';
        FKeyText = 'ENTER=Select F3=Exit';
        Options(1) = 'Work with active jobs';
        Options(2) = 'Work with disc status';
        Options(3) = 'Work with outqueues';
        Options(4) = 'Work with users';
        Res2 = PopupMenu(Location:
                         *Zeros:
                         *Zeros:
                         Border:
                         Style:
                         *On:
                         Title:
                         Header:
                         Footer:
                         FKeyText:
                         Options);
        If Res2 >= 1 and Res2 <= 4;
          Msg = 'You selected: ' + %Char(Res2);
          Dsply Msg;
        EndIf;
      EndSl;

    EndDo;

  *InLr = *On;
  Return;
