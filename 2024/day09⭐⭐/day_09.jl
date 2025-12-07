function C(D)
    g,r = 1,length(D)+1
    while g<r
        r -= 1
        D[r][1]==0 && continue
        l = findnext(d->d[1]==0 && d[2]≥D[r][2], D, g)
        l≥r && continue
        D[l],D[r] = D[r],D[l]
        if D[l][2]≠D[r][2]
            insert!(D, l+1, [0,D[r][2]-D[l][2]])
            D[r+=1][2] = D[l][2]
        end
        g = findnext(d->d[1]==0, D, g)
    end
    v = vcat([fill(d...) for d∈D]...)
    sum(i->(v[i]≠0)*(i-1)*(v[i]-1), keys(v))
end
S = read("09.txt", String)
D = [[isodd(i)*fld(i+1,2),S[i]-'0'] for i∈keys(S) if S[i]>'0']
C([(l,1) for (l,s)∈D for _∈1:s]), C(D)