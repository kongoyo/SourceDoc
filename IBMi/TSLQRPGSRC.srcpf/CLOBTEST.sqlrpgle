       Identification Division.
       Program-ID. clobtest.

       Data Division.
       Working-Storage Section.
           EXEC SQL INCLUDE SQLCA END-EXEC.

           EXEC SQL BEGIN DECLARE SECTION END-EXEC.
       01 userid            pic x(8).
       01 passwd.
         49 passwd-length   pic s9(4) comp-5 value 0.
         49 passwd-name     pic x(18).
       01 empnum            pic x(6).
       01 di-begin-loc      pic s9(9) comp-5.
       01 di-end-loc        pic s9(9) comp-5.
       01 resume            USAGE IS SQL TYPE IS CLOB-LOCATOR.   [1]
       01 di-buffer         USAGE IS SQL TYPE IS CLOB-LOCATOR.
       01 lobind            pic s9(4) comp-5.
       01 buffer            USAGE IS SQL TYPE IS CLOB(1K).
           EXEC SQL END DECLARE SECTION END-EXEC.

       Procedure Division.
       Main Section.
           display "Sample COBOL program: LOBLOC".

      * Get database connection information.
           display "Enter your user id (default none): "
                with no advancing.
           accept userid.

           if userid = spaces
             EXEC SQL CONNECT TO sample END-EXEC
           else
             display "Enter your password : " with no advancing
             accept passwd-name.

      * Passwords in a CONNECT statement must be entered in a VARCHAR
      * format with the length of the input string.
           inspect passwd-name tallying passwd-length for characters
              before initial " ".

           EXEC SQL CONNECT TO sample USER :userid USING :passwd
               END-EXEC.

      * Employee A10030 is not included in the following select, because
      * the lobeval program manipulates the record for A10030 so that it is
      * not compatible with lobloc

           EXEC SQL DECLARE c1 CURSOR FOR
                    SELECT empno, resume FROM emp_resume
                    WHERE resume_format = 'ascii'
                    AND empno <> 'A00130' END-EXEC.

           EXEC SQL OPEN c1 END-EXEC.

           Move 0 to buffer-length.

           perform Fetch-Loop thru End-Fetch-Loop
              until SQLCODE not equal 0.

      * display contents of the buffer.
           display buffer-data(1:buffer-length).

           EXEC SQL FREE LOCATOR :resume, :di-buffer END-EXEC.

           EXEC SQL CLOSE c1 END-EXEC.

           EXEC SQL CONNECT RESET END-EXEC.
       End-Main.
           go to End-Prog.

       Fetch-Loop Section.
           EXEC SQL FETCH c1 INTO :empnum, :resume :lobind
              END-EXEC.

           if SQLCODE not equal 0
              go to End-Fetch-Loop.

      * check to see if the host variable indicator returns NULL.
           if lobind less than 0 go to NULL-lob-indicated.

      * Value exists.  Evaluate the LOB locator.
      * Locate the beginning of "Department Information" section.
           EXEC SQL VALUES (POSSTR(:resume, 'Department Information'))
                    INTO :di-begin-loc END-EXEC.

      * Locate the beginning of "Education" section (end of Dept.Info)
           EXEC SQL VALUES (POSSTR(:resume, 'Education'))
                     INTO :di-end-loc END-EXEC.

           subtract di-begin-loc from di-end-loc.

      * Obtain ONLY the "Department Information" section by using SUBSTR
           EXEC SQL VALUES (SUBSTR(:resume, :di-begin-loc,
                    :di-end-loc))
                    INTO :di-buffer END-EXEC.

      * Append the "Department Information" section to the :buffer var
           EXEC SQL VALUES (:buffer || :di-buffer) INTO :buffer
                    END-EXEC.

           go to End-Fetch-Loop.

       NULL-lob-indicated.
           display "NULL LOB indicated".

       End-Fetch-Loop. exit.

       End-Prog.
                  stop run.
 