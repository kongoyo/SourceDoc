             PGM

             DCL        VAR(&JOBTYPE) TYPE(*CHAR) LEN(1)

             RTVJOBA    TYPE(&JOBTYPE)

          /* IF         COND(&JOBTYPE = '1') THEN(DO)         */
          /* SBMJOB     CMD(CALL PGM(PROGRAM0)) JOB(PROGRAM0) */
          /* RETURN                                           */
          /* ENDDO                                            */

             OVRPRTF    FILE(TESTPRTF) MAXRCDS(*NOMAX) SHARE(*YES)

             CALL       PGM(PROGRAM1)

             CALL       PGM(PROGRAM2)

             ENDPGM
