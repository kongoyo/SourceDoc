PGM

/* �w�q�ܼ� */
/* volnum �ϱa�s�� */
/* Y �~�ƥ� */
/* M ��ƥ� */
/* D ��ƥ� */

dcl var(&volnum) type(*char) len(6)
dcl var(&dof) type(*char) len(4)
dcl var(&lom) type(*char) len(1)

dcl var(&curdat) type(*char) len(6)
dcl var(&curjdat) type(*char) len(6)
dcl var(&foredat) type(*char) len(6)
dcl var(&datfmt) type(*char) len(3)
dcl var(&datsep) type(*char) len(1)

/* �p��P���X */
RTVSYSVAL SYSVAL(QDAYOFWEEK) RTNVAR(&dof)

/* �p��O�_�����̫�@�� */
rtvsysval SYSVAL(QDATFMT) RTNVAR(&datfmt)
rtvsysval SYSVAL(QDATSEP) RTNVAR(&datsep)
cvtdat DATE(&curdat) FROMFMT(&datfmt) TOFMT(*JUL) TOVAR(&curjdat)
chgvar &forejdat (&curjdat + 1)
cvtdat date(&forejdat) fromfmt(*jul) TOFMT(&datfmt) tovar(&foredat)  
if cond(%sst(&foredat 5 2) *eq '01') THEN(do)
    chgvar VAR(&lom) VALUE('Y')
enddo



/* �p��ϱa */
/* ����ƥ� */
/* �H�e�q�� */


ENDPGM