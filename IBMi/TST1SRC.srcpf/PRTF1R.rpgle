**free
ctl-opt option(*nodebugio);
dcl-f lf1 disk(*ext) usage(*input:*output) keyed;
dcl-f prtf1 printer(*ext);

dcl-s pageOverflow ind;
dcl-s cnt int(3);
dcl-s pagnbr int(3);

cnt = 1;
pagnbr = 1;
pageOverflow = *off;

write HEADER;

setll *loval pfr;
read pfr;
dow not %eof;
  if cnt > 10;
    pageOverflow = *on;
    if pageOverflow = *on;
      pagnbr = pagnbr + 1;
      write header;
      pageOverflow = *off;
      cnt = 0;
    endif;
  endif;
  write pdta;
  read pfr;
  cnt = cnt + 1;
enddo;

write endreport;

*inlr = *on;
