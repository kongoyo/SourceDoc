select *
from qsys2.sysprocs
where EXTERNAL_LANGUAGE = 'CL'
or SQL_DATA_ACCESS = 'NONE'
order by specific_schema;

select * from qsys2.sysroutine order by specific_schema;

select * from qsys2.sysprocs order by specific_schema;

select * from qsys2.sysparms order by specific_schema;