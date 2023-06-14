--
-- Note: 
-- Documentation for ACS's cldownload and other fantastic hidden gems can be found here:
-- ftp://ftp.software.ibm.com/as400/products/clientaccess/solutions/GettingStarted_en.html
--

--
-- Do I have the ACS jar on this IBM i?
--
select create_timestamp, acs.*
  from table (
      qsys2.ifs_object_statistics( start_path_name => '/QIBM/ProdData/Access/ACS/Base/acsbundle.jar')
    ) acs;
stop;

--
-- Is there an update available for the 'IBM HTTP Server for i' PTF Group
--
select *
  from systools.group_ptf_currency
  where ptf_group_title like '%IBM HTTP%';
stop;

--
-- Review the top 10 storage consumers
--
select a.authorization_name,
       sum(a.storage_used) as total_storage_used, b.text_description,
       b.accounting_code, b.maximum_allowed_storage
  from qsys2.user_storage a
       inner join qsys2.user_info b
         on b.user_name = a.authorization_name
  where b.user_creator <> '*IBM'
  group by a.authorization_name, b.text_description,
           b.accounting_code, b.maximum_allowed_storage
  order by total_storage_used desc
  limit 10;
stop;

--
-- Where in the IFS should I create the spreadsheet?
--
select create_timestamp, acs.*
  from table (
      qsys2.ifs_object_statistics( start_path_name => '/home/IBMECS/')
    ) acs order by create_timestamp desc limit 5;
stop;

--
-- What is the host name of this IBM i?
--
select HOST_NAME from qsys2.system_status_info X;

stop;
--
-- Procedure to drive the spreadsheet creation
--
drop procedure ddscinfo.generate_1_spreadsheet;
stop;

create procedure ddscinfo.generate_1_spreadsheet(
   in v_ifs_path varchar(1000) for sbcs data,
   in v_spreadsheet_query varchar(1000) for sbcs data)
begin
  declare cmdtext varchar(2000) for sbcs data;
  declare v_ifs_full_path varchar(2000) for sbcs data;
  set v_ifs_full_path = v_ifs_path concat
        lpad(month(current date), 2, 0) concat
        lpad(day(current date), 2, 0)   concat 
        year(current date) concat
        '.xlsx';
-- Note: more options...
-- Control options exist on CLDOWNLOAD.
-- /colheadings=<1/0>   ====      Include column headings as the first row. When specified, the column names will be the heading.
-- /usecollabels        ====      Use column labels for the heading.
-- Suffixes             ====      .csv, .ods, .xlsx
--
-- Note 2: 
-- Check to see whether your IBM i host name matches the name you specified on line 82...."/system=COMMON1"?
-- 1) execute this query: select HOST_NAME from qsys2.system_status_info;
-- 2) change line 82, the name after /system= should be your IBM i Host name.
--
  set cmdtext =
  'STRQSH CMD(''java -jar /QIBM/ProdData/Access/ACS/Base/acsbundle.jar '
        concat '/plugin=cldownload /system=V7R3N /clientfile='
        concat v_ifs_full_path concat ' /sql="' concat
        v_spreadsheet_query concat '"'')';
  call qsys2.qcmdexc(cmdtext);
end; 
stop;

--
-- Create a spreadsheet
--
call ddscinfo.generate_1_spreadsheet(v_ifs_path => '/home/IBMECS/theTop10',
                                      v_spreadsheet_query => 'select a.authorization_name,
       sum(a.storage_used) as total_storage_used, b.text_description,
       b.accounting_code, b.maximum_allowed_storage
  from qsys2.user_storage a
       inner join qsys2.user_info b
         on b.user_name = a.authorization_name
  group by a.authorization_name, b.text_description,
           b.accounting_code, b.maximum_allowed_storage
  order by total_storage_used desc
  limit 10');

stop; 


--
-- Did the file get created in the IFS?
--
select create_timestamp, acs.*
  from table (
      qsys2.ifs_object_statistics( start_path_name => '/home/IBMECS/')
    ) acs 
    where path_name like '/home/IBMECS/theTop10%'
    order by create_timestamp desc limit 1;
stop;

--
-- Email the spreadsheet 
--

-- One time setup!
cl: STRTCPSVR SERVER(*SMTP)  ;
cl: ADDUSRSMTP USRPRF(SCOTTF);

stop;

--
-- Email an IFS file
-- Note: The SNDSMTPEMM command include more parameter options that could be extended here
--
create or replace procedure coolstuff.email_1_spreadsheet(
   in v_ifs_path varchar(100) for sbcs data,
   in v_email    varchar(100) for sbcs data,
   in v_subject  varchar(100) for sbcs data,
   in v_note     varchar(100) for sbcs data
   )
begin
  declare v_cmdstmt varchar(2000) for sbcs data;
  set v_cmdstmt =
  'SNDSMTPEMM RCP((''' concat v_email concat ''' *pri)) SUBJECT(''' concat v_subject concat ''') NOTE(''' concat v_note concat ''') ATTACH((''' concat v_ifs_path concat '''))'; 
  call qsys2.qcmdexc(v_cmdstmt);
end; 
stop;

--
-- Email an IFS file
--
call coolstuff.email_1_spreadsheet( v_ifs_path => '/home/SCOTTF/theTop1008032020.xlsx',
                                    v_email    => 'forstie@us.ibm.com', 
                                    v_subject  => 'Email sent by coolstuff.email_1_spreadsheet', 
                                    v_note     => 'Here is your top 10 list of storage consumers') ;
stop;


create or replace procedure coolstuff.create_and_email_top10()
begin
declare local_ifs_path_name varchar(100) for sbcs data;
--
-- Create a spreadsheet
--
call coolstuff.generate_1_spreadsheet(v_ifs_path => '/home/SCOTTF/theTop10',
                                      v_spreadsheet_query => 'select a.authorization_name,
       sum(a.storage_used) as total_storage_used, b.text_description,
       b.accounting_code, b.maximum_allowed_storage
  from qsys2.user_storage a
       inner join qsys2.user_info b
         on b.user_name = a.authorization_name
  group by a.authorization_name, b.text_description,
           b.accounting_code, b.maximum_allowed_storage
  order by total_storage_used desc
  limit 10');
  
select path_name into local_ifs_path_name
  from table (
      qsys2.ifs_object_statistics( start_path_name => '/home/SCOTTF/')
    ) acs 
    where path_name like '/home/SCOTTF/theTop10%'
    order by create_timestamp desc limit 1;

call coolstuff.email_1_spreadsheet( v_ifs_path => local_ifs_path_name,
                                    v_email    => 'forstie@us.ibm.com', 
                                    v_subject  => 'Email sent by coolstuff.email_1_spreadsheet', 
                                    v_note     => 'Here is your top 10 list of storage consumers') ;
end;

stop;

-- Create the spreadsheets on a schedule
cl: ADDJOBSCDE JOB(SCOTTSS1) CMD(RUNSQL SQL('call coolstuff.create_and_email_top10()') COMMIT(*NONE) NAMING(*SQL)) FRQ(*WEEKLY) SCDDATE(*NONE) SCDDAY(*ALL) SCDTIME(235500)   ;
