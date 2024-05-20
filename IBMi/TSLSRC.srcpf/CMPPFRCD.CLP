             PGM

             DCL        VAR(&STMT) TYPE(*CHAR) LEN(2000)

             CHKOBJ     OBJ(DDSCTSL/CMPPFMBR) OBJTYPE(*FILE)
             MONMSG     MSGID(CPF9801) EXEC(GOTO CMDLBL(BEG))
             CHGVAR     VAR(&STMT) VALUE('DROP TABLE DDSCTSL.CMPPFMBR')
             RUNSQL     SQL(&STMT) COMMIT(*NONE)

 BEG:        CHGVAR     VAR(&STMT) VALUE('CREATE TABLE +
                          DDSCTSL.CMPPFMBR AS (SELECT A.MBSYSN AS +
                          AMBSYSN, A.MBLIB AS AMBLIB, A.MBFILE AS +
                          AMBFILE, A.MBNAME AS AMBNAME, A.MBNRCD AS +
                          AMBNRCD, A.MBCHGD AS AMBCHGD, A.MBCHGT AS +
                          AMBCHGT,B.MBSYSN AS BMBSYSN, B.MBLIB AS +
                          BMBLIB, B.MBFILE AS BMBFILE, B.MBNAME AS +
                          BMBNAME, B.MBNRCD AS BMBNRCD, B.MBCHGD AS +
                          BMBCHGD, B.MBCHGT AS BMBCHGT FROM +
                          DDSCTSL.ALLPFMBRO A LEFT JOIN +
                          DDSCTSL.ALLPFMBRN B ON A.MBLIB = B.MBLIB +
                          AND A.MBFILE = B.MBFILE AND A.MBNAME = +
                          B.MBNAME WHERE (A.MBLIB = ''APRDW10'' OR +
                          A.MBLIB = ''BPRDW10'' OR A.MBLIB = +
                          ''CPRDW10'' OR A.MBLIB = ''IPRDW10'' OR +
                          A.MBLIB = ''UPRDW10'' ) AND (B.MBSYSN IS +
                          NULL OR A.MBNRCD <> B.MBNRCD)) WITH DATA')

             RUNSQL     SQL(&STMT) COMMIT(*NONE)

             RUNQRY     QRY(DDSCTSL/CMPPFMBRQ) +
                          QRYFILE((DDSCTSL/CMPPFMBR)) OUTTYPE(*PRINTER)

             ENDPGM 