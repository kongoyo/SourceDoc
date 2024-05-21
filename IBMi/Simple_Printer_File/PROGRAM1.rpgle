**free
dcl-f prtf1 printer ;

write HEADER ;

for Counter = 1 to 100 ;
  if (%error) ;
    write HEADER ;
  endif ;

  write(e) FORMAT01 ;
endfor;

return ;
