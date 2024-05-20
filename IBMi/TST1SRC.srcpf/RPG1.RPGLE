     HOPTION(*NODEBUGIO:*SRCSTMT)
     HDFTACTGRP(*NO)
     HDEBUG(*YES)
      *
     FLF1       UF A E           K DISK
     FTSTSUBF01 CF   E             WORKSTN
     F                                     SFILE(SFLDTA01:rcdnbr)
      *
     D RCDNBR          S              4S 0
      *
     C     kf1           klist
     C                   kfld                    name
     C                   kfld                    ext
     C                   kfld                    email
      *
     C     kd1           klist
     C                   kfld                    dname
     C                   kfld                    dext
     C                   kfld                    demail
      /free
      * set initial
        rcdnbr = 1;
        exsr  $clearsr;
        exsr  $loadsr;
      * write footer;
        opt = '';
      *
        dow *in03 = *Off;
          rcdnbr = 1;
          exfmt sflctl01;
          if *in03 = *on;
            *inlr = *on;
            return;
          endif;
          select;
            when *in06 = *On;
              exsr $addsub;
            other;
              readc sfldta01;
              if opt = 'C';
                opt = '';
                exsr $updsub;
              elseif opt = 'D';
                opt = '';
                exsr $dltsub;
              else;
              endif;
          endsl;
          exsr $clearsr;
          exsr $loadsr;
        enddo;
        *Inlr = *On;
        return;
      *
        BegSr   $addsub;
          dname  = *Blanks;
          dext   = *Blanks;
          demail = *Blanks;
          addmsg = *Blanks;
          Dow  *In12 = *Off;
            exfmt ADDREC;
            if *in12 = *on;
              *in12 = *off;
              leavesr;
            endif;
            If dname = *Blanks;
              addMSG = 'Name cannot be blanks.';
            Elseif   dext = *Blanks;
              addMSG = 'Ext cannot be blanks.';
            Elseif   demail = *Blanks;
              addMSG = 'Email cannot be blanks.';
            Else;
              name = dname;
              ext = dext;
              email = demail;
              write pfr;
              addMSG = 'Record added successfully...!';
              dname  = *Blanks;
              dext   = *Blanks;
              demail = *Blanks;
            Endif;
          Enddo;
        EndSr;
      *
        begsr $updsub;
          updmsg = '';
          Dow *In12 = *Off;
            name = dname;
            ext = dext;
            email = demail;
            exfmt updrec;
            if *in12 = *on;
              *in12 = *off;
              leavesr;
            endif;
            chain kf1 pfr;
            If %Found;
              name = dname;
              ext = dext;
              email = demail;
              update pfr;
              updmsg = 'Record update successfully...!';
              dname  = *Blanks;
              dext   = *Blanks;
              demail = *Blanks;
            Endif;
          Enddo;
        EndSr;
      *
        begsr $dltsub;
          dltmsg = '';
          dow *in12 = *off;
            exfmt dltcnf;
            if *in12 = *on;
              *in12 = *off;
              leavesr;
            endif;
            chain kd1 pfr;
            delete pfr;
            dltmsg = 'Record delete successfully...!';
            dname  = *Blanks;
            dext   = *Blanks;
            demail = *Blanks;
          enddo;
          setll *loval lf1;
          read pfr;
          if %eof(lf1);
            *in30 = *off;
            *in31 = *on;
            dname = *blanks;
            dext = *blanks;
            demail = *blanks;
            exfmt sflctl01;
          endif;
        endsr;
      *
        begsr $clearsr;
          *in30 = *off; //sfldsp
          *in31 = *off; //sfldspctl
          *in32 = *on ; //sflclr
          *in33 = *off;
          write sflctl01;

          *in30 = *on ;
          *in31 = *on ;
          *in32 = *off;
          *in33 = *on ;
          rcdnbr = 0;
        EndSr;
      *
        begsr $loadsr;
          Setll *Start lf1;
          read pfr;
          if %eof(lf1);
            *in30 = *off;
            *in31 = *on;
          else;
            *in30 = *on;
            *in31 = *on;
            dow not %eof(lf1);
              rcdnbr = rcdnbr + 1;
              dname = name;
              dext = ext;
              demail = email;
              write sfldta01;
              read pfr;
            Enddo;
          endif;
        EndSr;
      /End-Free 