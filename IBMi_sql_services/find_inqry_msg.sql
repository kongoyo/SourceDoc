with qsysopr_inquiries_today (msg, asker, text, key) as (
       select message_id, from_user, message_text, message_key
         from qsys2.message_queue_info
         where message_queue_library = 'QSYS'
               and message_queue_name = 'QSYSOPR'
               and message_type = 'INQUIRY'
               and date(message_timestamp) = current_date  
     ),
     qsysopr_answers_today (assoc_key) as (
       select associated_message_key
         from qsys2.message_queue_info
         where message_queue_library = 'QSYS'
               and message_queue_name = 'QSYSOPR'
               and message_type = 'REPLY'
               and date(message_timestamp) = current_date 
     )
  select msg, asker, text
    from qsysopr_inquiries_today
    where key not in (select assoc_key
          from qsysopr_answers_today); 