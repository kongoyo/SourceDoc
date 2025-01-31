PGM

DCL VAR(&INP) TYPE(*CHAR) LEN(1000)
DCL VAR(&SQLCMD) TYPE(*CHAR) LEN(1000)
DCL VAR(&CONFIRM) TYPE(*CHAR) LEN(1)

DCLF FILE(QTEMP/SQLRSLT)

DOWHILE COND('1')
  /* 提示使用者輸入SQL指令 */
  SNDUSRMSG MSG('請輸入SQL指令:') MSGRPY(&INP)

  /* 顯示使用者輸入並確認 */
  SNDPGMMSG MSG('您輸入的SQL指令是:')
  SNDPGMMSG MSG(&INP)
  SNDUSRMSG MSG('輸入是否正確? (Y/N)') MSGRPY(&CONFIRM)
  IF COND(&CONFIRM *NE 'Y') THEN(ITERATE)

  /* 準備SQL指令 */
  CHGVAR VAR(&SQLCMD) VALUE('RUNSQL SQL(''' *CAT &INP *TCAT ''') +
                            COMMIT(*NONE) NAMING(*SQL)')

  /* 執行SQL指令 */
  CALL PGM(QSYS/QCMDEXC) PARM(&SQLCMD 1000)

  /* 顯示結果 */
  SNDPGMMSG MSG('SQL指令執行結果:')
  RCVF
  DOW %EOF = '0'
    SNDPGMMSG MSG(&RESULT)
    RCVF
  ENDDO

  /* 確認結果是否正確 */
  SNDUSRMSG MSG('結果是否正確? (Y/N)') MSGRPY(&CONFIRM)
  IF COND(&CONFIRM *EQ 'Y') THEN(LEAVE)
ENDDO

SNDPGMMSG MSG('程式執行完成。')

ENDPGM
