        **free
        ctl-opt option(*srcstmt) dftactgrp(*no) ;

        dcl-ds Differences qualified dim(999) ;
          Attribute char(100) ;
          File1 char(10) ;
          File2 char(10) ;
        end-ds ;

        dcl-s Rows uns(5) ;
        dcl-s i like(Rows) ;

        exec sql SET OPTION COMMIT = *NONE, CLOSQLCSR = *ENDMOD ;

        MakeNewFile() ;

        //test
        exec sql call qsys2.qcmdexc('RUNSQLSTM SRCFILE(MYLIB/DEVSRC) +
                                                 SRCMBR(TEST1SQL) +
                                                 COMMIT(*NC)') ;
        //test end

        Comparison() ;

        if (Rows > 0) ;
          MakeDifferencesFile() ;
        endif ;

        *inlr = *on ;
        //exec sql DROP TABLE MYLIB.EXITS_NEW ; 