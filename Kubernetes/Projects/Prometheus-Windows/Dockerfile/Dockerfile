ARG BASE="mcr.microsoft.com/windows/nanoserver:1809"
FROM $BASE

ENV PATH="C:\Windows\system32;C:\Windows;"
COPY output/amd64/windows_exporter.exe /windows_exporter.exe
ENTRYPOINT ["windows_exporter.exe"]