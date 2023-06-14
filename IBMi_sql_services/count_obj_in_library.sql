--
-- description: Count objects in a library (superfast)
-- minvrm: v7r4m0
--
with libs (ln) as (
    select objname
      from table (
          qsys2.object_statistics('DDSCINFO', 'LIB')
        )
  )
  select ln, object_count 
    from libs, lateral (
           select *
             from table (
                 qsys2.library_info(system_schema_name => ln)
               )
         )
 order by object_count desc;
 
 
--
-- description: Count objects in a library (slowish)
-- minvrm: v7r3m0
--
 with libs (ln) as (
    select objname
      from table (
          qsys2.object_statistics('DDSCINFO', 'LIB')
        )
  )
  select ln, object_count 
    from libs, lateral (
           select count(*) as object_count
             from table (
                 qsys2.object_statistics(ln, '*ALL', '*ALLSIMPLE')
               )
         )
 order by object_count desc;
 
 
 
 select count(*) from table (qsys2.object_statistics('*ALLUSR','*ALL'));