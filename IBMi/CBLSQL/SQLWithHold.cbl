*-----------------------------------------------------------------------------
* 程式名稱：SQLWithHold.cob
* 程式說明：示範如何在 IBM i COBOL 中使用 WITH HOLD 控制 cursor
*-----------------------------------------------------------------------------

identification division.
program-id. SQLWithHold.

environment division.
configuration section.
repository.
data-base name is 'DB2'.

data division.
working-storage section.
01  employee-record.
    05  employee-number pic 9(5).
    05  employee-name pic x(30).
    05  employee-department pic x(10).

01  sql-statement pic x(100).

01  sql-code pic 9(9).
01  sql-message pic x(70).

01  cursor-handle pic x(16).

procedure division.
begin.

    * 宣告 cursor

    set sql-statement to
        'SELECT employee_number, employee_name, employee_department
        FROM employee
        WHERE employee_department = ''Sales''
        ORDER BY employee_number'.

    execute sql-statement
        returning cursor-handle
        into cursor-handle.

    * 使用 WITH HOLD 控制 cursor

    open cursor-handle
        with hold.

    * 取回第一筆資料

    fetch first from cursor-handle
        into employee-record.

    * 顯示第一筆資料

    display employee-record.

    * 取回下一筆資料

    fetch next from cursor-handle
        into employee-record.

    * 顯示下一筆資料

    display employee-record.

    * 關閉 cursor

    close cursor-handle.

end.
