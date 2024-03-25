
select * from qsys2.system_status_info;

--- 列出主機型號、序號、名稱、CPU配置、屬性、記憶體配置、硬碟空間配置等資訊
select machine_model, machine_type, machine_serial_number, host_name, CPU_SHARING_ATTRIBUTE, CURRENT_CPU_CAPACITY, MAIN_STORAGE_SIZE/1024/1024 as MAIN_STORAGE_SIZE_GB, SYSTEM_ASP_STORAGE/1024 as SYSTEM_ASP_STORAGE_GB from qsys2.system_status_info;