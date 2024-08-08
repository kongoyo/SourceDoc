PGM

/* 定義變數 */
/* volnum 磁帶編號 */
/* Y 年備份 */
/* M 月備份 */
/* D 日備份 */

dcl var(&volnum) type(*char) len(6)
dcl var(&dof) type(*char) len(4)
dcl var(&lom) type(*char) len(1)

dcl var(&curdat) type(*char) len(6)
dcl var(&curjdat) type(*char) len(6)
dcl var(&foredat) type(*char) len(6)
dcl var(&datfmt) type(*char) len(3)
dcl var(&datsep) type(*char) len(1)

/* 計算星期幾 */
RTVSYSVAL SYSVAL(QDAYOFWEEK) RTNVAR(&dof)

/* 計算是否為當月最後一天 */
rtvsysval SYSVAL(QDATFMT) RTNVAR(&datfmt)
rtvsysval SYSVAL(QDATSEP) RTNVAR(&datsep)
cvtdat DATE(&curdat) FROMFMT(&datfmt) TOFMT(*JUL) TOVAR(&curjdat)
chgvar &forejdat (&curjdat + 1)
cvtdat date(&forejdat) fromfmt(*jul) TOFMT(&datfmt) tovar(&foredat)  
if cond(%sst(&foredat 5 2) *eq '01') THEN(do)
    chgvar VAR(&lom) VALUE('Y')
enddo



/* 計算磁帶 */
/* 執行備份 */
/* 寄送通知 */


ENDPGM