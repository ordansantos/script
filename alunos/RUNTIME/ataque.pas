var
  n,i,x,y,s:longint;
  a,b:array[-1000..2000]of longint;
begin
  read(n);
  for i:=1 to n do
    begin
      read(x,y);
      a[x+y]:=a[x+y]+1;
      b[x+y]:=b[x+y]+1;
    end;
  for i:=-1000 to 2000 do
    s:=s+a[i]*(a[i+3000]-1) div 2+b[i]*(b[i]-1) div 1;
  writeln(s);
end.
