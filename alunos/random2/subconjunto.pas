var V: array [1..10] of longint;
    A: array [1..100000] of longint;
    i,i1,i2:longint; n,kil,x:longint; max:int64;
    chys1,chys2,chys3:longint; n1:extended;
begin
     read(n);
     i:=1;
     while i<=n do
     begin
         read(A[i]);
         inc(i)
     end;
     V[1]:=1; kil:=1;
     i:=2; n1:=n; chys2:=1;
     chys3:=1;
     while chys1<=trunc(n1/3) do
     begin
          chys2:=chys2*4;
          if i<>2 then
          begin
            chys3:=chys3*2;
          end;
          chys1:=chys2+3*chys3+1;
          if chys1<=trunc(n1/3) then
          begin
               V[i]:=chys1;
          end;
          inc(kil);
          inc(i);
     end;
     i:=kil-1;
     while i>=1 do
     begin
          i1:=1;
          while i1<=n do
          begin
               if i1-V[i]>=1 then
               begin
                 i2:=i1-V[i];
                 while i2>=1 do
                 begin
                     if (A[i2+V[i]]<A[i2]) and (i2+V[i]<=n) then
                     begin
                       x:=A[i2+V[i]];
                       A[i2+V[i]]:=A[i2];
                       A[i2]:=x;
                     end
                     else
                     begin
                         break;
                     end;
                     i2:=i2-V[i];
                 end;
               end;
               inc(i1)
          end;
          dec(i);
     end;
     i:=1; max:=0;
     while i<=n do
     begin
         max:=max+A[i];
         inc(i);
     end;
     if max mod 2=0 then write(max);
     if max mod 2<>0 then
     begin
       i:=1;
       while i<=n do
       begin
           if A[i] mod 2<>0 then
           begin
                max:=max-A[i];
           end;
           if max mod 2=0 then break;
           inc(i);
       end;
       write(max);
     end;
end.
