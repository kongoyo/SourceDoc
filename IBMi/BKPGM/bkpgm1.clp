     PGM
     DCL        VAR(&DATE) TYPE(*CHAR) LEN(8)
     DCL        VAR(&TIME) TYPE(*CHAR) LEN(6)
     DCL        VAR(&CMD) TYPE(*CHAR) LEN(100)
     DCL        VAR(&SRCFILE) TYPE(*CHAR) LEN(10)
     DCL        VAR(&LIBRARY) TYPE(*CHAR) LEN(10)
     DCL        VAR(&DAYOFWEEK) TYPE(*CHAR) LEN(1)
     DCL        VAR(&WEEKDAY) TYPE(*CHAR) LEN(3)
     DCL        VAR(&WEEKDAYS) TYPE(*CHAR) LEN(7) VALUE('SUNMONTUEWEDTHUFRISAT')

     /* 获取当前日期和时间 */
     RTVSYSVAL  SYSVAL(QDATE) RTNVAR(&DATE)
     RTVSYSVAL  SYSVAL(QTIME) RTNVAR(&TIME)

     /* 获取当前星期几 */
     CVTDAT     DATE(&DATE) TOVAR(&WEEKDAY) FROMFMT(*JOB) TOFMT(*WKDAY)
     CHGVAR     VAR(&DAYOFWEEK) VALUE(%SST(&WEEKDAYS %LOOKUP(&WEEKDAY &WEEKDAYS)))

     /* 检查是否为星期六或星期日 */
     IF         COND(&DAYOFWEEK *EQ 'SAT' *OR &DAYOFWEEK *EQ 'SUN') THEN(DO)
       SNDPGMMSG  MSG('星期六和星期日不执行备份。') MSGTYPE(*COMP)
       RETURN
     ENDDO

     /* 设置备份文件名称 */
     CHGVAR     VAR(&SRCFILE) VALUE('MYFILE')
     CHGVAR     VAR(&LIBRARY) VALUE('MYLIB')

     /* 构造备份命令 */
     CHGVAR     VAR(&CMD) VALUE('SAVOBJ OBJ(' || &LIBRARY || '/' || &SRCFILE || ') +
                                LIB(MYLIB) +
                                DEV(*SAVF) +
                                SAVF(MYLIB/BACKUP_' || &DATE || '_' || &TIME || ')')

     /* 执行备份命令 */
     CALL       PGM(QCMDEXC) PARM(&CMD 100)

     /* 显示备份完成消息 */
     SNDPGMMSG  MSG('备份已完成。') MSGTYPE(*COMP)

     ENDPGM
