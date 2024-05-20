             PGM

             /* QC3GENRN API PARAMETERS */
             DCL VAR(&DATA) TYPE(*CHAR) LEN(4)  VALUE('    ')
             DCL VAR(&DATALEN) TYPE(*INT) LEN(4)  VALUE(4)
             DCL VAR(&TYPE) TYPE(*CHAR) LEN(1)  VALUE('0')
             DCL VAR(&PARITY) TYPE(*CHAR) LEN(1)  VALUE('0')
             DCL VAR(&QUSEC) TYPE(*INT) LEN(4)  VALUE(0)

             /* SOME WORKING VARS */
             DCL VAR(&WORK1) TYPE(*INT) LEN(4) VALUE(0)
             DCL VAR(&WORK2) TYPE(*INT) LEN(4) VALUE(0)

             /* RESULT - RANDOM NUMBER 1-1000 */
             DCL        VAR(&RANDOM) TYPE(*DEC) LEN(4 0) VALUE(0)
             DCL        VAR(&NAME) TYPE(*CHAR) LEN(8)
             DCL        VAR(&EMAIL) TYPE(*CHAR) LEN(20)
             DCL        VAR(&EXT) TYPE(*CHAR) LEN(4)
             DCL        VAR(&CNT) TYPE(*DEC) LEN(3 0)
             DCL        VAR(&CHRCNT) TYPE(*DEC) LEN(1 0)
             DCL        VAR(&RANDOMC) TYPE(*CHAR) LEN(4)
             DCL        VAR(&STMT) TYPE(*CHAR) LEN(1000)
             DCL        VAR(&ERR) TYPE(*DEC) LEN(3 0)

             DOUNTIL    COND(&CNT *GT 998)
             /* CALL API */
             CALL PGM(QC3GENRN) PARM(&DATA &DATALEN &TYPE &PARITY &QUSEC)

             /* CONVERT BINARY RANDOM DATA TO DECIMAL 0 - 999 */
             CHGVAR     VAR(&WORK1) VALUE(%BINARY(&DATA 1 4))
             IF COND(&WORK1 *LT 0) THEN(CHGVAR VAR(&WORK1) VALUE(&WORK1 * -1))
             CHGVAR VAR(&WORK2) VALUE(&WORK1 / 1000)
             CHGVAR VAR(&WORK1) VALUE(&WORK1 - (&WORK2 * 1000))

             /* SET RESULT VARIABLE TO RANGE 1 - 1000 */
             CHGVAR VAR(&RANDOM) VALUE(&WORK1 + 1)

             CHGVAR     VAR(&RANDOMC) VALUE(&RANDOM)
             CHGVAR     VAR(&CHRCNT) VALUE(%SIZE(&RANDOMC))

             CHGVAR     VAR(&NAME) VALUE('T' *TCAT &RANDOMC)
             CHGVAR     VAR(&EXT) VALUE(&RANDOMC)
             CHGVAR     VAR(&EMAIL) VALUE('T' *TCAT &RANDOMC +
                          *TCAT '@DDSC.COM.TW')

             CHGVAR     VAR(&STMT) VALUE('INSERT INTO DDSCINFO/LF1 +
                          VALUES(''' *TCAT &NAME *TCAT ''', ''' *TCAT +
                          &EMAIL *TCAT ''', ''' *TCAT &EXT *TCAT ''')')
             SNDPGMMSG  MSG(&STMT)
             RUNSQL     SQL(&STMT) COMMIT(*NONE)
             MONMSG     MSGID(SQL9010) EXEC(DO)
               CHGVAR     VAR(&ERR) VALUE(&ERR + 1)
             ENDDO

             CHGVAR     VAR(&CNT) VALUE(&CNT + 1)
             ENDDO
             SNDPGMMSG  MSG('Total Count: ' *CAT %CHAR(&CNT) *CAT '. +
                          Total Error count: ' *CAT %CHAR(&ERR))
             ENDPGM 