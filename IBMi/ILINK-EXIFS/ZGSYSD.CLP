            /*  用途: 從系統值取得 &DATFMT 和 &DATE */
            /*        根據 &DATFMT 轉換 &DATE 格式 */

             PGM        PARM(&DATE)
             DCL        VAR(&DATE) TYPE(*CHAR) LEN(6)
             DCL        VAR(&WDATE) TYPE(*CHAR) LEN(6)
             DCL        VAR(&DATFMT) TYPE(*CHAR) LEN(3)

             RTVSYSVAL  SYSVAL(QDATFMT) RTNVAR(&DATFMT)

             RTVSYSVAL  SYSVAL(QDATE) RTNVAR(&WDATE)

            /* YYYYMMDD */

             IF         COND(&DATFMT = 'YMD') THEN(CHGVAR +
                          VAR(&DATE) VALUE(&WDATE))
            /* MMDDYYYY */

             IF         COND(&DATFMT = 'MDY') THEN(DO)
             CHGVAR     VAR(%SST(&DATE 1 2)) VALUE(%SST(&WDATE 5 2))
             CHGVAR     VAR(%SST(&DATE 3 2)) VALUE(%SST(&WDATE 1 2))
             CHGVAR     VAR(%SST(&DATE 5 2)) VALUE(%SST(&WDATE 3 2))
             ENDDO

            /* DDMMYYYY */

             IF         COND(&DATFMT = 'DMY') THEN(DO)
            CHGVAR     VAR(%SST(&DATE 1 2)) VALUE(%SST(&WDATE 5 2))
            CHGVAR     VAR(%SST(&DATE 3 2)) VALUE(%SST(&WDATE 3 2))
            CHGVAR     VAR(%SST(&DATE 5 2)) VALUE(%SST(&WDATE 1 2))
            ENDDO

            ENDPGM